from django.db import migrations, models


UPDATE_REPOSITORY = r"""
UPDATE main_repository rp SET (issue_tracker_url) = (
  SELECT DISTINCT
  regexp_replace(regexp_replace(issue_tracker_url, 'api.', ''),
                 '\{/number\}', '')
  FROM main_content c
  WHERE c.repository_id = rp.id
  LIMIT 1
)
"""


class Migration(migrations.Migration):

    dependencies = [('main', '0089_delete_invalid_contents')]

    operations = [
        migrations.AddField(
            model_name='repository',
            name='issue_tracker_url',
            field=models.CharField(
                blank=True,
                max_length=256,
                null=True,
                verbose_name='Issue Tracker URL',
            ),
        ),
        migrations.RunSQL(sql=UPDATE_REPOSITORY),
        migrations.RemoveField(model_name='content', name='issue_tracker_url'),
    ]
