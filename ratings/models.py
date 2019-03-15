from django.db import models
from django.contrib.auth.models import User
from phone_field import PhoneField

class Teacher(models.Model):
	name=models.CharField(max_length=100)
	organization=models.CharField(max_length=100)
	qualification=models.CharField(max_length=100)
	email=models.EmailField(null=True)
	phone = PhoneField(blank=True, help_text='Contact phone number')
	cover=models.ImageField(upload_to="all_covers/",default="all_covers/cover.jpg")

	def __str__(self):
		return f"{self.id}. {self.name}"

	@property
	def get_skill_ratings(self):
		allskills = skills.objects.filter(teacher=self)
		ratings = {}

		for skill in allskills:
			reviews = Reviews.objects.filter(skills=skill)
			total = 0
			count = len(reviews)

			for review in reviews:
				total += review.ratings

			total = total / count

			ratings[skill.skill] = total

		return ratings 

class skills(models.Model):
	teacher= models.ForeignKey(Teacher,on_delete=models.CASCADE)
	skill = models.CharField(max_length=100)

	def __str__(self):
		return f"{self.id}. {self.skill}"

class Reviews(models.Model):
	skills = models.ForeignKey(skills,on_delete=models.CASCADE,null=True)
	teacher=models.ForeignKey(Teacher,on_delete=models.CASCADE)
	ratings=models.IntegerField()
	comments=models.CharField(max_length=100,blank=True,null=True)


	def __str__(self):
		return f" {self.ratings}"
