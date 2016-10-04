from django.conf.urls import url,include
from django.contrib import admin
from django.conf import settings
from django.views.static import serve
from django.conf.urls.static import static
from cart import urls as cartUrls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(
    	regex=r'^media/(?P<path>.*)/$',
    	view=serve,
    	kwargs={"document_root":settings.MEDIA_ROOT}
    	),
    url(r'^cart/',include(cartUrls,namespace='cart')),
    	]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)