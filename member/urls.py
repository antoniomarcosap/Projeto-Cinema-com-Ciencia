from django.urls import path

from .views import MemberView

app_name = 'member'

urlpatterns = [
    path('', MemberView.as_view(), name='member'),
]
