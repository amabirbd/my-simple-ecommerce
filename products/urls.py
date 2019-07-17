from django.urls import path
from . import views
app_name = 'products'

urlpatterns = [
    path('', views.index, name='index' ),
    path('<product_id>/', views.detail, name = 'detail'),
]
