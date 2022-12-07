from django.forms import ModelForm
#from .models import SoumissionArticle

# class SoumissionArticleForm(ModelForm):
#     class Meta:
#         model = SoumissionArticle
#         fields = ['titre']

class SignUpForm(UserCreationForm):
    evaluateur = forms.BooleanField(help_text="Etre evaluateur")

    class Meta:
        model = User
        fields = ('username', 'evaluateur', 'password1', 'password2')
