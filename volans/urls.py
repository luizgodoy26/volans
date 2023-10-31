
from companies import urls as companies_urls
from accounts import urls as accounts_urls
from clients import urls as clients_urls
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # Accounts app urls
    path('accounts/', include(accounts_urls)),

    # Companies app urls
    path('companies/', include(companies_urls)),

    # Clients app urls
    path('clients/', include(clients_urls)),

]
