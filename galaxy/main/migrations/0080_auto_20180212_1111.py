from django.db import migrations
import galaxy.main.fields


class Migration(migrations.Migration):

    dependencies = [('main', '0079_auto_20180208_0650')]

    operations = [
        migrations.AlterField(
            model_name='repository',
            name='commit_message',
            field=galaxy.main.fields.TruncatingCharField(
                default='', max_length=256, blank=True
            ),
        )
    ]
