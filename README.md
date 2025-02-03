# GenAI_Agent
With English as its primary communication language, this simple AI agent was created using python to get cryptocurrency prices (particularly, Bitcoin) and respond to language translation requests. The agent connects with the CoinGecko API to retrieve real-time cryptocurrency prices and generates conversations using the Together AI LLaMA 3.1 8B model. Furthermore, the agent can translate customer queries into English from other languages.
## Features
**Cryptocurrency Price Fetching:** Utilize the CoinGecko API to obtain the most recent price of Bitcoin and other supported cryptocurrencies.

**Language Translation:** Makes sure that all system responses are in English by automatically translating user input that is not in English into English.

**Conversation History:** Preserves the context of the conversation to produce pertinent and well-organized answers throughout several exchanges.

**Caching and Rate Limiting:** To avoid overloading the CoinGecko API, minimal caching for cryptocurrency prices is implemented, and API rate restrictions are respected.

## Requirements
The requirements are listed in requirements.txt

## Setup Instructions
1) **Clone the repository**
   
   git clone https://github.com/Ysmita/GenAI-agent.git
   
   cd GenAI-agent
2) **Install the dependences**
   
   pip install -r requirements.txt
   
3) **Add your API key**
4) 
   Add your together API key in config.py.

   This is required to interact with the LLaMA model from **together API**
   
   In case you want to use a different model, update the same in config.py

 5) **Run the agent**

      After doing the setup and installing the dependencies, run agent.py
    
    Once the agent is up and running, you can interact with it via the terminal. Even if you enter questions in a different language, the agent will reply in English. It can     translate non-English input and retrieve bitcoin prices.
    
  6) **Reference**
   
     To find example conversations refer to Report.docx

## API Integrations
1) **The CoinGecko API**
   
   The CoinGecko API, which is free and doesn't require an API key, is used by the agent to retrieve cryptocurrency prices.

    [CoinGecko API](https://www.coingecko.com/en/api)

2) **Together API**

   Conversations are handled by the AI agent using Together AI's LLaMA 3.1 8B model.

   [official documentation Together API](https://www.together.ai)

3) **Google Translate API**

   The agent uses the googletrans library to translate user input into English for consistent system responses.

## Improvements and Future Scope

The following features could enhance this project's straightforward implementation:

1) **Improved Error Handling:**
   
   Retry queries in the event that an API call fails or produces rate-limited answers to handle API failures more tactfully.

2) **Multi-User:**

   To accommodate several users at once with separate contexts, employ session handling.

3) **Increased CryptoCurrency Support:**

   The current project supports only bitcoin. This can be extended to other cryptocurrencies by using appropriate APIs.

## Assumptions and Limitations:

1)	**Performance:**

  	AI Agent performance varies depending on the model chosen.

  	In the current project we have chosen Meta-Llama-3.1-8B-Instruct-Turbo model(as listed in together.ai)

2)	**Translation Qualtiy:**
  
      The translation quality depends on the translation service. (googletranslate)
   
      Might not be able to handle complex words or languages


    
   
