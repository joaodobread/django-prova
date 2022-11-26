from django.urls import path
from clients.views import create_client
from clients.views import list_client

urlpatterns = [
    path('', list_client.ListClientView.index, name='all_client'),
    path('create/', create_client.CreateClientView.create, name='create_client'),
    path('save/', create_client.CreateClientView.save, name='save_client'),
]
