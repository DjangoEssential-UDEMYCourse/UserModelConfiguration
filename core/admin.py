from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', '_autor')
    exclude = ['autor', ]

    def _autor(self, instance):
        return f'{instance.autor.get_full_name()}'

    '''
        Sobreescrendo method para filtrar pelo usuario logado
    '''
    def get_queryset(self, request):
        qs = super(PostAdmin, self).get_queryset(request)
        return qs.filter(autor=request.user)

    '''
        Sobreescrevendo method de salvamento
        para pegar o usuario logado na sessao
    '''
    def save_model(self, request, obj, form, change):
        obj.autor = request.user
        super().save_model(request, obj, form, change)
