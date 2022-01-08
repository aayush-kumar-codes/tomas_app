from django.urls import path
from . import views

urlpatterns = [
    # auth routes
    path('signup/', views.RegisterView.as_view()),
    path('signin/', views.LoginView.as_view())
]