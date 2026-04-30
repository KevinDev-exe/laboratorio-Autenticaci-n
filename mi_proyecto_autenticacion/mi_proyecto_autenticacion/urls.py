from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from calificaciones.views import inicio, registro, CustomPasswordResetView

urlpatterns = [
    path('admin/', admin.site.urls),

    # HOME
    path('', inicio, name='inicio'),

    # AUTH
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # REGISTRO
    path('registro/', registro, name='registro'),

    # RECUPERAR PASSWORD
    path('password_reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset_done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),

    path('app/', include('calificaciones.urls')),
]