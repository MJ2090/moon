from django.http import HttpResponse
from django.shortcuts import render
import json
from django.shortcuts import render

# Create your views here.

def test_async(request):
    ai_message = "sssss"
    ret = {}

    # return HttpResponse(json.dumps({'ai_message': ai_message}))
    return render(request, 'endpoint/main.html', ret)
