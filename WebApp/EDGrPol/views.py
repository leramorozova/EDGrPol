from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import SearchForm
from .SearchUtilities.lemma_search import full_lemma_search, alphabet_search, cit_search, source_search, date_search, \
    get_full_article


def index(request):
    form = SearchForm()
    return render(request, 'EDGrPol/index.html', {'form': form})


def annotation(request):
    return render(request, 'EDGrPol/annotation.html', {})


def materials(request):
    return render(request, 'EDGrPol/materials.html', {})


def team(request):
    return render(request, 'EDGrPol/team.html', {})


def alphabet(request):
    letter = request.GET['letter']
    response = alphabet_search(letter)
    return render(request, 'EDGrPol/alphabet.html', {"response": response})


def search_result(request):
    lemma = request.GET['lemma']
    search_type = request.GET['tabs']
    if search_type == "lemma":
        articles = full_lemma_search(lemma)
        page = request.GET.get('page')
        if articles is None:
            return render(request, 'EDGrPol/failed_result.html', {"lemma": lemma})
        paginator = Paginator(articles, 7)
        try:
            response = paginator.page(page)
        except PageNotAnInteger:
            response = paginator.page(1)
        except EmptyPage:
            response = paginator.page(paginator.num_pages)
        return render(request, 'EDGrPol/search_result.html', {"lemma": lemma, "response": response})
    elif search_type == "cit":
        articles = cit_search(lemma)
        page = request.GET.get('page')
        if articles is None:
            return render(request, 'EDGrPol/failed_result.html', {"lemma": lemma})
        paginator = Paginator(articles, 7)
        try:
            response = paginator.page(page)
        except PageNotAnInteger:
            response = paginator.page(1)
        except EmptyPage:
            response = paginator.page(paginator.num_pages)
        return render(request, 'EDGrPol/cit_result.html', {"lemma": lemma, "response": response})
    elif search_type == "source":
        articles = source_search(lemma)
        page = request.GET.get('page')
        if articles is None:
            return render(request, 'EDGrPol/failed_result.html', {"lemma": lemma})
        paginator = Paginator(articles, 7)
        try:
            response = paginator.page(page)
        except PageNotAnInteger:
            response = paginator.page(1)
        except EmptyPage:
            response = paginator.page(paginator.num_pages)
        return render(request, 'EDGrPol/source_result.html', {"lemma": lemma, "response": response})
    elif search_type == "date":
        articles = date_search(lemma)
        page = request.GET.get('page')
        if articles is None:
            return render(request, 'EDGrPol/failed_result.html', {"lemma": lemma})
        paginator = Paginator(articles, 5)
        try:
            response = paginator.page(page)
        except PageNotAnInteger:
            response = paginator.page(1)
        except EmptyPage:
            response = paginator.page(paginator.num_pages)
        return render(request, 'EDGrPol/date_result.html', {"lemma": lemma, "response": response})


def full_article(request, pk):
    data = get_full_article(pk)
    return render(request, 'EDGrPol/article.html', {'data': data})


def contacts(request):
    return render(request, 'EDGrPol/contacts.html', {})
