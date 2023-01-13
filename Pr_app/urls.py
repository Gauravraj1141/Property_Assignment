from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.All_Property, name="home"),
    path('Update/<int:id>/', views.Update_Property, name="Update"),
    path('Fetch_by_city', views.Fetch_Property, name="Fetch_by_city"),
    path('Find_city', views.Find_cities, name="Find_city"),
    path('Find_similiar', views.Find_similiar_pr, name="Find_similiar"),
]
