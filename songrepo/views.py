from django.http import HttpResponse
from .models import partitions, authors, types, playlist
#from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
import json

def index(request):
    return render(request, 'index.j2')

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
        'partition_files' : partition.partition_files.all,
        'types' : partition.types.all
    }
    return render(request, 'partition_detail.j2', context)

@login_required(login_url='/accounts/login/')
def partitions_type_search(request, type_name):
    type_object = types.objects.filter(type=type_name)
    partitions_list = partitions.objects.filter(types__in=type_object)
    context = {
       'partitions' : partitions_list,
    }
    return render(request, 'partitions.j2', context)

@login_required(login_url='/accounts/login/')
def search(request):
    search_type = request.GET.get('search_type') 
    search_content = request.GET.get('search_content')
    if  search_type == 'type':
        type_object = types.objects.filter(type=search_content)
        partitions_list = partitions.objects.filter(types__in=type_object)
    elif search_type == 'author':
        author_object = authors.objects.filter(name=search_content)
        partitions_list = partitions.objects.filter(authors__in=author_object)
    context = {
       'partitions' : partitions_list,
    }
    return render(request, 'partitions.j2', context)

@login_required(login_url='/accounts/login/')
def ajax_search(request):
    if request.is_ajax():
        query=request.GET.get('term')
        search_type = request.GET.get('search_type')
        queryset=None 
        result=[]
        if search_type == 'type':
            queryset = list(types.objects.filter(type__icontains=query))
            for obj in queryset:
                result.append(obj.type)
        elif search_type == 'author':
            queryset = list(authors.objects.filter(name__icontains=query))
            for obj in queryset:
                result.append(obj.name)
        dump=json.dumps(result)
    else: 
        data='fail'
    mimetype='application/json'
    return HttpResponse(dump,mimetype)

@login_required(login_url='/accounts/login/')
def playlists(request):
    playlists = playlist.objects.all
    context = {
        'playlists' : playlists
    }
    return render(request,'playlists.j2', context)


@login_required(login_url='/accounts/login/')
def playlist_detail(request, playlist_id):
    playlist_object = get_object_or_404(playlist, pk=playlist_id)
    partition_list = []
    for partition in playlist_object.partition_list.all():
        file_list=[]
        for file_object in partition.partition_files.all():
            file_list.append(file_object)
        partition_list.append(file_list)
            
    context = {
        'partition_list' : partition_list
    }
    return render(request, 'playlist.j2', context)
