from django.urls import path
from .views import MembershipSelectView

app_name = 'membership'

urlpatterns = [
    path('membership/', MembershipSelectView.as_view(), name='select'),
]
