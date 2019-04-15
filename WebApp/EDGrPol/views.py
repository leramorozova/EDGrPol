from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import SearchForm
from .SearchUtilities.lemma_search import full_lemma_search


def index(request):
    form = SearchForm()
    return render(request, 'EDGrPol/index.html', {'form': form})


def search_result(request):
    lemma = request.GET['lemma']
    articles = full_lemma_search(lemma)
    page = request.GET.get('page')
    if len(articles) == 0:
        return render(request, 'EDGrPol/failed_result.html', {"lemma": lemma})
    paginator = Paginator(articles, 5)
    try:
        response = paginator.page(page)
    except PageNotAnInteger:
        response = paginator.page(1)
    except EmptyPage:
        response = paginator.page(paginator.num_pages)
    return render(request, 'EDGrPol/search_result.html', {"lemma": lemma, "response": response})


def full_article(request, pk):
    print(pk)
    return render(request, 'EDGrPol/article.html', {'id': pk})
