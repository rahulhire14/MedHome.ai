from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse


# Home page view
def home(request):
    return HttpResponse(
        """
        <h1>MedHome.ai Backend Running 🚀</h1>
        <p>Authentication & Profile APIs are active.</p>
        <ul>
            <li>/api/auth/</li>
            <li>/api/profile/</li>
            <li>/admin/</li>
        </ul>
        """
    )


urlpatterns = [
    path("", home, name="home"),
    path("admin/", admin.site.urls),
    path("api/auth/", include("accounts.urls")),
    path("api/profile/", include("profiles.urls")),
]
