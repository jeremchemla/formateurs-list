from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.search_formateurs, name='search_formateurs'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)