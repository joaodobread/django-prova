from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.decorators import login_required


from clients import models


class ListClientView:
    @login_required(login_url='login_page')
    def index(request: HttpRequest):
        clients = models.Client.objects.all()
        return render(request, 'clients/list-all.html', {"clients": clients})

    @login_required(login_url='login_page')
    def detail(request: HttpRequest, client_id: int):
        client = models.Client.objects.filter(id=client_id).first()
        return render(request, 'clients/details.html', {"client": client})
