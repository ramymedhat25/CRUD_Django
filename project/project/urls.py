from django.contrib import admin
from django.urls import path
from student.views import home, contact, students, delete_student, edit_student, signup, login, create_student

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),  # Adjusted line
    path('home/', home, name='home'),
    path('students/', students, name='students'),
    path('contact/', contact, name='contact'),
    path('delete_student/<int:id>', delete_student, name='delete_student'),
    path('edit_student/<int:id>', edit_student, name='edit_student'),
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
    path('create_student/', create_student, name='create_student'),
]
