from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path, include
from app import views

urlpatterns = (
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', views.MainPage.as_view()),
    path('scientists/', views.ScientistsPage.as_view(), name="scientists"),
    path('scientists/search', views.Search.as_view(), name="search"),
    path('profile/<str:profile_id>', views.ProfilePage.as_view(), name="profile"),
    path('information/', views.information, name="information"),
    path('report/', login_required(views.report), name="report"),
    path('report/export_xls/', login_required(views.export_xls), name="export_xls"),
)


