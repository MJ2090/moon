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
        prompt_template = """
        Below is aninstruction that describes a task, paired with an input that provides further context. Write a response that appropriately completes the request.

### Instruction:
"""

        print("request.POST = ", request.POST)
        prompt = prompt_template
        messages = json.loads(request.POST['messages'])
        for item in messages:
            if item['role'] == 'user':
                prompt += f"""
Patient: {item['content']}"""
            if item['role'] == 'Assistant':
                prompt += f"""
Therapist: {item['content']}"""
        prompt += """

### Response:

"""
        ai_message = settings.LLAMA.evaluate(prompt = prompt)
        splitted = ai_message.split("### Response:")
        if len(splitted)>1:
            ans = splitted[1]
        else:
            ans = splitted[0]
        return HttpResponse(json.dumps({'ai_message': ans}))
    else:
        ret = {}
        return render(request, 'endpoint/main.html', ret)