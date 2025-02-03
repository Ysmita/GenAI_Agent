import config
import translate
import crypto_data_api

def generate_response(user_input):
    """If the input is already available in cache, fetech data from cache"""
    if user_input in config.cache:
        print(f"Cache hit for prompt: {user_input}")
        return config.cache[user_input]
    """Send user input to Together AI and get the response."""
    headers = {
        "Authorization": f"Bearer {config.API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model":config.model,
        "messages": [{"role": "user", "content": user_input}],
        "max_tokens": 150,
        "temperature": 0.7
    }
    

    try:
        response = config.requests.post(config.API_URL, json=payload, headers=headers)
        response.raise_for_status()  # Raise an error for bad responses (4xx, 5xx)
        if response.status_code == 429:  # Too Many Requests
            # Extract the time the rate limit resets
            reset_time = int(response.headers.get('X-RateLimit-Reset', time.time()))
            current_time = time.time()
            wait_time = reset_time - current_time + 1  # Wait until the rate limit is reset
            print(f"Rate limit exceeded, waiting for {wait_time} seconds...")
            time.sleep(wait_time)  # Sleep until the rate limit is reset
            return generate_response(user_input)  # Retry the API call
        config.cache[user_input] =response.json()["choices"][0]["message"]["content"]
        return response.json()["choices"][0]["message"]["content"]
    except config.requests.exceptions.RequestException as e:
        return f"Error fetching AI response: {str(e)}"

    #  Handle user messages dynamically
def handle_message( message):
        context.append(message)
        message_in_english = translate.detect_and_translate(message)
        message_lower = message_in_english.lower()
        if "bitcoin" in message_lower:
            if "price" in message_lower :
                return crypto_data_api.fetch_bitcoin_details("price")
            elif "market" in message_lower or "cap" in message_lower or "volume" in message_lower:
                return crypto_data_api.fetch_bitcoin_details("market")
            elif "history" in message_lower:
                try:
                    days = int(message.split()[-2])
                    return crypto_data_api.fetch_bitcoin_details("history", days)
                except (ValueError, IndexError):
                    return crypto_data_api.fetch_bitcoin_details("history")
            elif "supply" in message_lower:
                return crypto_data_api.fetch_bitcoin_details("supply")
            elif "all-time high" in message_lower or "ath" in message_lower:
                return crypto_data_api.fetch_bitcoin_details("ath")
            else:
                ai_response = generate_response(f"User: {message_in_english}\nAI:")
                return f"{ai_response}"
        else:
            ai_response = generate_response(f"User: {message_in_english}\nAI:")
            return f" {ai_response}"

#  Example interactions
context=[]
print("To leave the conversation, type 'exit'.")
while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print(" Goodbye!")
        break

    response = handle_message(user_input)
    print("AI: ",response)
    print("\n")