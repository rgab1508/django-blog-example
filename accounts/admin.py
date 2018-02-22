from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserProfileAdminCreationForm, UserProfileAdminChangeForm
# Register your models here.
User = get_user_model()

class UserProfileAdmin(BaseUserAdmin):
    search_fields =['email']
    ordering = ('email',)
    filter_horizontal = ()
    form = UserProfileAdminChangeForm
    add_from = UserProfileAdminCreationForm

    list_display = ('email', 'admin')
    list_filter = ('admin',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name',)}),
        ('Permissions', {'fields': ('admin','staff', 'active')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
        ),
    )
admin.site.unregister(Group)
admin.site.register(User, UserProfileAdmin)