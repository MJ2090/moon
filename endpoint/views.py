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
        prompt_template = """Below is aninstruction that describes a task, paired with an input that provides further context. Write a response that appropriately completes the request.

### Instruction:
Below is a dialogue between a patient and a therapist. Write one reply as if you were the therapist.

### Input:"""
        print("messages , ", request.POST['messages'])
        prompt = prompt_template
        messages = json.loads(request.POST['messages'])
        for item in messages:
            if item['role'] == 'user':
                prompt += f"""
Patient: {item['content']}"""
            if item['role'] == 'assistant':
                prompt += f"""
Therapist: {item['content']}"""
        prompt += """

### Response:
"""
        print("prompt = ", prompt)
        ai_message = settings.LLAMA.evaluate(prompt = prompt)
        print("output = ", ai_message)
        splitted = ai_message.split("### Response:")
        if len(splitted)>1:
            ans = splitted[1]
        else:
            ans = splitted[0]
        return HttpResponse(json.dumps({'ai_message': ans}))
    else:
        ret = {}
        return render(request, 'endpoint/main.html', ret)