from django.contrib import admin
from .models import *

class ListingTask(admin.ModelAdmin):
  readonly_fields = ('id',)

admin.site.register(Task, ListingTask)

