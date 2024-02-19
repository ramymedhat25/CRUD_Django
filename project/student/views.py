from django.shortcuts import render ,redirect
from django.http import HttpResponse,JsonResponse

from .models import MyUser, Student


# Create your views here.

def signup(request):
    if request.method =='GET':
       return render(request , 'student/signup.html' )
    elif request.method == 'POST':

        name=request.POST['name']
        email=request.POST['email']
        password=request.POST['psw']

        if_vaild=MyUser.objects.filter(email=email)
        if if_vaild:
            return render(request , 'student/signup.html' )
        # create user
        MyUser.objects.create(name=name, email=email, password=password )
        return redirect('login')

 


def login(request):
    if request.method =='GET':
       return render(request , 'student/login.html' )
    elif request.method == 'POST':
        
        email=request.POST['email']
        password=request.POST['psw']

        if_vaild=MyUser.objects.filter(email=email ,password=password)
        if if_vaild:
             return redirect('home')
        else:
            return render(request , 'student/login.html' )



def home(request):

    return render(request , 'student/home.html')




def students(request):
    students=Student.objects.all()
    context={}
    context['students']=students
    return render(request , 'student/students.html' , context)



def create_student(request):
   
    if request.method =='GET':
       return render(request , 'student/create_student.html' )
    elif request.method == 'POST':

        # create user
        Student.objects.create(f_name=request.POST['firstname'],
                               l_name=request.POST['lastname'],
                               age=request.POST['age']
                              )
        # then :
        return redirect('students')




def edit_student(request, id):
    student = Student.objects.get(id=id)
    if request.method == 'POST':
        student.f_name = request.POST['firstname']
        student.l_name = request.POST['lastname']
        student.age = request.POST['age']
        student.save()
        return redirect('students')
    return render(request, 'student/edit_student.html', {'student': student})



def delete_student(request, id):
    Student.objects.get(id=id).delete()
    # then render redirect to home
    return redirect('home')




def contact(request):
    users=MyUser.objects.all()
    context={}
    context['users']=users
    return render(request , 'student/contact.html' , context)


