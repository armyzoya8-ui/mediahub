'''import admin avails all inbuild operations for 
content management'''
from django.contrib import admin
'''import the existing configs fro an admin user'''
from django.contrib.auth.admin import UserAdmin
'''import the custom user schema/custom user table'''
from.models import User

# Register your models here.
# step 1:utilise the admin decorstor to register ur
#model
@admin.register(User)
class CustomUserAdmin(UserAdmin):
    #override the list display of the user info 
    list_display = ('username','email','user_type','is_staff','date_joined')
    # override the filtering of above list
    list_filter = ('user_type', 'is_staff','is_superuser')
    #override what cridentials the admin acn create
    # add our custom fields
    # UserAdmin.fieldsets points to existing django
    # fields thane we add our added fields
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info',{
            'fields': ('user_type','profile_image','bio')
        }),
    )
    #we are above fields to django inbuilt admin 
    #system
    add_fieldssets=UserAdmin.add_fieldsets + (
        ('Additional Info',{'fields':
        ('user_type')}),
    )

