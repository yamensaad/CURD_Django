
from django.urls import path, include
from . import views

urlpatterns = [

    path('', views.student_form),
    path('list/', views.student_list)
    # this function get fired when somone visit this page.




]
