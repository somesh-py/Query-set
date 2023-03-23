from django.shortcuts import render
from .models import Student
# Create your views here.

# query-set return queries

def all_data(request):
    student_data=Student.objects.all()
    # student_data=Student.objects.filter(marks=70)
    # student_data=Student.objects.exclude(marks=70)
    # student_data=Student.objects.order_by('name')
    # student_data=Student.objects.order_by('-name')
    # student_data=Student.objects.order_by('?')
    # student_data=Student.objects.order_by('id')
    # student_data=Student.objects.order_by('id').reverse()
    # student_data=Student.objects.order_by('id').reverse()[0:7]
    # student_data=Student.objects.values('name','roll')
    # student_data=Student.objects.values_list('id','name')
    print("Return:",student_data)
    print()
    print("SQL Query :",student_data.query)       
    return render(request,'index.html',{'student':student_data})


# query-set return object

def all_data_object(request):
    # student_data=Student.objects.get(pk=1)
    # student_data=Student.objects.first()
    # student_data=Student.objects.order_by('name').first()
    # student_data=Student.objects.last()
    # student_data=Student.objects.latest('passdate')
    # student_data=Student.objects.earliest('passdate')
    # student_data=Student.objects.all()
    # print(student_data.exists())
    # student_data=Student.objects.create(name='sonam',roll=115,city='indore',marks=70,passdate='2000-01-20')
    # student_data=Student.objects.get_or_create(name='sonam',roll=115,city='indore',marks=70,passdate='2000-01-20')
    # student_data=Student.objects.filter(roll=107).update(name='sonam',roll=115,city='indore',marks=70,passdate='2000-01-20')
    # student_data=Student.objects.filter(roll=107).update_or_create(name='sonam',roll=115,city='indore',marks=70,passdate='2000-01-20')
    # objs=[
    #     Student(name='rajkumar',roll=116,city='indore',marks=80,passdate='2000-01-21')
    #     Student(name='rajaan',roll=117,city='bhopal',marks=60,passdate='2000-10-12')
    #     Student(name='jignesh',roll=118,city='rajgadh',marks=50,passdate='2000-11-23')
    #     Student(name='sanjeev',roll=119,city='pipliya',marks=40,passdate='2000-14-22')
    # ]
    # student_data=Student.objects.bulk_create(objs)
    # student_data=Student.objects.all()
    # for i in student_data:
    #     i.city='dhar'
    # student_data=Student.objects.bulk_update(student_data,['city'])
    # student_data=Student.objects.in_bulk()
    # student_data=Student.objects.in_bulk()
    # print("Return:",student_data[2].name)
    # student_data=Student.objects.get(pk=10).delete()
    # student_data=Student.objects.filter(marks=75).delete()
    # student_data=Student.objects.all().delete()
    student_data=Student.objects.all()
    print("Return:",student_data.count())
    return render(request,'objecct_index.html',{'student':student_data})
