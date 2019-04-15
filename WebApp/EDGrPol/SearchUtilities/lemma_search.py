"""
Реализация поиска по лемме
"""

from .db_utils import Database
from .articles import ResponseView


def full_lemma_search(request):
    """
    Search by lemma in title lemmas, morph and phonetic variants
    :param request: form arguments
    :return: array of result lemmas
    """
    db = Database()
    result = db.execute("""SELECT id, lemma_rus, lemma_greek, lang FROM simple_fields
                            WHERE lemma_rus LIKE '%""" + request + """%'
               """, 0)
    ret = []
    if len(result) != 0:
        for lemma in result:
            semantics = db.execute("""SELECT semantics FROM complex_fields
                                        WHERE lemma=%s
                                        """, (lemma[1],))
            if len(semantics) != 0:
                semantics = semantics[0][0]
            else:
                semantics = ''
            ret.append(ResponseView(lemma[0], lemma[1], lemma[2], semantics, lemma[3]))
        db.close()
        return ret
    else:
        db.close()
        pass  # тут будет фонетический поиск и всякое такое
    return None
