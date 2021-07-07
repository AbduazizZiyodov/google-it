from telebot.types import InlineQuery
from core import googleit


def get_search_results(query: InlineQuery) -> str:
    query, results = query.query.lower(), "[🔍Search results🤓]\n\n"
    total: int = 0
    for index, result in enumerate(googleit(term=query)):
        results += f'🔰{index+1}) {result}\n'
        total += 1
    return results