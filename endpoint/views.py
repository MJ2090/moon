from django.http import HttpResponse
from django.shortcuts import render
import json
from django.shortcuts import render

# Create your views here.

def test_async(request):
    if request.method == 'POST':
        ai_message = "okay how are you"
        return HttpResponse(json.dumps({'ai_message': ai_message}))
    else:
        ret = {}
        return render(request, 'endpoint/main.html', ret)