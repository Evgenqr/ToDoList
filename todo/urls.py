# from django.urls import path
# from . import views
from importlib.resources import path
from django.conf.urls.static import static
from django.conf import settings
from .views import TaskAPIView


urlpatterns = [
    # path('api/v1/todolist/', TaskAPIView.as_view())
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
