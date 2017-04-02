from django.http import JsonResponse
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
import json

from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

@csrf_exempt
def authCheck(request):
    credentials = json.loads(request.body)
    user = authenticate(username=credentials['username'], password=credentials['password'])
    token = Token.objects.create()
    if user is not None:
        return JsonResponse({"success":"1","id_token":token})
    else:
        return JsonResponse({"success":"0"})


