from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from company import settings

urlpatterns = [
    #АДМИНКА
    path('jet/', include('jet.urls', 'jet')),
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),

    path('admin/', admin.site.urls),
    path('', include('main.urls')),
]

urlpatterns += [
    path("ckeditor5/", include('django_ckeditor_5.urls'), name="ck_editor_5_upload_file"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)