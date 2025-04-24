from django.forms import ModelForm



class BlogPartido(ModelForm):
    
    class Meta:
        model= ModelForm

        fields= ["fecha","lugar","rival","resultado"]

    