from django.http import HttpRequest
from django.shortcuts import redirect
from clients import models
import os


class DeleteClientView:
    def delete(request: HttpRequest, client_id: int):
        client = models.Client.objects.filter(id=client_id).first()
        if client:
            client.image_path.delete()
            client.delete()
        return redirect('all_client')
