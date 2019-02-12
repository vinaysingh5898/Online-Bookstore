from django import forms
from .models import *
from .backends import *
from django.contrib.auth import (
	authenticate,
	get_user_model,
	login,
	logout,
	)

from django.utils.translation import ugettext_lazy as _

class AddAuthorForm(forms.ModelForm):
	class Meta:
		model=Author
		fields=["Name","StartYear","EndYear"]
	def clean(self):
		Name=self.cleaned_data.get("Name")
		EndYear=self.cleaned_data.get("EndYear")
		StartYear=self.cleaned_data.get("StartYear")
		#put validation code here
		author_qs=Author.objects.filter(Name=Name,StartYear=StartYear,EndYear=EndYear)
		# print (author_qs)
		if author_qs.exists():
			raise forms.ValidationError("This author  already exists.")
		# return Name,EndYear,StartYear

# class SellerFilterForm(forms.ModelForm):
	# class Meta:
		# model

User=get_user_model()

class LoginForm(forms.Form):
	email=forms.EmailField()
	password= forms.CharField(widget=forms.PasswordInput)
		
	def clean(self,*args,**kwargs):
		email=self.cleaned_data.get("email")
		password=self.cleaned_data.get("password")
		user=EmailBackend.authenticate(self,username=email,password=password,**kwargs)
		if not user:
			raise forms.ValidationError("This User does not exits")
		if not user.check_password(password):
			raise forms.ValidationError("Incorrect Password")
		if not user.is_active:
			raise forms.ValidationError("This User is no longer active")
		return super(LoginForm,self).clean(*args,**kwargs)

class RegistrationForm(forms.ModelForm):
	password= forms.CharField(widget=forms.PasswordInput,label="Password")
	password2= forms.CharField(widget=forms.PasswordInput,label="Confirm Password")
	email=forms.EmailField(label="Email Address")

	class Meta:
		model=User
		fields=[
		"username",
		"email",
		"first_name",
		"last_name",
		"password",
		]
	def clean_password2(self):
		password=self.cleaned_data.get("password")
		password2=self.cleaned_data.get("password2")
		if password != password2:
			raise forms.ValidationError("Two Password Must Match.")
		return password
	def clean_email(self):
		email=self.cleaned_data.get("email")
		email_qs=User.objects.filter(email=email)
		if email_qs.exists():
			raise forms.ValidationError("This email has already been registered.")
		return email
	labels = {
            "first_name": _("First Name"),
        	"last_name":_("Last Name"),
        	
        }

class CustomerForm(forms.ModelForm):
	class Meta:
		model=Customer
		fields=[
		'PriPhone',
		'SecPhone',
		'LandMark',
		'City',
		'State',
		'Country',
		'PinCode',
		'AddressLine',
		'ProfileImg',
		]
		labels = {
            "PriPhone": _("Primary Phone No"),
        	"SecPhone":_("Secondary Phone No"),
        	"PinCode":_("Pin Code"),
        	"AddressLine":_("Address Line"),
        	"LandMark":_("Land-Mark"),
        	"ProfileImg":_("Profile Picture"),
	        }

class SellerForm(forms.ModelForm):
	class Meta:
		model=Seller
		fields=[
		'PriPhone',
		'SecPhone',
		'LandMark',
		'City',
		'State',
		'Country',
		'PinCode',
		'AddressLine',
		'ProfileImg',
		'Remark',
		'AdharNo',
		]
		labels = {
            "PriPhone": _("Primary Phone No"),
        	"SecPhone":_("Secondary Phone No"),
        	"PinCode":_("Pin Code"),
        	"AddressLine":_("Address Line"),
        	"AdharNo":_("Adhaar No"),
	        "LandMark":_("Land-Mark"),
	        "ProfileImg":_("Profile Picture"),
	        }

class AdminForm(forms.ModelForm):
	class Meta:
		model=Admin
		fields=[
		'Address',
		'Phone'
		]
class PublisherForm(forms.ModelForm):
	class Meta:
		model=Publisher
		fields=[
		'Name',
		# 'Publication',
		'Address',
		'email',
		'Phone',
		]
		labels = {
            "email": _("Email Address"),
	        }
	def clean_email(self):
		email=self.cleaned_data.get("email")
		email_qs=Publisher.objects.filter(email=email)
		if email:
			if email_qs.exists():
				raise forms.ValidationError("This Email has already registered.")
		return email

	def clean_Phone(self):
		Phone=self.cleaned_data.get("Phone")
		if Phone:
			Phone_qs=Publisher.objects.filter(Phone=Phone)
			if Phone_qs.exists():
				raise forms.ValidationError("This Phone no has already registered.")
		return Phone

class BookForm(forms.ModelForm):
	class Meta:
		model=Book
		fields=[
		'Title',
		'Publisher',
		'Authors',
		]
	def clean_Title(self):
		Title=self.cleaned_data.get("Title")
		title_qs=Book.objects.filter(Title=Title)
		if title_qs.exists():
			raise forms.ValidationError("This title is already exists.")
		return Title
class CategoryForm(forms.ModelForm):
	class Meta:
		model=Category
		fields=[
		'Name',
		]
	def clean_Name(self):
		Name=self.cleaned_data.get("Name")
		Category_qs=Category.objects.filter(Name=Name)
		if Category_qs.exists():
			raise forms.ValidationError("This Category is already exists.")
		return Name
class BookCategoryForm(forms.ModelForm):
	class Meta:
		model=BookCategory
		fields=[
		"Category",
		# "Book",
		]
	def clean(self):
		Category=self.cleaned_data.get("Category")
		Book=self.cleaned_data.get("Book")
		Category_qs=BookCategory.objects.filter(Category=Category,Book=Book)
		if Category_qs.exists():
			raise forms.ValidationError("The Book already exists.")
		# return Name
class BookEditionForm(forms.ModelForm):
	class Meta:
		model=BookEdition
		fields=[
			'Book',
			'Edition',
			'YearOfPublication',
			'Price',
			'CoverImage',
			'PageCount',
			'Discount',
			'AvailableNoOfCopies',
		]
		labels = {
            "YearOfPublication": _("Year Of Publication"),
        	"PageCount":_("No. of Pages"),
        	"AvailableNoOfCopies":_("No Of Copies Available "),
        }
        # placeholers = { 
        #     " "YearOfPublication"": _("e.g:1656"),

        # }


class ReviewForm(forms.ModelForm):
	class Meta:
		model=Review
		fields=[
		# 'Customer',
		# 'Book',
		'Content',
		'Ratings',
		]
class adminRecommendationForm(forms.ModelForm):
	class Meta:
		model=adminRecommendation
		fields=[
		'Email',
		]
	def clean_Email(self):
		Email=self.cleaned_data.get("Email")
		Is_existsInUser=User.objects.filter(email=Email)
		Is_existsInAdminRec=adminRecommendation.objects.filter(Email=Email)
		if Is_existsInAdminRec.exists() or Is_existsInUser.exists():
			raise forms.ValidationError("This Email is already registered or in recommendation list.")
		return Email
