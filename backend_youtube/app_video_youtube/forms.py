from django import forms
from .models import Video

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['id_video', 'id_canal', 'titulo', 'fecha_subida', 'duracion', 'vistas']
        labels = {
            'id_video': 'Video ID',
            'id_canal': 'Canal ID',
            'titulo': 'Título',
            'fecha_subida': 'Fecha de Subida',
            'duracion': 'Duración',
            'vistas': 'Vistas'
        }
        widgets = {
            'id_video': forms.TextInput(attrs={'class': 'form-control'}),
            'id_canal': forms.TextInput(attrs={'class': 'form-control'}),
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_subida': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'duracion': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'vistas': forms.NumberInput(attrs={'class': 'form-control'}),
        }
