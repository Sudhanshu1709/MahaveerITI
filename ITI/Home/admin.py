from django.contrib import admin
from .models.notice import Notice
from .models.image import Image
# Register your models here.
class AdminNotice(admin.ModelAdmin):
    list_display = ['name', 'pdf']

class AdminImage(admin.ModelAdmin):
    list_display = ['images']

admin.site.register(Notice, AdminNotice)
admin.site.register(Image, AdminImage)