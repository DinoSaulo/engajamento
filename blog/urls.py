
from django.contrib import admin
from django.urls import path
from core.views import HomeView
from core.views import ContactView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('contato/', ContactView, name='contact'),
]
