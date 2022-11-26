from django.db import models


class StateModel(models.Model):
    class Meta:
        db_table = 'states'

    name = models.CharField('state_name', 'name', null=False, max_length=200)
    code = models.CharField('state_code', 'code', null=False, max_length=200)

    def cities(self):
        cities = CityModel.objects.filter(state=self)
        self.cities = cities
        return cities


class CityModel(models.Model):
    class Meta:
        db_table = 'cities'

    name = models.CharField('city_name', 'name', null=False, max_length=200)
    state = models.ForeignKey(StateModel, models.CASCADE)
