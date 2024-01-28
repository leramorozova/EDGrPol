from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views import View
from django.views.generic import TemplateView

from .models import Article
from .forms import SearchForm
from .SearchUtilities.lemma_search import lemma_search, cit_search, source_search, date_search


class Alphabet(View):
    def get(self, request):
        letter = request.GET['letter']
        response = Article.objects.filter(lemma_rus__startswith=letter).order_by('lemma_rus')
        return render(request, 'alphabet.html', {"response": response})


class WordEntry(View):
    def get(self, request, pk):
        data = Article.objects.get(id=pk)
        return render(request, 'article.html', {'data': data})


class Search(View):
    REQUEST_TYPES = {
        "lemma": lemma_search,
        "cit": cit_search,
        "source": source_search,
        "date": date_search
    }

    def get(self, request):
        lemma = request.GET['lemma']
        search_type = request.GET['tabs']

        search_func = self.REQUEST_TYPES.get(search_type)
        if search_func is None:
            return render(request, 'failed_result.html', {"lemma": lemma})

        articles = search_func(lemma)
        page = request.GET.get('page')
        if not articles:
            return render(request, 'failed_result.html', {"lemma": lemma})
        paginator = Paginator(articles, 7)
        try:
            response = paginator.page(page)
        except PageNotAnInteger:
            response = paginator.page(1)
        except EmptyPage:
            response = paginator.page(paginator.num_pages)
        return render(request, f'{search_type}_result.html', {"lemma": lemma, "response": response})
