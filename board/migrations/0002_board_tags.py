
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tag', '0001_initial'),
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='tags',
            field=models.ManyToManyField(to='tag.Tag', verbose_name='태그'),
        ),
    ]
