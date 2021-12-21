from django.urls import path,include
# from watchlist_app.api import views
from watchlist_app.api.views import MovieListAV,MovieDetailAV

urlpatterns = [
    path('list/',MovieListAV.as_view(),name='movie-list'),
    path('<int:pk>/',MovieDetailAV.as_view(),name='movie-details'),
    
]



