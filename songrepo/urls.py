from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('partitions', views.partitions_view),
    path('partition/<int:partition_id>', views.partition_view),
    ]
