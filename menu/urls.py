from django.urls import path
from .views import viewMenu, searchMenu, addMenuItem

urlpatterns = [
    path('menu/', viewMenu.as_view()),
    path('menu/addItem/', addMenuItem.as_view()),
    path('menu/search/<str:name>/', searchMenu.as_view()),
]