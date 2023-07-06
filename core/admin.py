from django.contrib import admin
from core.models import login, cpassword, menu, desbloqueo, bloquear_usuario, desbloquear_usuario, fechaexpi, cambiarfecha
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

class bloquear_usuarioAdmin(admin.ModelAdmin):
    pass

admin.site.register(bloquear_usuario, bloquear_usuarioAdmin)

class desbloquear_usuarioAdmin(admin.ModelAdmin):
    pass

admin.site.register(desbloquear_usuario, desbloquear_usuarioAdmin)


class fechaexpiAdmin(admin.ModelAdmin):
    pass

admin.site.register(fechaexpi, fechaexpiAdmin)

class cambiarfechaAdmin(admin.ModelAdmin):
    pass

admin.site.register(cambiarfecha, cambiarfechaAdmin)

