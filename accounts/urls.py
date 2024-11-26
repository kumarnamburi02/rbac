from django.urls import path
from .views import RegisterView, LoginView, LogoutView, home
from .views import AdminProfileView, ModeratorProfileView, UserProfileView

urlpatterns = [
    # Authentication URLs
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    
    # Home page
    path('', home, name='home'),

    # Role-specific profile views
    path('admin/profiles/', AdminProfileView.as_view(), name='admin-profile'),
    path('moderator/profiles/', ModeratorProfileView.as_view(), name='moderator-profile'),
    path('user/profile/', UserProfileView.as_view(), name='user-profile'),
]
