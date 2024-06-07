from django.shortcuts import render
from .models import Main


def index(request):
    main = Main.objects.all()
    return render(request, 'main/index.html',
                  {'main': main})
