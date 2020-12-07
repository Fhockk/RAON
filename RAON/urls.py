from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from browsing.views import home, profile, offer

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('home/', home),
    path('home/<slug:category>', home, name='home'),
    path('profile/<slug:username>', profile, name='profile'),
    path('offer/<uuid:offer_uuid>', offer, name='offer')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

print(urlpatterns)
