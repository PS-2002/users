from django.urls import path
from .views import user_login, user_logout, signup, doctor_dashboard, patient_dashboard
from blog.views import create_blog_post, doctor_blog_list, patient_blog_list_by_category

urlpatterns = [
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('', signup, name='signup'),
    path('doctor/dashboard/', doctor_dashboard, name='doctor_dashboard'),
    path('patient/dashboard/', patient_dashboard, name='patient_dashboard'),
    path('create_blog_post/', create_blog_post, name='create_blog_post'),
    path('doctor_blog_list/', doctor_blog_list, name='doctor_blog_list'),
    path('patient_blog_list_by_category/<str:category>/', patient_blog_list_by_category, name='patient_blog_list_by_category')
]
