from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
        path("home/",wework_home),
        path("add-emp/",add_emp),
        path("delete-emp/<str:emp_id>",delete_emp),
        path("update-emp/<str:emp_id>",update_emp),
        path("do-update-emp/<str:emp_id>",do_update_emp)
]