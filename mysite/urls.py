from django.contrib import admin
from django.urls import include, path
##### For Image Upload
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('polls/', include('polls.urls')),
    path('news/', include('news.urls')),
    path('restapi/', include('restapi.urls')),
    path('admin/', admin.site.urls),
]


#### For Image Upload finance-instcollect-transaction 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#managecollect

