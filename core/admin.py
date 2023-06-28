from django.contrib import admin
from core.models import login, cpassword
# Register your models here.

class loginAdmin(admin.ModelAdmin):
        list_display = ('id','username','password')
        fields= ('id', 'username', 'password')

admin.site.register(login, loginAdmin)

class cpasswordAdmin(admin.ModelAdmin):
    pass

admin.site.register(cpassword, cpasswordAdmin)

class menuAdmin(admin.ModelAdmin):
    pass

admin.site.register(menu, menuAdmin)

