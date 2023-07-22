from django.contrib import admin

# Register your models here.
from .models import Question, Choice

admin.site.site_header="Pollester Admin"
admin.site.site_title="Pollester Admin Area"
admin.site.index_title="Welcome to Pollester Admin Area."

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin (admin.ModelAdmin):
    fieldsets = [(None, {'fields':['question_text']}),
                 ('Date Information', {'fields':['pub_date'], 'classes':['collapse']}), ]
    inlines=[ChoiceInline]


admin.site.register(Question, QuestionAdmin)


# admin.site.register(Question)
# admin.site.register(Choice)