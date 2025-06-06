from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('fitnessapp.urls')),  #routes all API traffic to the fitnessapp
]
