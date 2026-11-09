from django.urls import path

from . import views

urlpatterns = [
    path('pixelman/', views.webhook, name='webhook'),
]
