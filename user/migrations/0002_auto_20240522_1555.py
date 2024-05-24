
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': '사용자', 'verbose_name_plural': '사용자'},
        ),
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.CharField(max_length=50, null=True, verbose_name='이메일'),
        ),
    ]
