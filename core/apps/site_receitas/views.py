from django.shortcuts import render


def index(request):
    return render(request, "../templates/index.html")


def receita(request):
    return render(request, "../templates/receita.html")
