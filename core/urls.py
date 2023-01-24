from django.contrib import admin
from django.urls import path, include

from .views import homeview

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', homeview.as_view(), name="home"),

    path('blog/', include('blog.urls', namespace='blog'))
]
