from django.urls import path
from catalogo import views

urlpatterns = [
    path('', views.index, name='index'),
    path('game/', views.GameListView.as_view(), name='games'),
    path('gamess/<int:pk>', views.GameDetailView.as_view(), name='game_detail'),
    path('usuario/',views.UsuarioListView.as_view(), name='usuarios'),
    path('usuarios/<int:pk>',views.UsuarioDetailView.as_view(), name='usuario_detail'),

    path('categoria/', views.categoria, name='categoria'),
    path('mejorjuego/', views.mjrjuego, name='mjrjuego'),
    path('retrogames/', views.retrogame, name='retro'),
    path('formulario/', views.formulario, name='formulario')    
]


urlpatterns+= [
    path('game/create/', views.GameCreate.as_view(), name='game_create'),
    path('game/<int:pk>/update/', views.GameUpdate.as_view(), name='game_update'),
    path('game/<str:pk>/delete/', views.GameDelete.as_view(), name='game_delete'),

    path('usuario/create/', views.UsuarioCreate.as_view(), name='usuario_create'),
    path('usuario/<int:pk>/update/', views.UsuarioUpdate.as_view(), name='usuario_update'),
    path('usuario/<int:pk>/delete/', views.UsuarioDelete.as_view(), name='usuario_delete')
]