# Generated by Django 4.1.3 on 2022-12-19 04:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('soumissionArticle', '0004_remove_soumissionarticle_titre_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='soumissionarticle',
            name='article',
            field=models.ForeignKey(default=1, editable=False, on_delete=django.db.models.deletion.CASCADE, to='soumissionArticle.article'),
            preserve_default=False,
        ),
    ]