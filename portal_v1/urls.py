from django.urls import path
from announcements.views import AnnouncementCreateView, AnnouncementListView, AnnouncementDetailView, \
    AnnouncementUpdateView, \
    AnnouncementDeleteView
from users.views import LoginView, logout_view, RegisterView, ChangePassword


app_name = "users"

urlpatterns = [
    path('', AnnouncementListView.as_view(), name='announcement-home'),
    path('announcements/<int:pk>/', AnnouncementDetailView.as_view(), name='announcement_detail'),
    path('announcements/<int:pk>/update/', AnnouncementUpdateView.as_view(), name='announcement-update'),
    path('announcements/<int:pk>/delete/', AnnouncementDeleteView.as_view(), name='announcement-delete'),
    path('announcements/new/', AnnouncementCreateView.as_view(), name='announcement-create'),
    path('login/', LoginView.as_view(), name="login"),
    path("logout/", logout_view, name="logout"),
    path("register/", RegisterView.as_view(), name="register"),
    path("change_password/", ChangePassword.as_view(), name="change_password"),
]
