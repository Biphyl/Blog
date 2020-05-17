import urllib.request,json
from config import Config
from .models import Quotes

quotes_api = Config.QUOTES_API
base_url = None
def get_Quotes():
  
  with urllib.request.urlopen(quotes_api) as url:
      quotes_api_data = url.read()
      quotes_api_response = json.loads(quotes_api_data)

      quote_object = None
      if quotes_api_response:
        author = quotes_api_response['author']
        quote = quotes_api_response['quote']    
        quote_object = Quotes(author=author , quote=quote)
  return quote_object