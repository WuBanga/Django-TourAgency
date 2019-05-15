from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify
from time import time


def gen_slug(s):
	new_slug = slugify(s, allow_unicode=True)
	return new_slug + '-' + str(int(time()))


class Customer(models.Model):
	slug = models.SlugField(max_length=150, blank=True, unique=True)
	surname = models.CharField(max_length=150, db_index=True)
	name = models.CharField(max_length=150, db_index=True)
	patronymic = models.CharField(max_length=150, db_index=True)
	passport = models.CharField(max_length=50, db_index=True)
	address = models.CharField(max_length=150, db_index=True)
	city = models.CharField(max_length=150, db_index=True)
	telephone = models.CharField(max_length=20, db_index=True)
	birthday = models.DateTimeField()

	tours = models.ManyToManyField('Tour', blank=True, related_name='customers')


	def get_absolute_url(self):
		return reverse('customers_detail_url', kwargs={"slug": self.slug})
	
	def get_update_url(self):
		return reverse('customer_update_url', kwargs={'slug': self.slug})

	def get_delete_url(self):
		return reverse('customer_delete_url', kwargs={'slug': self.slug})

	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = gen_slug(self.surname)
		super().save(*args, **kwargs)


	def __str__(self):
		# return '{}'.format(self.surname)
		return self.surname

	class Meta:
		ordering = ['surname']

class Tour(models.Model):
	slug = models.SlugField(max_length=150, unique=True)
	title = models.CharField(max_length=150, db_index=True)
	transport = models.CharField(max_length=150, db_index=True)
	house_night = models.CharField(max_length=150, db_index=True)
	type_food = models.CharField(max_length=150, db_index=True)
	price_per_day = models.CharField(max_length=150, db_index=True)

	def get_absolute_url(self):
		return reverse('tour_detail_url', kwargs={"slug": self.slug})
	
	def get_update_url(self):
		return reverse('tour_update_url', kwargs={'slug': self.slug})

	def get_delete_url(self):
		return reverse('tour_delete_url', kwargs={'slug': self.slug})

	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = gen_slug(self.title)
		super().save(*args, **kwargs)

	def __str__(self):
		return '{}'.format(self.title)

	class Meta:
		ordering = ['title']

class Pension(models.Model):
	slug = models.SlugField(max_length=150, blank=True, unique=True)
	title = models.CharField(max_length=150, db_index=True)
	address = models.CharField(max_length=150, db_index=True)
	city = models.CharField(max_length=150, db_index=True)
	telephone = models.CharField(max_length=20, db_index=True)
	description = models.CharField(max_length=150, db_index=True)
	rooms = models.IntegerField(db_index=True)
	swimming_pool = models.BooleanField(db_index=True)
	medical_services = models.BooleanField(db_index=True)
	spa = models.BooleanField(db_index=True)
	level = models.IntegerField(db_index=True)
	distance = models.IntegerField(db_index=True)

	def get_absolute_url(self):
		return reverse('pension_detail_url', kwargs={"slug": self.slug})
	
	def get_update_url(self):
		return reverse('pension_update_url', kwargs={'slug': self.slug})

	def get_delete_url(self):
		return reverse('pension_delete_url', kwargs={'slug': self.slug})

	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = gen_slug(self.title)
		super().save(*args, **kwargs)

	def __str__(self):
		return self.title

	class Meta:
		ordering = ['title']

class Voucher(models.Model):
	slug = models.SlugField(max_length=150, blank=True, unique=True)
	customers = models.ManyToManyField('Customer', blank=True, related_name='vouchers')
	tours = models.ManyToManyField('Tour', blank=True, related_name='vouchers')
	pensions = models.ManyToManyField('Pension', blank=True, related_name='vouchers')
	housings = models.ManyToManyField('Housing', blank=True, related_name='vouchers')
	arrival_date = models.DateTimeField()
	departure_date = models.DateTimeField()
	childrens = models.BooleanField(db_index=True)
	medical_insurance = models.BooleanField(db_index=True)
	people = models.IntegerField(db_index=True)
	price = models.IntegerField(db_index=True)


	def get_absolute_url(self):
		return reverse('voucher_detail_url', kwargs={"slug": self.slug})
	
	def get_update_url(self):
		return reverse('voucher_update_url', kwargs={'slug': self.slug})

	def get_delete_url(self):
		return reverse('voucher_delete_url', kwargs={'slug': self.slug})

	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = gen_slug(self.arrival_date)
		super().save(*args, **kwargs)


	def __str__(self):
		# return '{}'.format(self.surname)
		return self.arrival_date

	class Meta:
		ordering = ['arrival_date']

class Housing(models.Model):
	slug = models.SlugField(max_length=150, blank=True, unique=True)
	title = models.CharField(max_length=150, db_index=True)
	category = models.CharField(max_length=150, db_index=True)
	description = models.CharField(max_length=150, db_index=True)
	price = models.IntegerField(db_index=True)

	def get_absolute_url(self):
		return reverse('housing_detail_url', kwargs={"slug": self.slug})
	
	def get_update_url(self):
		return reverse('housing_update_url', kwargs={'slug': self.slug})

	def get_delete_url(self):
		return reverse('housing_delete_url', kwargs={'slug': self.slug})

	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = gen_slug(self.title)
		super().save(*args, **kwargs)


	def __str__(self):
		return self.title

	class Meta:
		ordering = ['title']
