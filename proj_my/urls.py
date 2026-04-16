from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('justice_app.urls', 'justice_app'), namespace='justice_app')),
]

admin.site.site_header = "Youth Justice Administration"
admin.site.site_title = "Youth Justice Admin Portal"
admin.site.index_title = "Youth Diversion & Support Matching System"