from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.


# index view
def index(request):
    return render(request, "dashboard/index.html")