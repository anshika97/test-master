from django.urls import path

from . import views

app_name='movie'

urlpatterns = [
    path('', views.index, name='index'),
    path('movie/new', views.new_movie, name='new_movie'),
    path('movie/<int:movie_id>/', views.movie_detail, name='movie_detail'),
    path('movie/<int:movie_id>/<staff_type>', views.edit_movie_staff, name='add_movie_staff'),
]