from django.urls import path
from . import views  # Import views from the users app
# users/urls.py
from users import views  # This line is fine as long as views.py doesn't import urls.py


urlpatterns = [
    # Example route:
    path('', views.home, name='users-home'),  # Replace `home` with your actual view
]
