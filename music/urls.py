from django.urls import path
from . import views

app_name = 'music'
urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login_user/', views.login_user, name='login_user'),
    path('logout_user/', views.logout_user, name='logout_user'),
    # /music/71/
    path('<int:album_id>/', views.detail, name='detail'),
    # /music/<int:song_id>/favorite
    path('<int:song_id>/favorite/', views.favorite, name='favorite'),
    path('songs/all/', views.songs, name='songs'),
    # /music/album/add/
    path('album/add/', views.create_album, name='create_album'),
    # /music/<album_id>/create_song/
    path('<int:album_id>/create_song/', views.create_song, name='create_song'),
    # /music/<int:album_id>/delete_song/<int:song_id>/
    path('<int:album_id>/delete_song/<int:song_id>/', views.delete_song, name='delete_song'),
    # /music/album/2/delete/
    path('album/<int:pk>/delete/', views.delete_album, name='delete_album'),
    path('album/<int:album_id>/favorite_album/', views.favorite_album, name='favorite_album'),
]
