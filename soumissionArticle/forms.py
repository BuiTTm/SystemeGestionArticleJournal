from django.forms import ModelForm
from .models import ArticleSubmission

class ArticleSubmissionForm(ModelForm):
    class Meta:
        model = ArticleSubmission
        fields = ['title']
