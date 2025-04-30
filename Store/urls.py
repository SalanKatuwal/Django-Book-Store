from django.urls import path
from . import views
urlpatterns = [
    path('', views.home,name='home'),
    path('add/',views.add,name='add'),
    path('display/',views.display,name='display'),
    path('details/<slug:name>/',views.details, name='details'),
    path('delete/<slug:name>/',views.delete, name='delete'),
    path('edit/<slug:name>/',views.edit, name='edit'),
]
