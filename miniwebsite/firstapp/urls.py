from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('about/', about),
    path('contactus/', about),
    path('category/<int:category_id>', get_category)


]
