from django.shortcuts import render
from django.http import HttpRequest
from django.contrib.auth.decorators import login_required


from clients import models


class ListClientView:
    @login_required(login_url='login_page')
    def index(request: HttpRequest):
        clients = models.Client.objects.all()
        return render(request, 'clients/list-all.html', {"clients": clients})
