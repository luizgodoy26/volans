
from companies import urls as companies_urls
from accounts import urls as accounts_urls
from clients import urls as clients_urls
from items import urls as items_urls
from .views import forbidden_access
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # Accounts app urls
    path('accounts/', include(accounts_urls)),

    # Companies app urls
    path('companies/', include(companies_urls)),

    # Items app urls
    path('items/', include(items_urls)),

    # Clients app urls
    path('clients/', include(clients_urls)),    
    path('', include(clients_urls)),

    # Errors
    path('error/', forbidden_access, name='forbidden_access')

]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
