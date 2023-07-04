from django.contrib import admin
from core.models import login, cpassword, menu, desbloqueo, fechaexpi, cambiarfecha
# Register your models here.

class loginAdmin(admin.ModelAdmin):
    pass

admin.site.register(login, loginAdmin)

class cpasswordAdmin(admin.ModelAdmin):
    pass

admin.site.register(cpassword, cpasswordAdmin)

class menuAdmin(admin.ModelAdmin):
    pass

admin.site.register(menu, menuAdmin)

class desbloqueoAdmin(admin.ModelAdmin):
    pass

admin.site.register(desbloqueo, desbloqueoAdmin)

class fechaexpiAdmin(admin.ModelAdmin):
    pass

admin.site.register(fechaexpi, fechaexpiAdmin)

class cambiarfechaAdmin(admin.ModelAdmin):
    pass

admin.site.register(cambiarfecha, cambiarfechaAdmin)

