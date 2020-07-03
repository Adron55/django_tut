from django.contrib import admin
from .models import News,Faq,Contact
from django.contrib.auth.models import Group,Permission
# Register your models here.

#Filter News
class NewsFilter(admin.ModelAdmin):
    list_display = ('title','date_created','date_modified')
#Filter Faqs
class FaqsFilter(admin.ModelAdmin):
    list_display = ('question','date_created','date_modified')


admin.site.register(News,NewsFilter)
admin.site.register(Faq,FaqsFilter)
admin.site.register(Contact)

admin.site.site_header = "Task Admin Panel"

moderator_group, created = Group.objects.get_or_create(name='Moderator')
user_group, created = Group.objects.get_or_create(name='User')
