from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from app import views

urlpatterns = (
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', views.MainPage.as_view()),
    path('scientists/search/', views.Search.as_view(), name="search"),
    path('scientists/', views.ScientistsPage.as_view(), name="scientists"),
    path('information/', views.information, name="information"),
    path('report/', views.report, name="report"),
    path('report/export/', views.export, name="export"),
    path('report/export_xls/', views.export_xls, name="export_xls"),
    path('profile/<str:profile_id>', views.ProfilePage.as_view(), name="profile")
)


