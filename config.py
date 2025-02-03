#importing the required library
import requests
import datetime
from googletrans import Translator
import together
from cachetools import TTLCache
import time
# API Details
API_URL = "https://api.together.xyz/v1/chat/completions"
API_KEY = "add_your_together_api_key_here" 
#model 
model="meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo"# change the model here
# URL to fetch the crypto details
coingecko_url = "https://api.coingecko.com/api/v3"
# Google translator to detect and translate user input
translator = Translator()
# Create an in-memory cache (TTL: 60 seconds, max size: 100 items)
cache = TTLCache(maxsize=100, ttl=60)