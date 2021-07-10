from googleapiclient.discovery import build

from settings import config


key, cse = config['GOOGLE_API_KEY'], config['CSE_ID']


def search(search_term: str, api_key: str,
           cse_id: str, **kwargs) -> list:
    """
    - search_term : no comment
    - api_key : from https://developers.google.com/custom-search/v1/introduction (click get API key)
    - cse_id : after creating search engine, you can get it from its settings page
    """
    service = build("customsearch", "v1", developerKey=api_key)
    response = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()

    return response['items']


def googleit(term: str = "django null constraint failed") -> list:
    """
    Default search term is 'google'
    """
    if len(term) == 0:
        return []
    return [result['link'] for result in search(term, key, cse, num=10)]
