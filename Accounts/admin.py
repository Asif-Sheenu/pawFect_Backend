from django.contrib import admin
from .models import User# Register your models here.

@admin.register(User)
class UserAdemin (admin.ModelAdmin):
    list_display = ('email','is_staff','is_active')
    ordering= ('email',)