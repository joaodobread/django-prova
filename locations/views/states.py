from django.http import JsonResponse, HttpResponseNotFound
from django.forms.models import model_to_dict


from locations import models


class StatesView:
    def list_all(request):
        states = models.StateModel.objects.all()
        return JsonResponse({"data": list(map(model_to_dict, states))})

    def list_one(request, id):
        state = models.StateModel.objects.filter(
            id=id).first()
        if not state:
            return HttpResponseNotFound(content='state_not_found')
        cities = list(map(model_to_dict, state.cities()))
        return JsonResponse({"data": {**model_to_dict(state), "cities": cities}})
