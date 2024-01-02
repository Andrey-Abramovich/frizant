from django.contrib import admin
from .models import *


class OrderAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'conder', 'datecreation')

admin.site.register(Categories)
admin.site.register(Mark)
admin.site.register(Series)
admin.site.register(Cond)
admin.site.register(Order, OrderAdmin)
