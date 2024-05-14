from django.shortcuts import render
from .models import Login
from .forms import LoginForm

# Create your views here.

def index(request):
    x = {'name': 'ali', 'age': 24}
    return render(request, 'pages/index.html', x)

def about(request):
    if request.method == 'POST':
        dataform = LoginForm(request.POST )
        if dataform.is_valid():
            dataform.save()
    
    return render(request, 'pages/about.html', {'LF' : LoginForm})
     
     
    