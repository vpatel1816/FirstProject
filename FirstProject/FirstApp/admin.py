from django.contrib import admin
from . models import Info

# Register your models here.
class Infoo(admin.ModelAdmin):
	list_display = ('Name','Eid')

admin.site.register(Info, Infoo)