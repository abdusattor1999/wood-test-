from django.urls import path
from .views import woodmenu_view, wood_view

urlpatterns = [
    path('', woodmenu_view),
    path('<str:slug>/', wood_view),
]
