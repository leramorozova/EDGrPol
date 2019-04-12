"""
Реализация поиска по лемме
"""

from .db_utils import Database


def full_lemma_search(request):
    """
    Search by lemma in title lemmas, morph and phonetic variants
    :param request: form arguments
    :return: array of result lemmas
    """
    db = Database()
    result = db.execute("""SELECT * FROM SimpleFields
               """, 0)
    if result is not None:
        return result
    else:
        pass  # тут будет фонетический поиск и всякое такое
    return None
