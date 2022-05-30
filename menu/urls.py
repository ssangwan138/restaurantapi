from django.urls import path
from .views import viewMenu, searchMenu, addMenuItem

urlpatterns = [
    path('', viewMenu.as_view()),
    path('addItem/', addMenuItem.as_view()),
    path('search/<str:name>/', searchMenu.as_view()),
]