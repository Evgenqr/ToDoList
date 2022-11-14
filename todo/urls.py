from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import TaskAPIView, TaskAPIList


urlpatterns = [
    path('api/v1/todolist/', TaskAPIList.as_view()),
    path('api/v1/todolist/<int:pk>/', TaskAPIList.as_view()),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
