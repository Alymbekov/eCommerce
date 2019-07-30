from django.urls import path

from apps.users.views import SignupView, CabinetView

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('cabinet/<int:pk>/', CabinetView.as_view(), name="cabinet"),
    path('cabinet/', CabinetView.as_view(), name="cabinet"),
]