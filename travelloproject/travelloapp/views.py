from django.shortcuts import render
from . models import destination
def index(requests):

    dests=destination.objects.all()
    return render(requests,'index.html',{'dests':dests})

# Create your views here.
