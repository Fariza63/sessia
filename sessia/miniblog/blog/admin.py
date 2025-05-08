from django.contrib import admin
from .models import Post, Comment

# Модельдерді админ панелінде көрсету
admin.site.register(Post)
admin.site.register(Comment)
