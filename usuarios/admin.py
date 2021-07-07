from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUsurioCreationForm, CustomUsuarioChangeForm
from .models import CustomUsuario


@admin.register(CustomUsuario)
class CustomUsuarioAdmin(UserAdmin):
    add_form = CustomUsurioCreationForm
    form = CustomUsuarioChangeForm
    model = CustomUsuario
    list_display = ('first_name', 'last_name', 'email', 'telefone', 'is_staff')

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Informações Pessoais', {'fields': ('first_name', 'last_name', 'telefone')}),
        ('Permissões', {'fields': ('is_active', 'is_staff', 'is_super_user', 'groups', 'user_permissions')}),
        ('Datas Importantes', {'fields': ('last login', 'date_joined')})
    )


