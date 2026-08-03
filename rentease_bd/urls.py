from django.contrib import admin
 proma-working-code
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.urls import path, include  # নিশ্চিত করুন 'include' ইমপোর্ট করা আছে

urlpatterns = [
    path('admin/', admin.site.urls),    # জ্যাঙ্গোর ডিফল্ট অ্যাডমিন প্যানেল
    path('', include('home.urls')),     # আমাদের অ্যাপের ইউআরএল রুট
]
 main
