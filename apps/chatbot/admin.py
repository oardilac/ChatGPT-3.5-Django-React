from django.contrib import admin
from .models import AIPost, Answer

# Register your models here.
class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 1

class AIPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'pub_date')
    search_fields = ['title']
    inlines = [AnswerInline]

admin.site.register(AIPost, AIPostAdmin)
admin.site.register(Answer)
