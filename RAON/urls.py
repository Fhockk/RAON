from django.contrib import admin
from django.urls import path

from browsing.views import home, profile, offer

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('home/<slug:category>', home, name='home'),
    path('home/', home),
    path('profile/<uuid:user_id>', profile),
    path('profile/', profile),
    path('offer/<uuid:offer_uuid>', offer, name='offer')
]
