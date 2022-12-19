# Generated by Django 4.1.3 on 2022-12-19 01:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('soumissionArticle', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='auteurs_secondaires',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='article',
            name='auteur',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='ArticleAuteur',
        ),
    ]
