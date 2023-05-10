from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views

urlpatterns = [
    path('llama_async/', views.llama_async, name='llama_async'),
    path('glm_async/', views.glm_async, name='glm_async'),
    path('test/', views.test, name='test'),
]

urlpatterns += staticfiles_urlpatterns()