from django.http import HttpRequest
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


class DashboardView:
    @login_required(login_url='login_page')
    def index(request: HttpRequest):
        return render(request, 'dashboard/index.html')
