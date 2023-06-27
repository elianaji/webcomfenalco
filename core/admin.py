from django.contrib import admin
from core.models import login, cpassword
# Register your models here.

class loginAdmin(admin.ModelAdmin):
    pass

admin.site.register(login, loginAdmin)
