from django.contrib import admin

# Register your models here.

from django.contrib import admin

from .models import partitions, authors

class partitionsAdmin(admin.ModelAdmin):
    fields = ('title','authors','ref')
    list_display = ('title', 'author_name', 'ref' )

    def author_name(self, obj):
        return obj.authors.name

class authorsAdmin(admin.ModelAdmin):
    fields = ('name',)
    list_display = ('name',)


admin.site.register(partitions, partitionsAdmin)
admin.site.register(authors, authorsAdmin)
