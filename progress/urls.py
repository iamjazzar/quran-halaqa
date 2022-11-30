
from django.urls import path

from progress.views import my_view, profile_view, record_view


urlpatterns = [
    path('', my_view, name='index'),
    path('profile', profile_view, name='profile'),
    path('record', record_view, name='record'),
]
