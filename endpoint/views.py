from django.http import HttpResponse
from django.shortcuts import render
import json
from django.conf import settings

# Create your views here.

def test_async(request):
    if request.method == 'POST':
        ai_message = settings.MESSAGE
        return HttpResponse(json.dumps({'ai_message': ai_message}))
    else:
        ret = {}
        return render(request, 'endpoint/main.html', ret)