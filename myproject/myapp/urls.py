from django.urls import path
from .views import user_login, user_logout, signup, doctor_dashboard, patient_dashboard

urlpatterns = [
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('', signup, name='signup'),
    path('doctor/dashboard/', doctor_dashboard, name='doctor_dashboard'),
    path('patient/dashboard/', patient_dashboard, name='patient_dashboard')
]
