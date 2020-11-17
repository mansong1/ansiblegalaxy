from django.db import migrations, models


INSERT_MODULE_UTILS_CONTENT_TYPE = """
INSERT INTO main_contenttype
  (name, description, created, modified)
VALUES
  ('module_utils', 'Module Utils', now(), now())
"""

DELETE_MODULE_UTILS_CONTENT_TYPE = """
DELETE FROM main_contenttype WHERE name = 'module_utils'
"""


class Migration(migrations.Migration):
    dependencies = [
        ('main', '0090_issue_tracker_url')
    ]

    operations = [
        migrations.AlterField(
            model_name='contenttype',
            name='name',
            field=models.CharField(
                choices=[
                    ('apb', 'Ansible Playbook Bundle'),
                    ('role', 'Role'),
                    ('module', 'Module'),
                    ('module_utils', 'Module Utils'),
                    ('action_plugin', 'Action Plugin'),
                    ('cache_plugin', 'Cache Plugin'),
                    ('callback_plugin', 'Callback Plugin'),
                    ('cliconf_plugin', 'CLI Conf Plugin'),
                    ('connection_plugin', 'Connection Plugin'),
                    ('filter_plugin', 'Filter Plugin'),
                    ('inventory_plugin', 'Inventory Plugin'),
                    ('lookup_plugin', 'Lookup Plugin'),
                    ('netconf_plugin', 'Netconf Plugin'),
                    ('shell_plugin', 'Shell Plugin'),
                    ('strategy_plugin', 'Strategy Plugin'),
                    ('terminal_plugin', 'Terminal Plugin'),
                    ('test_plugin', 'Test Plugin')
                ], db_index=True, max_length=512, unique=True),
        ),
        migrations.RunSQL(sql=INSERT_MODULE_UTILS_CONTENT_TYPE,
                          reverse_sql=DELETE_MODULE_UTILS_CONTENT_TYPE)
    ]
