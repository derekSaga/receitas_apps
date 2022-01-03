from django.shortcuts import render


def index(request):
    # return render(request, '../templates/site_receitas/index.html')
    return render(request, "../templates/index.html")
