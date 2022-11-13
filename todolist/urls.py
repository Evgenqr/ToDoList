from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from todo.views import TaskAPIView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('todo.urls')),
    path('api/v1/todolist/', TaskAPIView.as_view()),
    path('api/v1/todolist/<int:pk>/', TaskAPIView.as_view()),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns = [
        path('__debug__/', include('debug_toolbar.urls')),
        ] + urlpatterns
