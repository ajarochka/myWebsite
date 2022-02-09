from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name = 'home'),
    path('about/', about, name = 'about'),
    path('contactus/', contactus, name = 'contact'),
    path('category/<int:category_id>', get_category, name = 'category'),
    path('news/<int:news_id>', view_news, name = 'view_news')


]
