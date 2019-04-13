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
    result = db.execute("""SELECT lemma_rus FROM simple_fields
                            WHERE lemma_rus LIKE '%""" + request + """%'
               """, 0)
    ret = []
    if result is not None:
        for lemma in result:
            ret.append(lemma[0])
        return ret
    else:
        pass  # тут будет фонетический поиск и всякое такое
    return None
