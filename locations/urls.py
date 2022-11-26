
from django.urls import path
from locations.views import states

urlpatterns = [
    path('states/', states.StatesView.list_all),
    path('states/<int:id>/', states.StatesView.list_one),
]
