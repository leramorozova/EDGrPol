"""
Реализация поиска по лемме
"""

from .db_utils import Database


class Article:
    def __init__(self, id, lemma):
        self.id = id
        self.lemma = lemma


def full_lemma_search(request):
    """
    Search by lemma in title lemmas, morph and phonetic variants
    :param request: form arguments
    :return: array of result lemmas
    """
    db = Database()
    result = db.execute("""SELECT id, lemma_rus FROM simple_fields
                            WHERE lemma_rus LIKE '%""" + request + """%'
               """, 0)
    ret = []
    if result is not None:
        for lemma in result:
            ret.append(Article(lemma[0], lemma[1]))
        return ret
    else:
        pass  # тут будет фонетический поиск и всякое такое
    return None
