from django.contrib import admin
from django.urls import path, re_path
from student.views import view_hello, view_hello_20, view_record  # Import views correctly

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^hello1/', view_hello),
    re_path(r'^hello20/', view_hello_20),
    re_path(r'^record1/', view_record),
    # re_path(r'^django/', view_django),  # Uncomment if the function exists in views
]
