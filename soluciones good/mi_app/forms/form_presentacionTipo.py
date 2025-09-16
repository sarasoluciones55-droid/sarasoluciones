from django import forms
from django.forms import ModelForm, TextInput
from mi_app.models import PresentacionTipo

class presentacionTipoForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs['autofocus'] = True
    
    class Meta:
        model = PresentacionTipo
        fields = '__all__'
        widgets = {
            'Nombre de la presentacion': TextInput(
                attrs={
                    'placeholder': 'Ingrese el nombre de la presentación',
                }
            ),
            'Color': TextInput(
                attrs={
                    'placeholder': 'Ingrese el color',
                }
            ),
            'Modelo': TextInput(
                attrs={
                    'placeholder': 'Ingrese el modelo de la presentacion',
                }
            ),
            'Funcion principal': TextInput(
                attrs={
                    'placeholder': 'cual es la funcion principal',
                }
                
            ),
            'Descripcion': TextInput(
                attrs={
                    'placeholder': 'Ingrese una breve descripcion',
                }
            ),
        }