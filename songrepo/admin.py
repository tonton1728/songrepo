# Register your models here.

from django.contrib import admin

from .models import partitions, authors, types, partition_file, playlist

class partitionsAdmin(admin.ModelAdmin):
    fields = ('title','authors','ref', 'types', 'partition_files')
    list_display = ('title','authors','ref', )
    filter_horizontal = ('partition_files','types')
    autocomplete_fields = ['authors',]


class authorsAdmin(admin.ModelAdmin):
    fields = ('name',)
    list_display = ('name',)
    search_fields = ('name',)

class typesAdmin(admin.ModelAdmin):
    fields = ('type',)

class partition_fileAdmin(admin.ModelAdmin):
    fields = ('partition_file',)

class playlistAdmin(admin.ModelAdmin):
    fields = ('name', 'partition_list')
    filter_horizontal = ('partition_list',)

admin.site.register(playlist, playlistAdmin)
admin.site.register(partitions, partitionsAdmin)
admin.site.register(authors, authorsAdmin)
admin.site.register(types, typesAdmin)
admin.site.register(partition_file, partition_fileAdmin)
