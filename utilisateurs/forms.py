from django.forms import ModelForm
#from .models import SoumissionArticle

# class SoumissionArticleForm(ModelForm):
#     class Meta:
#         model = SoumissionArticle
#         fields = ['titre']

from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser

# class SignUpForm(UserCreationForm):
#     evaluateur = forms.BooleanField(help_text="Etre evaluateur")

#     class Meta:
#         model = User
#         fields = ('username', 'evaluateur', 'password1', 'password2')

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = (
            "username",
            "prenom",
            "nom",
        )  # new

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = (
            "username",
            "prenom",
            "nom",
        )  # new
