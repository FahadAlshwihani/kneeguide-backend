from django.contrib import admin
from django.urls import path, include  # ← مهم جداً

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('users.urls')),
    path('api/exercises/', include('exercises.urls')),
    path('api/reports/', include('reports.urls')),
    path('api/appointments/', include('appointments.urls')),

]
