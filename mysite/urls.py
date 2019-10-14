
from django.contrib import admin
from django.urls import path, include
from . import views
from products import views as index_view
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view.index, name='index'),
    path('products/', include('products.urls')),
    path('accounts/', include('accounts.urls')),
    #path('accounts/', include('allauth.urls')),
    path('auth/', include('allauth.urls')),
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
