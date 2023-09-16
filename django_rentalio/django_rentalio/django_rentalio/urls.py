"""
URL configuration for django_rentalio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from .views import change_theme, chart_data, login_view, otp_view, logout_view, AboutView, HomeView,StatsView

urlpatterns = [
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    path('nadmin1/', admin.site.urls),
    path('',HomeView.as_view(),name='home'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('otp/', otp_view, name='otp'),
    path('about/', AboutView.as_view(), name='about'),
    path('stats/', StatsView.as_view(), name='stats'),
    path('chart-data/', chart_data, name='data'),
    path('switch/',change_theme,name='change'),
    path('books/',include('books.urls',namespace='books')),
    path('authors/', include('authors.urls', namespace='authors')),
    path('rentals/', include('rentals.urls', namespace='rentals')),
    path('publishers/', include('publishers.urls', namespace='publishers')),
    path("__reload__/", include("django_browser_reload.urls")),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = 'Rental System Administration'
