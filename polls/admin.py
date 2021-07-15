from django.contrib import admin
from .models import Poll, Choice, Vote

admin.site.register(Poll)
admin.site.register(Choice)
admin.site.register(Vote)

from import_export import resources
from import_export.admin import ExportMixin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from import_export.admin import ImportExportModelAdmin

# Register your models here.


class UserResource(resources.ModelResource):
    class Meta:
        model = User
        fields = ('id','username','first_name', 'last_name', 'email','password')

# class UserAdmin(ExportMixin, UserAdmin):
#     resource_class = UserResource
#     pass

class UserAdmin(ImportExportModelAdmin):
    list_display = ('id','username','first_name', 'last_name', 'email','password')
    # list_filter = ('created_at',)
    resource_class = UserResource
    pass



admin.site.unregister(User)
admin.site.register(User, UserAdmin)