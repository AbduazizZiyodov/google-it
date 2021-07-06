from os import getenv
from dotenv import load_dotenv
from googleapiclient.discovery import build

# For getting enviroment variables from .env file
load_dotenv()

API_KEY: str = getenv('GOOGLE_API_KEY')
CSE: str = getenv('CSE_ID')


def search(search_term: str, api_key: str, cse_id: str, **kwargs) -> list:
    """
    - search_term : no comment
    - api_key : from https://developers.google.com/custom-search/v1/introduction (click get API key)
    - cse_id : after creating search engine, you can get it from its settings page
    """
    service = build("customsearch", "v1", developerKey=api_key)
    response = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
    return response['items']


def get_results(term: str = "google") -> list:
    """
    Default search term is 'google'
    """
    results = search(term, API_KEY, CSE, num=10)
    return [result['link'] for result in results]
