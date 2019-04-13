from django.shortcuts import render
from .forms import SearchForm
from .SearchUtilities.lemma_search import full_lemma_search


def index(request):
    form = SearchForm()
    return render(request, 'EDGrPol/index.html', {'form': form})


def search_result(request):
    lemma = request.GET['lemma']
    response = full_lemma_search(lemma)
    if len(response) == 0:
        return render(request, 'EDGrPol/failed_result.html', {"lemma": lemma})
    return render(request, 'EDGrPol/search_result.html', {"lemma": lemma, "response": response})
