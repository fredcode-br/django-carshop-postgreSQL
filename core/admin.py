from django.contrib import admin

from .models import Fabricante, Tipo, Categoria, Veiculo, VeiculoImage
from .forms import VeiculoImageForm


admin.site.register(Fabricante)
admin.site.register(Tipo)
admin.site.register(Categoria)
admin.site.register(Veiculo)

@admin.register(VeiculoImage)
class VeiculoImageAdmin(admin.ModelAdmin):
    form = VeiculoImageForm
    list_display = ['veiculo']

    
  

    def save_model(self, request, obj, form, change):
        fotos = request.FILES.getlist('foto')
        for foto in fotos:
            if (foto == fotos[(len(fotos)-1)]):
                pass
            else:
                instance=VeiculoImage(foto=foto,  veiculo_id=obj.veiculo.pk)
                instance.save()
        return super(VeiculoImageAdmin, self).save_model(request, obj, form, change)




 
    