from django.contrib import admin
from .models import Signup
# Register your models here.

class SignupAdmin(admin.ModelAdmin):
    list_display = ('email', 'timestamp')
    search_fields = ('email', 'timestamp')

admin.site.register(Signup,SignupAdmin)