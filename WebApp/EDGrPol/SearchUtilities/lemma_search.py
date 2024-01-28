"""
Реализация поиска по лемме
"""

import re

from ..models import Article


class SearchResultFormatter:
    _MARK = "<mark><b>%s</b></mark>"
    _LONG_TEXT_LIMIT = 400
    _SHORT_TEXT_LIMIT = 150
    _EOS = " <...>"

    def cut_long_text(self, text):
        if len(text) > self._LONG_TEXT_LIMIT:
            return text[:self._LONG_TEXT_LIMIT] + " <...>"
        return text

    def cut_short_text(self, text):
        if len(text) > self._SHORT_TEXT_LIMIT:
            return text[:self._SHORT_TEXT_LIMIT] + " <...>"
        return text

    def put_mark(self, text, marked_text):
        return re.sub(marked_text, self._MARK % marked_text, text)


def lemma_search(request):
    """
    Search by lemma in title lemmas, morph and phonetic variants
    :param request: form arguments
    :return: array of result lemmas
    """
    return Article.objects.filter(lemma_rus__contains=request)


def cit_search(request):
    formatter = SearchResultFormatter()
    result = Article.objects.filter(citation__contains=request)
    for article in result:
        # highlight matching places in citation
        article.citation = formatter.cut_long_text(article.citation)
        article.citation = formatter.put_mark(article.citation, request)
    return result


def source_search(request):
    formatter = SearchResultFormatter()
    result = Article.objects.filter(translated_srcs__contains=request) | \
             Article.objects.filter(historic_sources__contains=request) | \
             Article.objects.filter(slavic_sources__contains=request) | \
             Article.objects.filter(orig_srcs__contains=request)
    for article in result:
        # highlight matching places in citation
        article.translated_srcs = formatter.put_mark(article.translated_srcs, request)
        article.historic_sources = formatter.put_mark(article.historic_sources, request)
        article.slavic_sources = formatter.put_mark(article.slavic_sources, request)
        article.orig_srcs = formatter.put_mark(article.orig_srcs, request)
    return result


def date_search(request):
    formatter = SearchResultFormatter()
    result = Article.objects.filter(translated_srcs__contains=request) | \
             Article.objects.filter(rewrit_date__contains=request) | \
             Article.objects.filter(orig_creation__contains=request) | \
             Article.objects.filter(orig_srcs__contains=request) | \
             Article.objects.filter(citation__contains=request)
    for article in result:
        # highlight matching places in citation
        article.citation = formatter.cut_long_text(article.citation)
        article.citation = formatter.put_mark(article.citation, request)
        article.translated_srcs = formatter.put_mark(article.translated_srcs, request)
        article.rewrit_date = formatter.put_mark(article.rewrit_date, request)
        article.orig_creation = formatter.put_mark(article.orig_creation, request)
        article.orig_srcs = formatter.put_mark(article.orig_srcs, request)
    return result
