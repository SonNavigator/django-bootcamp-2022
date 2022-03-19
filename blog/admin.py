from django.contrib import admin
from .models import Post, Author

from django_summernote.admin import SummernoteModelAdmin


class PostAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'
    list_display = [
        'title',
        'date_created',
        'date_updated'
    ]

# admin.site.register(Model, AdminClass)
admin.site.register(Post, PostAdmin)

admin.site.register(Author)


