from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


from clients.forms import create_client


class CreateClientView:
    @login_required(login_url='login_page')
    def create(request: HttpRequest):
        form = create_client.CreateClientForm()
        return render(request, 'clients/form.html')

    @login_required(login_url='login_page')
    def save(request: HttpRequest):
        form = create_client.CreateClientForm(request.POST, request.FILES)
        form.full_clean()
        if not form.is_valid():
            return render(request, 'clients/form.html', {"form": form, })
        form.save()
        return redirect('all_client')
