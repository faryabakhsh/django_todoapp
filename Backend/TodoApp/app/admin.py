from django.contrib import admin
from .models import Todo
# Register your models here.
@admin.register(Todo)
class TodoModel (admin.ModelAdmin):
    list_filter = ('title', 'description')
    list_display = ('title', 'description')
