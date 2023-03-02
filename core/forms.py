from django import forms
from core.models import Fabricante, Categoria, Veiculo, VeiculoImage
       

class FormFabricante(forms.ModelForm):
    class Meta:
        model = Fabricante
        fields = '__all__'

class FormCategoria(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'

class FormVeiculo(forms.ModelForm):
    class Meta:
        model = Veiculo
        fields = '__all__'
              
class VeiculoImageForm(forms.ModelForm):
    class Meta:
        model = VeiculoImage
        fields = ['foto', 'veiculo']

        widgets = {
            'foto': forms.ClearableFileInput(attrs={'multiple': True}),
        }