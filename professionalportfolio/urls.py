
from django.contrib import admin
from django.urls import path, include 
from django.conf import settings #Add this to get the settings.py
from django.conf.urls.static import static #for static files
import jobs.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',jobs.views.home, name='home'),
    path('blog/', include('blog.urls')),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) #for dynamic image url click
