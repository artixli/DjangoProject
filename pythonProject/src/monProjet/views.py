from django.shortcuts import render
from datetime import datetime


def index(request):
    date = datetime.today()
    return render(request, "monProjet/index.html", context={"date": date})
