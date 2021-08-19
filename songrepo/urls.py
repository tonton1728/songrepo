from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('partitions', views.partitions_view, name="partitions_list"),
#    path('partitions/type/<str:type_name>', views.partitions_type_search),
    path('partitions/search', views.search, name="partitions_search"),
    path('partition/<int:partition_id>', views.partition_view, name="partition_detail"),
    path('ajax/search', views.ajax_search),
    path('playlists', views.playlists),
    path('playlist/<int:playlist_id>', views.playlist_detail, name='playlist_detail'),
    ]
