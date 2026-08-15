from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("students_lists/", views.students_lists, name="students_lists"),
    path("student_form/", views.student_create, name="student_create"),
    path(
    "<int:student_id>/edit/",
    views.student_update, name="student_update"
),
    path(
    "<int:student_id>/delete/",
    views.student_delete,
    name="student_delete"
),
    path("register/", views.register, name="register"),



]