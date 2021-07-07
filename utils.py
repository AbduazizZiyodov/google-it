from telebot.types import InlineQuery
from core import googleit


bad_words: list = ['bad']


def get_search_results(query: InlineQuery) -> str:
    query, results = query.query.lower(), "[🔍Search results🤓]\n\n"
    for index, result in enumerate(googleit(term=query)):
        results += f'🔰{index+1}) {result}\n'
    return results


def check(query: InlineQuery) -> bool:
    term = query.query.lower()
    for word in bad_words:
        if word in term:
            return False
    return True
