from django.shortcuts import render,HttpResponse,redirect
from crudapp import models
# Create your views here.

def student_cards(request):
    if request.method=='POST':
        photo=request.FILES.get('photo')
        name=request.POST.get('name')
        section=request.POST.get('section')
        address=request.POST.get('address')
        phone=request.POST.get('phone')
        bloodgroup=request.POST.get('bloodgroup')
        student = models.Students.objects.create(
            photo=photo, name=name,section=section,address=address,phone=phone,b_group=bloodgroup
        )
        student.save()
        return HttpResponse('Student added Successfully')
    students = models.Students.objects.all()

    return render(request,'students.html',{'students':students})

def student_form(request):
    if request.method=='POST':
        photo=request.FILES.get('photo')
        name=request.POST.get('name')
        section=request.POST.get('section')
        address=request.POST.get('address')
        phone=request.POST.get('phone')
        bloodgroup=request.POST.get('bloodgroup')
        student = models.Students.objects.create(
            photo=photo, name=name,section=section,address=address,phone=phone,b_group=bloodgroup
        )
        student.save()
        return HttpResponse('Student added Successfully')
    return redirect('students')

def student_edit(request,id):
    student= models.Students.objects.get(id=id)
    print(request)
    if request.method=='POST':
        print(request.FILES)
         # Check if the 'photo' field exists in the POST data
        if 'photo' in request.FILES:
            student.photo = request.FILES['photo']
        student.name=request.POST.get('name')
        student.section=request.POST.get('section')
        student.address=request.POST.get('address')
        student.phone=request.POST.get('phone')
        student.b_group=request.POST.get('bloodgroup')
        student.save()
        return redirect('students')
    return render(request,'students_edit.html',{'student':student})

def student_delete(request,id):
    student = models.Students.objects.get(id=id)
    student.delete()
    return redirect('students')
