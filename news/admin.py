from django.contrib import admin
from .models import News,Category
# Register your models here.
admin.site.register(Category)
@admin.register(News)
class NewsListView(admin.ModelAdmin):
    list_display = ('title','status','slug')
    readonly_fields = ('slug'),