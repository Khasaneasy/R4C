from django.urls import path

from .views import production_dowload_report

urlpatterns = [
    path('download-report/', production_dowload_report, name='download_report'),
]
