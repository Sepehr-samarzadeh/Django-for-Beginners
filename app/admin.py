from django.contrib import admin
from app.models import JobPost
# Register your models here.

class JobAdmin(admin.ModelAdmin):
    list_display = ('title','date','salary')
    list_filter = ('date','salary',)
    search_fields = ['title']
    fields = [('title','description'),'expiry']
    

admin.site.register(JobPost,JobAdmin)