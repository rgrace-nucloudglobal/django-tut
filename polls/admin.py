from django.contrib import admin
from polls.models import Question, Choice, QuestionType
# from django.contrib.admin.helpers import Fieldset

# Register your models here.

# adds displaying of related choices to question display
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2


# configure choice type admin display
class QuestionTypeAdmin(admin.ModelAdmin):
    fields = ['question_type_text', 'other_stuff']

# configure question admin display
class QuestionAdmin(admin.ModelAdmin):
    # basic listing of 2 fields
#     fields = ['question_text', 'pub_date', 'question_type']

    # show in separate groupings
#     fieldsets = [
#         (None, {'fields': ['question_text']}
#          ), ('Date info', {'fields': ['pub_date']})
#     ]

    # show one grouping collapsed
    fieldsets = [
        (None, {'fields': ['question_text']}
         ), ('Date info', {'fields': ['pub_date', 'question_type'], 'classes': ['collapse']})
    ]
    inlines = [ChoiceInline]

    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']

# configure choice admin display
class ChoiceAdmin(admin.ModelAdmin):
    fields = ['votes', 'choice_text', 'question']

admin.site.register(QuestionType, QuestionTypeAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)