# Register your models here.

from django.contrib import admin

from .models import partitions, authors, types, partition_file

class partitionsAdmin(admin.ModelAdmin):
    fields = ('title','authors','ref', 'types', 'partition_files')
    list_display = ('title','authors','ref', )


class authorsAdmin(admin.ModelAdmin):
    fields = ('name',)
    list_display = ('name',)

class typesAdmin(admin.ModelAdmin):
    fields = ('type',)

class partition_fileAdmin(admin.ModelAdmin):
    fields = ('partition_file',)


admin.site.register(partitions, partitionsAdmin)
admin.site.register(authors, authorsAdmin)
admin.site.register(types, typesAdmin)
admin.site.register(partition_file, partition_fileAdmin)
