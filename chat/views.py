from django.shortcuts import render
from django.http import JsonResponse
import json
from .agent import run_agent # Import our agent

def chat_view(request):
    return render(request, 'chat/index.html')

def ask_agent(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        query = data.get('query')
        if query:
            response = run_agent(query)
            return JsonResponse({'response': response})
        return JsonResponse({'error': 'No query provided'}, status=400)
    return JsonResponse({'error': 'Invalid request method'}, status=405)