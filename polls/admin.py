from django.contrib import admin

from .models import Choice, Question, Userdata
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date','was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)

class UserAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields' : ['username']}),
        (None, {'fields' : ['email']}),
        (None, {'fields' : ['phone_no']}),
        (None, {'fields' : ['password']}),
    ]
    list_display = ('username' ,'email', 'password', 'phone_no')
    list_filter = ['username']
    search_fields = ['username']

admin.site.register(Userdata, UserAdmin)

#admin.site.register(Choice)
