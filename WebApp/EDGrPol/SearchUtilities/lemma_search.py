"""
Реализация поиска по лемме
"""

import re

from ..models import Article


def full_lemma_search(request):
    """
    Search by lemma in title lemmas, morph and phonetic variants
    :param request: form arguments
    :return: array of result lemmas
    """
    return Article.objects.filter(lemma_rus__contains=request)


def alphabet_search(request):
    return Article.objects.filter(lemma_rus__startswith=request).order_by('lemma_rus')


def cit_search(request):
    result = Article.objects.filter(citation__contains=request)
    for article in result:
        # highlight matching places in citation
        if len(article.citation) > 400:
            article.citation = article.citation[:400] + " <...>"
        article.citation = re.sub(request, "<mark><b>" + request + "</b></mark>", article.citation)
    return result


def source_search(request):
    result = Article.objects.filter(translated_srcs__contains=request) | \
             Article.objects.filter(historic_sources__contains=request) | \
             Article.objects.filter(slavic_sources__contains=request) | \
             Article.objects.filter(orig_srcs__contains=request)
    for article in result:
        # highlight matching places in citation
        article.translated_srcs = re.sub(request, "<mark><b>" + request + "</b></mark>", article.translated_srcs)
        article.historic_sources = re.sub(request, "<mark><b>" + request + "</b></mark>", article.historic_sources)
        article.slavic_sources = re.sub(request, "<mark><b>" + request + "</b></mark>", article.slavic_sources)
        article.orig_srcs = re.sub(request, "<mark><b>" + request + "</b></mark>", article.orig_srcs)
    return result


def date_search(request):
    result = Article.objects.filter(translated_srcs__contains=request) | \
             Article.objects.filter(rewrit_date__contains=request) | \
             Article.objects.filter(orig_creation__contains=request) | \
             Article.objects.filter(orig_srcs__contains=request) | \
             Article.objects.filter(citation__contains=request)
    for article in result:
        # highlight matching places in citation
        article.translated_srcs = re.sub(request, "<mark><b>" + request + "</b></mark>", article.translated_srcs)
        article.rewrit_date = re.sub(request, "<mark><b>" + request + "</b></mark>", article.rewrit_date)
        article.orig_creation = re.sub(request, "<mark><b>" + request + "</b></mark>", article.orig_creation)
        article.orig_srcs = re.sub(request, "<mark><b>" + request + "</b></mark>", article.orig_srcs)
        if len(article.citation) > 150:
            article.citation = article.citation[:400] + " <...>"
        article.citation = re.sub(request, "<mark><b>" + request + "</b></mark>", article.citation)
    return result


def get_full_article(request):
    return Article.objects.get(id=request)
