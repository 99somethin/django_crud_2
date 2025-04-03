from django.contrib import admin
from apps.news.models import Articles
# Register your models here.

class NewsAdmin(admin.ModelAdmin):
    fields = ['title', 'anons', 'date', 'full_text']


admin.site.register(Articles, NewsAdmin)

