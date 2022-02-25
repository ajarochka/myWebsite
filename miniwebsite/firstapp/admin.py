from django.contrib import admin
from .models import *
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
# Register your models here.

class NewsAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = News
        fields = '__all__'

class NewsAdmin(admin.ModelAdmin):
    form = NewsAdminForm
    list_display = ['id', 'title', 'content', 'category', 'created_at', 'update_at', 'is_published']
    list_display_links = ['id', 'title', 'category']
    search_fields = ['title', 'content', 'category']
    list_editable = ('is_published',)
    list_filter = ('update_at', 'is_published', 'category')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_display_links = ['id', 'title']
    search_fields = ['title',]

admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)