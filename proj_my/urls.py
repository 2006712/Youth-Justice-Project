from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # THIS connects your app URLs
    path('', include('justice_app.urls')),
]