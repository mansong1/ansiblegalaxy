from django.db import migrations, models
import galaxy.main.fields

STRIP_VERSION_SUFFIX = """
UPDATE main_repositoryversion
SET version = substring(version from 2)
WHERE version ILIKE 'v%'
"""

UPDATE_NON_SEMVER_VERSIONS = r"""
UPDATE main_repositoryversion
SET version = NULL
WHERE version !~ ('^' ||
                  '(0|[1-9][0-9]*)\.' ||
                  '(0|[1-9][0-9]*)\.' ||
                  '(0|[1-9][0-9]*)' ||
                  '(\-' ||
                  '(0|[1-9A-Za-z-][0-9A-Za-z-]*)' ||
                  '(\.(0|[1-9A-Za-z-][0-9A-Za-z-]*))*)?' ||
                  '(\+[0-9A-Za-z-]+(\.[0-9A-Za-z-]+)*)?' ||
                  '$');
"""

DELETE_VERSION_DUPLICATES = """
DELETE FROM main_repositoryversion
WHERE id IN (
  SELECT t.id FROM (
    SELECT
      id,
      row_number() OVER (
        PARTITION BY repository_id, version ORDER BY id DESC
      ) AS row
    FROM main_repositoryversion
  ) t
  WHERE t.row > 1
)
"""


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0103_repository_download_count'),
    ]

    operations = [
        migrations.RunSQL('SET CONSTRAINTS ALL IMMEDIATE',
                          reverse_sql=migrations.RunSQL.noop),
        migrations.RemoveField(
            model_name='repositoryversion',
            name='active',
        ),
        migrations.RemoveField(
            model_name='repositoryversion',
            name='description',
        ),
        migrations.RenameField(
            model_name='repositoryversion',
            old_name='name',
            new_name='tag',
        ),
        migrations.AlterField(
            model_name='repositoryversion',
            name='tag',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='repositoryversion',
            name='loose_version',
            field=galaxy.main.fields.VersionField(max_length=64, null=True),
        ),
        migrations.RenameField(
            model_name='repositoryversion',
            old_name='loose_version',
            new_name='version',
        ),
        migrations.RunSQL(
            sql=(STRIP_VERSION_SUFFIX,
                 UPDATE_NON_SEMVER_VERSIONS,
                 DELETE_VERSION_DUPLICATES),
        ),
        migrations.AlterUniqueTogether(
            name='repositoryversion',
            unique_together={('repository', 'version')},
        ),
        migrations.AlterModelOptions(
            name='repositoryversion',
            options={'ordering': ('-version',)},
        ),
        migrations.RenameField(
            model_name='repositoryversion',
            old_name='release_date',
            new_name='commit_date'
        ),
        migrations.AlterField(
            model_name='repositoryversion',
            name='commit_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='repositoryversion',
            name='commit_sha',
            field=models.CharField(max_length=40, null=True),
        ),
    ]
