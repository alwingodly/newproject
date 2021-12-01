from django.contrib import admin

# Register your models here.
from.models import prod,cat

class catad(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(cat,catad)

class prodad(admin.ModelAdmin):
    list_display = ['name','slug','price','availability','stock','created','update']
    list_editable = ['price','stock','availability']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(prod,prodad)
