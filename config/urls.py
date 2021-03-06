from django.conf import settings
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls")),
    path("tasks/", include("tasks.urls")),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns.append(path("", include(debug_toolbar.urls)))
