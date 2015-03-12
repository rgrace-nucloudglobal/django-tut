# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_question_question_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='questiontype',
            name='other_stuff',
            field=models.CharField(max_length=100, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='question',
            name='question_type',
            field=models.ForeignKey(to='polls.QuestionType'),
            preserve_default=True,
        ),
    ]
