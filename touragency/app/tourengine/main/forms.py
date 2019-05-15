from django import forms
from django.core.exceptions import ValidationError

from .models import *

class TourForm(forms.ModelForm):
	class Meta:
		model = Tour
		fields = ['title', 'transport', 'house_night', 'type_food', 'price_per_day']

		widgets = {
			'title': forms.TextInput(attrs={'class': 'form-control'}),
			# 'slug': forms.TextInput(attrs={'class': 'form-control'}),
			'transport': forms.TextInput(attrs={'class': 'form-control'}),
			'house_night': forms.TextInput(attrs={'class': 'form-control'}),
			'type_food': forms.TextInput(attrs={'class': 'form-control'}),
			'price_per_day': forms.TextInput(attrs={'class': 'form-control'})
		}

	def clean_slug(self):
		new_slug = self.cleaned_data['slug'].lower()

		if new_slug == 'create':
			raise ValidationError('Slug can`t be "Create"')
		if Tour.objects.filter(slug__iexact=new_slug).count():
			raise ValidationError('Slug must be unique! We have "{}" slug already'.format(new_slug))
		return new_slug

class CustomerForm(forms.ModelForm):
	class Meta:
		model = Customer
		fields = ['surname', 'name', 'patronymic', 'birthday', 'passport', 'address', 'city', 'telephone', 'tours']

		widgets = {
			'surname': forms.TextInput(attrs={'class': 'form-control'}),
			'name': forms.TextInput(attrs={'class': 'form-control'}),
			'patronymic': forms.TextInput(attrs={'class': 'form-control'}),
			'passport': forms.TextInput(attrs={'class': 'form-control'}),
			'address': forms.TextInput(attrs={'class': 'form-control'}),
			'city': forms.TextInput(attrs={'class': 'form-control'}),
			'telephone': forms.TextInput(attrs={'class': 'form-control'}),
			'tours': forms.SelectMultiple(attrs={'class': 'form-control'}),
			'birthday': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'})
		}

	def clean_slug(self):
		new_slug = self.cleaned_data['slug'].lower()

		if new_slug == 'create':
			raise ValidationError('Slug can`t be "Create"')
		return new_slug

class PensionForm(forms.ModelForm):
	class Meta:
		model = Pension
		fields = ['title', 'address', 'city', 'telephone', 'description', 'rooms', 'swimming_pool', 'medical_services', 
				  'spa', 'level', 'distance']

		widgets = {
			'title': forms.TextInput(attrs={'class': 'form-control'}),
			'address': forms.TextInput(attrs={'class': 'form-control'}),
			'city': forms.TextInput(attrs={'class': 'form-control'}),
			'telephone': forms.TextInput(attrs={'class': 'form-control'}),
			'description': forms.TextInput(attrs={'class': 'form-control'}),
			'rooms': forms.TextInput(attrs={'class': 'form-control'}),
			'swimming_pool': forms.CheckboxInput(attrs={'type': 'checkbox'}),
			'medical_services': forms.CheckboxInput(attrs={'type': 'checkbox'}),
			'spa': forms.CheckboxInput(attrs={'type': 'checkbox'}),
			'level': forms.TextInput(attrs={'class': 'form-control'}),
			'distance': forms.TextInput(attrs={'class': 'form-control'}),
		}

	def clean_slug(self):
		new_slug = self.cleaned_data['slug'].lower()

		if new_slug == 'create':
			raise ValidationError('Slug can`t be "Create"')
		if Pension.objects.filter(slug__iexact=new_slug).count():
			raise ValidationError('Slug must be unique! We have "{}" slug already'.format(new_slug))
		return new_slug


class VoucherForm(forms.ModelForm):
	class Meta:
		model = Voucher
		fields = ['customers', 'tours', 'pensions', 'housings', 'arrival_date', 'departure_date', 'childrens', 
					'medical_insurance', 'people', 'price']

		widgets = {
			'customers': forms.SelectMultiple(attrs={'class': 'form-control'}),
			'tours': forms.SelectMultiple(attrs={'class': 'form-control'}),
			'pensions': forms.SelectMultiple(attrs={'class': 'form-control'}),
			'housings': forms.SelectMultiple(attrs={'class': 'form-control'}),
			'arrival_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
			'departure_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
			'childrens': forms.CheckboxInput(attrs={'type': 'checkbox'}),
			'medical_insurance': forms.CheckboxInput(attrs={'type': 'checkbox'}),
			'people': forms.TextInput(attrs={'class': 'form-control'}),
			'price': forms.TextInput(attrs={'class': 'form-control'}),
		}

	def clean_slug(self):
		new_slug = self.cleaned_data['slug'].lower()

		if new_slug == 'create':
			raise ValidationError('Slug can`t be "Create"')
		if Voucher.objects.filter(slug__iexact=new_slug).count():
			raise ValidationError('Slug must be unique! We have "{}" slug already'.format(new_slug))
		return new_slug


class HousingForm(forms.ModelForm):
	class Meta:
		model = Housing
		fields = ['title', 'category', 'description', 'price']

		widgets = {
			'title': forms.TextInput(attrs={'class': 'form-control'}),
			'category': forms.TextInput(attrs={'class': 'form-control'}),
			'description': forms.TextInput(attrs={'class': 'form-control'}),
			'price': forms.TextInput(attrs={'class': 'form-control'}),
		}

	def clean_slug(self):
		new_slug = self.cleaned_data['slug'].lower()

		if new_slug == 'create':
			raise ValidationError('Slug can`t be "Create"')
		if Housing.objects.filter(slug__iexact=new_slug).count():
			raise ValidationError('Slug must be unique! We have "{}" slug already'.format(new_slug))
		return new_slug