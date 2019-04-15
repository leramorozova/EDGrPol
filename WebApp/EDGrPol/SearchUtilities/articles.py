"""
    Объекты словарных статей
"""


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


class FullTextArticle(ResponseView):
    def __init__(self):
        pass
