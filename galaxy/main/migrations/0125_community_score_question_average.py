from django.db import migrations

SET_COMMUNITY_SCORE_TO_QUESTION_AVERAGE = """
UPDATE main_repository
set community_score =
    (SELECT (((sum(docs-1))/4.0 +
             sum(ease_of_use-1)/4.0 +
             sum(does_what_it_says-1)/4.0 +
             sum(works_as_is-1)/4.0 +
             sum(used_in_production-1)/4.0
             ) / (count(docs) + count(ease_of_use) + count(does_what_it_says) +
                  count(works_as_is) + count(used_in_production)))
            * 5 as average
    FROM main_communitysurvey
        WHERE main_communitysurvey.repository_id = main_repository.id)
"""


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0124_auto_20181210_1433'),
    ]

    operations = [
        migrations.RunSQL(SET_COMMUNITY_SCORE_TO_QUESTION_AVERAGE),
    ]
