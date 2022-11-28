from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.db import transaction

from clients.forms import create_client
from clients.models import Client


class EditClientView:
    def edit(request: HttpRequest, client_id: int):
        client = Client.objects.filter(id=client_id).first()
        if not client:
            return redirect('all_client')
        return render(request, 'clients/form.html', {"client": client})

    def update(request: HttpRequest, client_id: int):
        with transaction.atomic():
            client = Client.objects.select_for_update().filter(id=client_id).first()

            if request.method.lower() != 'post' or not client:
                return redirect('all_client')
            form = create_client.CreateClientForm(
                request.POST, instance=client)
            form.full_clean()
            form.save()
            return redirect('all_client')
