from django.urls import path
from . import views

app_name = 'music'
urlpatterns = [
    path('', views.IndexView.as_view(), name ='index'),
    path('register/', views.UserFormView.as_view(), name ='register'),
    # /music/71/
    path('<int:pk>/', views.DetailView.as_view(), name ='detail'),
    # /music/<int:song_id>/favorite
    path('<int:pk>/', views.favorite, name ='favorite'),
    # /music/album/add/
    path('album/add/', views.AlbumCreate.as_view(), name ='album_add'),
    # /music/<album_id>/create_song/
    path('<int:album_id>/create_song/', views.create_song, name ='create_song'),
    # /music/<int:album_id>/delete_song/<int:song_id>/
    path('<int:album_id>/delete_song/<int:song_id>/', views.delete_song, name ='delete_song'),
    # /music/album/2/
    path('album/<int:pk>/', views.AlbumUpdate.as_view(), name ='album_update'),
    # /music/album/2/delete/
    path('album/<int:pk>/delete/', views.AlbumDelete.as_view(), name ='album_delete'),
]