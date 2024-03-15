from django.urls import path
from .views import scrape_website1, scrape_website2, Home, ArticleView, ArticleFilter, ArticleWithSource, ArticleFilterByDate

urlpatterns = [
    path('scrap-site-1/',scrape_website1, name = 'scrap1'),
    path('scrap-site-2/',scrape_website2, name = 'scrap2'),

    path('',Home.as_view(), name = 'home'),
    path('article/<int:pk>/',ArticleView.as_view(), name = 'article'),
    path('article/filter/',ArticleFilter.as_view(), name = 'article_filter'),
    path('article/filter/date/<str:parameter>/',ArticleFilterByDate.as_view(), name = 'article_filter_date'),
    path('article/source/<str:article_source>/',ArticleWithSource.as_view(), name = 'article_source'),

]