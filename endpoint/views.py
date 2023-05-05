from django.http import HttpResponse
from django.shortcuts import render
import json
from django.conf import settings

# Create your views here.

print("in the view!!")
x=0

def test_async(request):
    if request.method == 'POST':
        ai_message = 'wwwww'
        prompt = """
        Below is an instruction that describes a task, paired with an input that provides further context. Write a response that appropriately completes the request.

        ### Instruction:
        Below is a dialogue between a patient and a therapist. Write one reply as if you were the therapist.

        ### Input:
        Patient: I'm sad, I lost my job

        ### Response:
        """
        ai_message = settings.LLAMA.evaluate(prompt=prompt)
        return HttpResponse(json.dumps({'ai_message': ai_message}))
    else:
        ret = {}
        return render(request, 'endpoint/main.html', ret)