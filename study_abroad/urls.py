from django.urls import path
from .views import homepage_view, program_detail_view


urlpatterns = [
    path('', homepage_view, name='home'),
    path('program/<int:pk>/', program_detail_view, name='program')
]