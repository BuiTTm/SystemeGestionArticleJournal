from django.forms import ModelForm
from .models import SoumissionArticle

class SoumissionArticleForm(ModelForm):
    class Meta:
        model = SoumissionArticle
        fields = ['titre']
