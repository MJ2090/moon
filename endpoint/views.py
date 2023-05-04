from django.http import HttpResponse
from django.shortcuts import render
import json

# Create your views here.

def test_async(request):
    ai_message = "sssss"

    return HttpResponse(json.dumps({'ai_message': ai_message}))
