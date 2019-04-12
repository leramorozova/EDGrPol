from django.shortcuts import render
from .forms import SearchForm
from .SearchUtilities.lemma_search import full_lemma_search


def index(request):
    if request.method == 'GET':
        form = SearchForm()
    return render(request, 'EDGrPol/index.html', {'form': form})


def search_result(request):
    response = full_lemma_search(request.GET['lemma'])
    for el in response:
        print(el)
    return render(request, 'EDGrPol/search_result.html', {})
