
from django.contrib import admin
from django.urls import path,include
from products import views as index_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view.index ),
    path('products/', include('products.urls'))
]
