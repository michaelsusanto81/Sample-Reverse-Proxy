from django.http import JsonResponse

def hello(request):
    return JsonResponse({'response': 'Hello World from Django'}, status=200)