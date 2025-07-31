from django.shortcuts import redirect

def home(request):
    return redirect('http://127.0.0.1:8000/api/v1')