from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, "blog/index.html")


def article_01(request):
    return render(request, "blog/article_01.html")

