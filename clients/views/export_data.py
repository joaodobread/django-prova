import json
from django.http import HttpRequest, HttpResponse


def export(request: HttpRequest):
    if not request.POST:
        return
    file_names = []
    if request.FILES.items():
        for filename, _ in request.FILES.items():
            file_names.append(request.FILES[filename].name)
    data_export = {
        **request.POST.dict(),
        "images": file_names
    }
    if data_export.get('csrfmiddlewaretoken'):
        del data_export['csrfmiddlewaretoken']
    response = HttpResponse(json.dumps(data_export, indent=2, ensure_ascii=False).encode('utf-8'),
                            content_type='application/json')
    response['Content-Disposition'] = 'attachment; filename=export.json'
    return response
