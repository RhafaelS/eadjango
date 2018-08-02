from django.contrib import admin
from django import forms
from .models import Post

class PostAdminForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = '__all__'


class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm
    list_display = ['title', 'text', 'created_date']
    readonly_fields = ['title', 'text', 'created_date']

admin.site.register(Post, PostAdmin)
