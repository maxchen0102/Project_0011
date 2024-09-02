from django.http import JsonResponse
from django.shortcuts import render
import json
# Create your views here.
from django.shortcuts import render


def home_view(request):
    context = {
        'title': 'My First Django Template',
        'name': 'World'
    }
    return render(request, 'home.html', context)


def data_text(request):
    data = {
        'name': "John",
        'age': 30,
        'city': "New York",
        'enable': True
    }
    print("original:", type(data))
    # convert data to json
    print("data:", data)
    print("===cover dict to json===:")
    json_data = json.dumps(data)

    print("json_data:", type(json_data))
    print("json_data:", json_data)
    return JsonResponse(data)


def some_view(request):
    permissions = {'can_edit': True, 'can_delete': False}
    json_permissions = json.dumps(permissions)
    print(json_permissions)
    print(type(json_permissions))
    return render(request, 'template.html', {'permissions': permissions, 'json_permissions': json_permissions})
