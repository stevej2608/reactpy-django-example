from django.shortcuts import render


def router(request, path=None):
    return render(request, "index.html", {})
