from django.urls import path
from django.conf.urls.static import static
from .views import index_func

urlpatterns = [
    path('', index_func, name='homepage'),
    ]