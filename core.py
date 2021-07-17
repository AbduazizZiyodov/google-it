from googleapiclient.discovery import build

from settings import CSE_ID
from settings import GOOGLE_API_KEY


key, cse = GOOGLE_API_KEY, CSE_ID


service = build("customsearch", "v1", developerKey=key)


def search(search_term: str,
           cse_id: str, **kwargs) -> list:
    """
    - api_key : https://developers.google.com/custom-search/v1/introduction
    - cse_id : you can get it from your search engine's settings
    """

    response = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()

    return response['items'] if 'items' in response else []


def googleit(term: str = "sql insert") -> list:
    """
    Default search term is 'google'
    """
    search_results = search(term, cse, num=10)

    return [
        {
            'title': result['title'],
            'link':result['link'],
        }
        for result in search_results
    ]
