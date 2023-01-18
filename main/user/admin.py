from django.contrib import admin

# Register your models here.
from . import models

class _UserAdmin(admin.ModelAdmin):
    list_display=(
        'id',
        'first_name',
        'last_name',
        'email'
    )

admin.site.register(models.User,_UserAdmin)