from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('main', '0077_auto_20180201_1639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='importtaskmessage',
            name='message_type',
            field=models.CharField(
                max_length=10, choices=[
                    ('DEBUG', 'DEBUG'), ('INFO', 'INFO'),
                    ('WARNING', 'WARNING'), ('SUCCESS', 'SUCCESS'),
                    ('FAILED', 'FAILED'), ('ERROR', 'ERROR')]),
        ),
        migrations.AlterField(
            model_name='providernamespace',
            name='avatar_url',
            field=models.CharField(max_length=256, null=True,
                                   verbose_name='Avatar URL', blank=True),
        ),
        migrations.AlterField(
            model_name='providernamespace',
            name='company',
            field=models.CharField(max_length=256, null=True,
                                   verbose_name='Company Name', blank=True),
        ),
        migrations.AlterField(
            model_name='providernamespace',
            name='email',
            field=models.CharField(max_length=256, null=True,
                                   verbose_name='Email Address', blank=True),
        ),
        migrations.AlterField(
            model_name='providernamespace',
            name='followers',
            field=models.IntegerField(null=True, verbose_name='Followers'),
        ),
        migrations.AlterField(
            model_name='providernamespace',
            name='html_url',
            field=models.CharField(max_length=256, null=True,
                                   verbose_name='Web Site URL', blank=True),
        ),
        migrations.AlterField(
            model_name='providernamespace',
            name='location',
            field=models.CharField(max_length=256, null=True,
                                   verbose_name='Location', blank=True),
        ),
    ]
