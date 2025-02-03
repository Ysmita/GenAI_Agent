import config
# Fetch Bitcoin details dynamically
def fetch_bitcoin_details(detail_type="price", days=30): #By default fetech data from previous 30 days
        try:
            response = config.requests.get(f"{config.coingecko_url}/coins/bitcoin")
            response.raise_for_status()
            data = response.json()

            if detail_type == "history":
                return fetch_bitcoin_history(days)

            if detail_type == "price":
                return f"Current Bitcoin price: ${data['market_data']['current_price']['usd']:,} USD."
            elif detail_type == "market":
                return (f"Market Cap: ${data['market_data']['market_cap']['usd']:,}\n"
                        f"24h Volume: ${data['market_data']['total_volume']['usd']:,}")
            elif detail_type == "supply":
                return (f"Total Supply: {data['market_data']['total_supply']:,} BTC\n"
                        f"Circulating Supply: {data['market_data']['circulating_supply']:,} BTC")
            elif detail_type == "ath":
                return (f"All-Time High (ATH): ${data['market_data']['ath']['usd']:,} USD\n"
                        f"ATH Date: {data['market_data']['ath_date']['usd'][:10]}")
            else:
                return " I couldn't recognize the request. Try asking for 'price', 'market', 'history', 'supply', or 'ATH'."

        except config.requests.exceptions.RequestException as e:
            return f" Error fetching Bitcoin details: {str(e)}"

# Fetch Bitcoin price history for a given duration
def fetch_bitcoin_history(days):
        try:
            response = config.requests.get(f"{config.coingecko_url}/coins/bitcoin/market_chart?vs_currency=usd&days={days}")
            response.raise_for_status()
            data = response.json()

            prices = data['prices']
            formatted_prices = "\n".join([
                f"Date: {config.datetime.datetime.utcfromtimestamp(price[0] // 1000).strftime('%Y-%m-%d')},  Price: ${price[1]:,.2f}"
                for price in prices[:5]  # Show first 5 days for brevity
            ])
            return f" Bitcoin history for the last {days} days:\n{formatted_prices}..."

        except config.requests.exceptions.RequestException as e:
            return f" Error fetching Bitcoin history: {str(e)}"