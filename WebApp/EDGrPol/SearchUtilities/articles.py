"""
    Объекты словарных статей
"""

from .db_utils import Database

class ResponseView:
    def __init__(self, id, lemma, original, semantics, lang):
        self.id = id
        self.lemma = lemma
        self.original = original
        self.semantics = semantics
        if lang == "greek":
            self.lang = "греч."
        else:
            self.lang = "польск."


class FullTextArticle:
    def __init__(self, lemma_id):
        db = Database()
        self.lemma = db.get_data(db.execute("""SELECT lemma_rus FROM simple_fields WHERE id=%s""", (lemma_id,)), 0)
        self.pos = db.get_data(db.execute("""SELECT pos FROM simple_fields WHERE id=%s""", (lemma_id,)), 0)
        self.original = db.get_data(db.execute("""SELECT lemma_greek FROM simple_fields WHERE id=%s""", (lemma_id,)), 0)
        self.lang = db.get_data(db.execute("""SELECT lang FROM simple_fields WHERE id=%s""", (lemma_id,)), 0)
        self.theme = db.get_data(db.execute("""SELECT theme FROM simple_fields WHERE id=%s""", (lemma_id,)), 0)
        if self.lang == "greek":
            self.lang = "греч."
        elif self.lang == "polish":
            self.lang = "польск."
        self.semantics = db.get_data(db.execute("""SELECT semantics FROM complex_fields WHERE lemma=%s""",
                                                (self.lemma,)), 0)
        self.etymology = db.get_data(db.execute("""SELECT etymology FROM complex_fields WHERE lemma=%s""",
                                                (self.lemma,)), 1)
        self.vasmer = db.get_data(db.execute("""SELECT vasmer FROM simple_fields WHERE id=%s""", (lemma_id,)), 1)
        self.hist_sources = db.execute("""SELECT source FROM sources WHERE lemma=%s AND type=%s""",
                                       (self.lemma, "hist",))
        if len(self.hist_sources) == 0:
            self.hist_sources = None
        else:
            self.hist_sources = '; '.join([el[0] for el in self.hist_sources]).rstrip().lstrip()
        self.dict_sources = db.execute("""SELECT source FROM sources WHERE lemma=%s AND type=%s""",
                                       (self.lemma, "slavic",))
        if len(self.dict_sources) == 0:
            self.dict_sources = None
        else:
            self.dict_sources = '; '.join([el[0] for el in self.dict_sources]).rstrip().lstrip()
#!        self.orig_sources = db.get_data(db.execute("""SELECT orig_srcs FROM complex_fields WHERE lemma=%s""",
#!                                                   (self.lemma,)), 1)
        
