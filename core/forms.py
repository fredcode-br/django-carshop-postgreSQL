from django import forms
from core.models import Fabricante, Categoria, Veiculo, VeiculoImage

              

class VeiculoImageForm(forms.ModelForm):
    class Meta:
        model = VeiculoImage
        fields = ['foto', 'veiculo']

        widgets = {
            'foto': forms.ClearableFileInput(attrs={'multiple': True}),
        }

