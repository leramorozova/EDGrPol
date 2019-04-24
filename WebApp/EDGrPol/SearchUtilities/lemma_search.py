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
    if len(result) == 0:
        req = db.get_data(db.execute("""SELECT lemma FROM variants
                            WHERE variant LIKE '%""" + request + """%'
                            """, 0), 1)
        if req is not None:
            result = db.execute("""SELECT id, lemma_rus, lemma_greek, lang FROM simple_fields
                            WHERE lemma_rus LIKE '%""" + req + """%'
                            """, 0)
        else:
            return None
    ret = []
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


def alphabet_search(request):
    db = Database()
    obj_ret = []
    result = db.execute("""SELECT id, lemma_rus FROM simple_fields
                               WHERE lemma_rus LIKE '""" + request + """%'
                               """, 0)
    db.close()
    i = 1
    for el in result:
        if i % 25 == 0:
            obj_ret.append(ResponseView(el[0], el[1], None, None, None))
        else:
            obj_ret.append(ResponseView(el[0], el[1], "a", "a", "a"))
        i += 1
    if len(obj_ret) == 0:
        return None
    return obj_ret
