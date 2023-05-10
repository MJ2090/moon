from django.http import HttpResponse
from django.shortcuts import render
import json
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def llama_async(request):
    if request.method == 'POST':
        prompt_template = """Below is an instruction that describes a task, paired with an input that provides further context. Write a response that appropriately completes the request.

### Instruction:
Below is a dialogue between a patient and a therapist. Write one reply as if you were the therapist.

### Input:"""
        print("POST messages : ", request.POST['messages'])
        prompt = prompt_template
        messages = json.loads(request.POST['messages'])
        for item in messages:
            if item['role'] == 'user':
                prompt += f"""\nPatient: {item['content']}"""
            if item['role'] == 'assistant':
                if 'Therapist: ' in item['content']:
                    prompt += f"""\n{item['content']}"""
                else:
                    prompt += f"""\nTherapist: {item['content']}"""
        prompt += """\n\n### Response:\n"""
        print(f"Prompt =============================\n{prompt}\n=============================")
        ai_message = settings.LLAMA.evaluate(prompt = prompt)
        print(f"Output =============================\n{ai_message}\n=============================")
        splitted = ai_message.split("### Response:\n")
        if len(splitted)>1:
            ans = splitted[1]
        else:
            ans = splitted[0]
        ans = ans.replace('Therapist: ', '')
        return HttpResponse(json.dumps({'ai_message': ans}))
    else:
        ret = {}
        return render(request, 'endpoint/main.html', ret)
    

@csrf_exempt
def glm_async(request):
    if request.method == 'POST':
        messages = json.loads(request.POST['messages'])
        print("POST messages : ", messages)
        ai_message = settings.LLAMA.evaluate(prompt = prompt)
    else:
        ret = {}
        return render(request, 'endpoint/main.html', ret)
    

@csrf_exempt
def test(request):
    prompt_template = """Below is an instruction that describes a task, paired with an input that provides further context. Write a response that appropriately completes the request.

### Instruction:
Below is a dialogue between a patient and a therapist. Write one reply as if you were the therapist.

### Input:
Patient: I'm so sad today

### Response:
"""
    print("In TEST")
    print(f"Prompt =============================\n{prompt_template}\n=============================")
    ai_message = settings.LLAMA.evaluate(prompt = prompt_template)
    print(f"Output =============================\n{ai_message}\n=============================")
    splitted = ai_message.split("### Response:\n")
    if len(splitted)>1:
        ans = splitted[1]
    else:
        ans = splitted[0]
    ans = ans.replace('Therapist: ', '')
    return HttpResponse(json.dumps({'ai_message': ans, 'prompt': prompt_template}))