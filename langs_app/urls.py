from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('word/add/', views.add_word_page, name='add_word_page'),
    path('voice/add/', views.add_voice_page, name='add_voice_page'),
    path('full/data/add/', views.add_full_data_page, name='add_full_data_page'),
    path('class/<slug:slug>/', views.full_data_page, name='full_data_page'),
    path('class/<slug:slug>/<int:pk>/', views.full_data_detail_page, name='full_data_detail_page'),
]