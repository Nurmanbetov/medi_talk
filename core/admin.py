from django.contrib import admin
from .models import Doctor, Patient, Record
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _


class CustomUserAdmin(UserAdmin):
    """
        Creating own admin and customise it to our own works
    """
    fieldsets = (
        (None, {'fields': ('phone_number', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name',)}),
        (_('Important dates'), {'fields': ( 'joining_date',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email','first_name','last_name' ,'phone_number', 'password1', 'password2'),
        }),
    )
    list_display = ('phone_number', 'first_name', 'last_name', 'email')
    

admin.site.register(Doctor, CustomUserAdmin)
admin.site.register(Patient, CustomUserAdmin)
admin.site.register(Record)
