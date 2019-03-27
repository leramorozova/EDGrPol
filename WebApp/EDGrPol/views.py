from django.shortcuts import render


def index(request):
    return render(request, 'EDGrPol/index.html', {})
