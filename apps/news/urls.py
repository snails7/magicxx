from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('news/',views.index, name='index'),
path('<int:news_id>/',views.news_detail,name='news_detail'),
]