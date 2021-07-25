#from django.http import HttpResponse
from .models import partitions, authors
#from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

@login_required(login_url='/accounts/login/')
def partitions_view(request):
    partitions_list = partitions.objects.all()
    #template = loader.get_template('partitions.j2')
    context = {
       'partitions' : partitions_list, 
    }
#   return HttpResponse(template.render(context, request))
    return render(request, 'partitions.j2', context)

@login_required(login_url='/accounts/login/')
def partition_view(request, partition_id):
    partition = get_object_or_404(partitions, pk=partition_id)
    if not partition.ref:
        partition.ref = ''
    context = {
        'title' : partition.title,
        'author' : partition.authors.name,
        'ref' : partition.ref,
        'partition_files' : partition.partition_files.all
    }
    return render(request, 'partition_detail.j2', context)
