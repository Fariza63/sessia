from django.contrib import admin
from django.urls import path, include  # include қосуды ұмытпа

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('blog.urls')),  # blog қосымшасының маршруттарын тіркейміз
]

