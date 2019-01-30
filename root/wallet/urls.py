from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^create_wallet/', views.create_wallet, name='create_wallet'),
    url(r'^get_wallet/', views.get_wallet, name='get_wallet'),
]