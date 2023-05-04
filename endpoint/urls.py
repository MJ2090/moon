from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views

urlpatterns = [
    path('test_async/', views.test_async, name='test_async'),
]

urlpatterns += staticfiles_urlpatterns()