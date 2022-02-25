from django.urls import include, path
from rest_framework import routers
from Main import views
from Main.views import *
from django.urls import path
from django.urls.conf import include
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()


# router.register(r'users', views.UserViewSet)
# router.register(r'supplement', views.SupplementViewSet)
# router.register(r'oceny', views.OcenyViewSet)

urlpatterns = [
    # path('', include(router.urls))
    path('', index, name='index'),
    path('kategoria/<id>/', kategoria, name='kategoria'),
    # path('produkty/<id>', kategoria, name='produkty'),
    path('suplement/<id>', suplement, name='supplement'),
    path('rejestracja/', views.stronaRejestracji, name="rejestracja"),
    path('login/', views.stronaLogowania, name="login"),
    path('wylogowanie/', views.wylogowanie, name="wylogowanie"),
 ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
