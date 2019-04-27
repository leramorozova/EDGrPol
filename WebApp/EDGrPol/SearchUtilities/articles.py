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


class CitSearchView:
    def __init__(self, id, lemma, citation):
        self.id = id
        self.lemma = lemma
        self.citation = citation


class SourceSearchView:
    def __init__(self, id, lemma, source):
        self.id = id
        self.lemma = lemma
        self.source = source


class DateSearchView:
    def __init__(self, id, lemma, dates):
        self.id = id
        self.lemma = lemma
        self.dates = dates


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
        self.citation = db.get_data(db.execute("""SELECT citation FROM complex_fields WHERE lemma=%s""",
                                               (self.lemma,)), 1)
        self.add_histor = db.get_data(db.execute("""SELECT add_histor FROM complex_fields WHERE lemma=%s""",
                                                 (self.lemma,)), 1)
        self.add_philol = db.get_data(db.execute("""SELECT add_philol FROM complex_fields WHERE lemma=%s""",
                                                 (self.lemma,)), 1)
        self.orig_sources = db.get_data(db.execute("""SELECT orig_srcs FROM complex_fields WHERE lemma=%s""",
                                                   (self.lemma,)), 1)
        self.hapax = db.get_data(db.execute("""SELECT if_hapax FROM simple_fields WHERE id=%s""", (lemma_id,)), 1)
        self.mid_lang = db.get_data(db.execute("""SELECT if_middle_lang FROM simple_fields WHERE id=%s""",
                                               (lemma_id,)), 1)
        self.translated_sources = db.get_data(db.execute("""SELECT translated_srcs FROM simple_fields WHERE id=%s""",
                                                         (lemma_id,)), 1)
        self.rewrit_date = db.get_data(db.execute("""SELECT rewrit_date FROM simple_fields WHERE id=%s""",
                                                  (lemma_id,)), 1)
        self.orig_creation = db.get_data(db.execute("""SELECT orig_creation FROM simple_fields WHERE id=%s""",
                                                    (lemma_id,)), 1)
        self.phon_variants = db.execute("""SELECT variant FROM variants WHERE lemma=%s AND var_type=%s""",
                                        (self.lemma, "phon",))
        if len(self.phon_variants) == 0:
            self.phon_variants = None
        else:
            self.phon_variants = ', '.join([el[0] for el in self.phon_variants]).rstrip().lstrip()
        self.morph_variants = db.execute("""SELECT variant FROM variants WHERE lemma=%s AND var_type=%s""",
                                        (self.lemma, "morph",))
        if len(self.morph_variants) == 0:
            self.morph_variants = None
        else:
            self.morph_variants = ', '.join([el[0] for el in self.morph_variants]).rstrip().lstrip()


