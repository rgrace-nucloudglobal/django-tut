# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_questiontype'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='question_type',
            field=models.ForeignKey(default=1, to='polls.QuestionType'),
            preserve_default=True,
        ),
    ]
