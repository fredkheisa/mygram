from django.contrib import admin
from .models import Editor,Pictures,tags

# Register your models here.
admin.site.register(Editor)
admin.site.register(Pictures)
admin.site.register(tags)