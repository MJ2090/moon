from django.http import HttpResponse
from django.shortcuts import render
import json
from django.conf import settings

# Create your views here.

print("in the view!!")
x=0

def test_async(request):
    if request.method == 'POST':
        ai_message = settings.LLAMA.evaluate()
        return HttpResponse(json.dumps({'ai_message': ai_message}))
    else:
        ret = {}
        return render(request, 'endpoint/main.html', ret)