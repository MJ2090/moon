from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views

urlpatterns = [
    path('test_async/', views.test_async, name='test_async'),
    path('test/', views.test, name='test'),
]

urlpatterns += staticfiles_urlpatterns()