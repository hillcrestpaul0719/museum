from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator

from .models import Exhibit, Object

# Create your views here.

def index(request):
    exhibits = Exhibit.objects.all()
    return render(request, 'museum/index.html', {'exhibits': exhibits})

def exhibit(request, pk):
    exhibit = Exhibit.objects.get(pk=pk)
    return render(request, 'museum/exhibit.html', {'exhibit': exhibit})

def object(request, exhibit_pk, obj_num):
    # object = Object.objects.get(pk=pk)
    # prevObj = Object.objects.filter(exhibit=object.exhibit, pk__lt=pk).order_by('-pk')
    # nextObj = Object.objects.filter(exhibit=object.exhibit, pk__gt=pk).order_by('pk')
    # if len(prevObj) == 0:
    #     prevObj = None
    # else:
    #     prevObj = prevObj[0]
    # if len(nextObj) == 0:
    #     nextObj = None
    # else:
    #     nextObj = nextObj[0]
    # return render(request, 'museum/object.html', {'object': object, 'prevObj': prevObj, 'nextObj': nextObj})

    objects = Object.objects.filter(exhibit__pk=exhibit_pk)
    paginator = Paginator(objects, 1) # Show 25 contacts per page
    object = paginator.get_page(obj_num)
    return render(request, 'museum/object.html', {'object': object})
