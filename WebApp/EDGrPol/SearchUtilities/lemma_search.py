"""
Реализация поиска по лемме
"""

from .db_utils import Database
from .articles import ResponseView, CitSearchView, SourceSearchView, DateSearchView
import re


def full_lemma_search(request):
    """
    Search by lemma in title lemmas, morph and phonetic variants
    :param request: form arguments
    :return: array of result lemmas
    """
    db = Database()
    result = db.execute("""SELECT id, lemma_rus, lemma_greek, lang FROM simple_fields
                            WHERE lemma_rus LIKE '%""" + request + """%'
                            ORDER BY lemma_rus""", 0)
    if len(result) == 0:
        req = db.get_data(db.execute("""SELECT lemma FROM variants
                            WHERE variant LIKE '%""" + request + """%'
                            ORDER BY lemma""", 0), 1)
        if req is not None:
            result = db.execute("""SELECT id, lemma_rus, lemma_greek, lang FROM simple_fields
                            WHERE lemma_rus LIKE '%""" + req + """%'
                            ORDER BY lemma_rus""", 0)
        else:
            return None
    ret = []
    for lemma in result:
        semantics = db.execute("""SELECT semantics FROM complex_fields
                                    WHERE lemma=%s
                                    ORDER BY lemma""", (lemma[1],))
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
                           ORDER BY lemma_rus
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


def cit_search(request):
    db = Database()
    obj_ret = []
    result = db.execute("""SELECT id, lemma_rus, citation FROM simple_fields
                        LEFT JOIN complex_fields WHERE lemma_rus = lemma AND
                        citation LIKE '%""" + request + """%'
                        ORDER BY lemma_rus
                        """, 0)
    db.close()
    if len(result) == 0:
        return None
    for el in result:
        citation = el[2]
        citation = re.sub(request, "<mark><b>" + request + "</b></mark>", citation)
        obj_ret.append(CitSearchView(el[0], el[1], citation))
    return obj_ret


def source_search(request):
    db = Database()
    obj_ret = []
    result = db.execute("""SELECT id, lemma_rus, source FROM simple_fields
                        LEFT JOIN sources WHERE lemma_rus = lemma AND
                        source LIKE '%""" + request + """%'
                        ORDER BY lemma_rus
                        """, 0)
    db.close()
    if len(result) == 0:
        return None
    for el in result:
        obj_ret.append(SourceSearchView(el[0], el[1], el[2]))
    return obj_ret


def date_search(request):
    db = Database()
    obj_ret = []
    result = db.execute("""SELECT id, lemma, citation, translated_srcs, rewrit_date, orig_creation, orig_srcs
                        FROM simple_fields
                        LEFT JOIN complex_fields WHERE lemma_rus = lemma
                        AND translated_srcs REGEXP '""" + request + """( в\.)?$' OR
                        rewrit_date REGEXP '""" + request + """( в\.)?$'
                        OR orig_creation REGEXP '""" + request + """( в\.)?$'
                        OR orig_srcs REGEXP '""" + request + """( в\.)?$'
                        OR citation REGEXP '""" + request + """( в\.)?$'""", 0)
    db.close()
    if len(result) == 0:
        return None
    for el in result:
        citation = el[6]
        if len(citation) > 150:
            citation = citation[:150] + " <...>"
        obj_ret.append(DateSearchView(el[0], el[1], ' '.join([citation, el[2], el[3], el[4], el[5]])))
    return obj_ret
