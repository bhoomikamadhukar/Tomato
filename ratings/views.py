from django.shortcuts import render,get_object_or_404,redirect
from .models import *
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.models import User


def index(request):
	all_teachers=Teacher.objects.all()		

	return render(request,"home.html",{'all_teachers':all_teachers})

def teaching_post(request,teacher_id):
	teacher=Teacher.objects.get(id=teacher_id)
	all_skills=skills.objects.filter(teacher=teacher)
	reviews = Reviews.objects.filter(teacher=teacher)

	return render(request,"teacher.html",{"teacher":teacher,"all_skills":all_skills, "reviews":reviews})

def review(request,teacher_id):
	teacher=Teacher.objects.get(id=teacher_id)
	reviews = Reviews.objects.filter(teacher=teacher)

	if request.method=="POST":
		form_rating=request.POST['rating']
		form_comment=request.POST['comments']
		review = Reviews(comments = form_comment, teacher=teacher, rating = form_rating, user = request.user)
		review.save()
		teacher.ratings[form_rating] += 1
		teacher.save()

		
		return redirect(f'/teacher/{teacher_id}/')
	return render(request,"ratings.html",{'teacher_id':teacher_id})
		

def signin(request):
	if request.method=='POST':
		username=request.POST.get('username',None)
		password=request.POST.get('password',None)
		user=authenticate(request,username=username,password=password)
		if user is not None:
			print("Im in")
			login(request,user)
			return redirect("/home/")
	return render(request,"login.html")



def signup(request):
	if request.method=='POST':
		usn=request.POST.get('usn',None)
		fullname=request.POST.get('fullname',None)
		email=request.POST.get('email',None)
		username=request.POST.get('username',None)
		password=request.POST.get('password',None)

		user_exists=User.objects.filter(username=username)
		if not user_exists:
			user=User.objects.create_user(
				username=username,
				password=password,
				email=email,
				first_name=fullname.split()[0],
				last_name=" ".join(fullname.split()[1:])
				)
			login(request,user)
			return redirect("/home/")
		else:
			return HttpResponse("Username exists. Try another name")
	return render(request,"signup.html")


def signout(request):
	logout(request)
	return redirect("/home/")