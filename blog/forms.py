from django.forms import ModelForm
from .models import Partido, Jugador  # Importa el modelo correcto

class BlogPartido(ModelForm):
    
    class Meta:
        model = Partido  # Usa el modelo 'Partido'
        fields = ["fecha", "lugar", "rival", "resultado"]

class BlogJugador(ModelForm):
    class Meta:
        model = Jugador
        fields = ["nombre", "posicion", "numero"]