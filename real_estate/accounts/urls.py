from django.urls import path,include
from .views import register_view,profileUpdate_view,profile_view


urlpatterns = [
	path("",include("django.contrib.auth.urls")),
	path("register/",register_view,name="user_register"),
	path("profile_update/",profileUpdate_view,name="profile_update"),
	path("profile/<int:pk>/",profile_view.as_view(),name="profile")
]