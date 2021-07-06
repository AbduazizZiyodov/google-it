from os import getenv
from dotenv import load_dotenv
from googleapiclient.discovery import build


load_dotenv()

API_KEY: str = getenv('GOOGLE_API_KEY')
CSE: str = getenv('CSE_ID')


def search(search_term: str, api_key: str, cse_id: str, **kwargs) -> list:
    service = build("customsearch", "v1", developerKey=api_key)
    response = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
    return response['items']


def get_results(term: str = "google") -> list:
    results = search(term, API_KEY, CSE, num=10)
    return [result['link'] for result in results]