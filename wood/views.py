from django.shortcuts import render
from django.urls import resolve
from .models import Wood, WoodMenu


def woodmenu_view(request):
    main_menu = WoodMenu.objects.filter(parent__isnull=True)
    context = {
        'main_menu': main_menu
    }
    return render(request, 'home.html', context)

def wood_view(request, slug):
    woods = Wood.objects.filter(menu__slug=slug)
    children_menu = WoodMenu.objects.filter(parent__slug=slug)
    return render(request, 'woods.html', {'woods': woods, 'children_menu': children_menu})