from django.db import models
from locations.models import CityModel


class Client(models.Model):
    name = models.CharField('client_name', 'name', max_length=256)
    city = models.ForeignKey(CityModel, on_delete=models.SET_NULL, null=True)
    client_type = models.CharField(
        'client_type', 'client_type', null=False, max_length=2)
    fiscal_code = models.CharField(
        'client_fiscal_code', 'fiscal_code', null=False, max_length=20, unique=True)
    state_registration = models.CharField(
        'client_state_registration', 'state_registration', null=False, max_length=20, unique=True)
    fantasy_name = models.CharField(
        'client_fantasy_name', 'fantasy_name', null=False, max_length=254)
    address = models.CharField(
        'client_address', 'address', null=False, max_length=300)
    street_number = models.CharField(
        'client_street_number', 'street_number', null=True, blank=True, max_length=20, default=0)
    neighborhood = models.CharField(
        'client_neighborhood', 'neighborhood', null=False, max_length=300)
    born_date = models.DateField('client_born_date', 'born_date', null=False)
    image_path = models.FileField(
        'client_image_path', 'image_path', null=False)
