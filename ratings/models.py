from django.db import models
from django.contrib.auth.models import User
from phone_field import PhoneField	
import jsonfield

class Teacher(models.Model):
	name=models.CharField(max_length=100)
	organization=models.CharField(max_length=100)
	qualification=models.CharField(max_length=100)
	email=models.EmailField(null=True)
	phone = PhoneField(blank=True, help_text='Contact phone number')
	cover=models.ImageField(upload_to="all_covers/",default="all_covers/cover.jpg")
	ratings = jsonfield.JSONField(default={5:0,4:0,3:0,2:0,1:0})

	def __str__(self):
		return f"{self.id}. {self.name}"

	@property
	def get_skill_ratings(self):

		total = 0
		sum_votes = 0
		for key, value in self.ratings.items():
			total += int(key) * int(value)
			sum_votes += int(value)

		if sum_votes == 0:
			return 0

		return total/sum_votes

class skills(models.Model):
	teacher= models.ForeignKey(Teacher,on_delete=models.CASCADE)
	skill = models.CharField(max_length=100)

	def __str__(self):
		return f"{self.id}. {self.skill}"

class Reviews(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
	skills = models.ForeignKey(skills,on_delete=models.CASCADE,null=True)
	teacher=models.ForeignKey(Teacher,on_delete=models.CASCADE)
	rating = models.FloatField(default=0.0, null=True, blank=True)
	
	comments=models.CharField(max_length=100,blank=True,null=True)


	def __str__(self):
		return f" {self.teacher}|{self.rating}"
