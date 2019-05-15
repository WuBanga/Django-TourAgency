from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic import View
from django.shortcuts import redirect
from django.urls import reverse
from django.core.paginator import Paginator

from .models import *
from .utils import *
from .forms import *

from django.contrib.auth.mixins import LoginRequiredMixin


def info_list(request):
	customers = Customer.objects.all()
	paginator = Paginator(customers, 2)
	
	page_number = request.GET.get('page', 1)
	page = paginator.get_page(page_number)

	is_paginated = page.has_other_pages()
	if page.has_previous():
		prev_url = '?page={}'.format(page.previous_page_number())
	else:
		prev_url = ''

	if page.has_next():
		next_url = '?page={}'.format(page.next_page_number())
	else:
		next_url = ''

	context= {
		'page_object': page,
		'is_paginated': is_paginated,
		'next_url': next_url,
		'prev_url': prev_url
	}

	return render(request, 'main/index.html', context=context)


def tours_list(request):
	tours = Tour.objects.all()
	return render(request, 'main/tours_list.html', context={'tours': tours})


def pensions_list(request):
	pensions = Pension.objects.all()
	return render(request, 'main/pensions_list.html', context={'pensions': pensions})


def vouchers_list(request):
	# vouchers = Voucher.objects.all()
	# return render(request, 'main/vouchers_list.html', context={'vouchers': vouchers})

	vouchers = Voucher.objects.all()
	paginator = Paginator(vouchers, 2)
	
	page_number = request.GET.get('page', 1)
	page = paginator.get_page(page_number)

	is_paginated = page.has_other_pages()
	if page.has_previous():
		prev_url = '?page={}'.format(page.previous_page_number())
	else:
		prev_url = ''

	if page.has_next():
		next_url = '?page={}'.format(page.next_page_number())
	else:
		next_url = ''

	context= {
		'page_object': page,
		'is_paginated': is_paginated,
		'next_url': next_url,
		'prev_url': prev_url
	}

	return render(request, 'main/voucher_index.html', context=context)


def housings_list(request):
	housings = Housing.objects.all()
	return render(request, 'main/housing_list.html', context={'housings': housings})


class CustomerDetail(ObjectDetailMixin, View):
	model = Customer
	template = 'main/customers_detail.html'
	

class CustomerCreate(LoginRequiredMixin, ObjectCreateMixin, View):
	form_model = CustomerForm
	template = 'main/customer_create_form.html'
	raise_exception = True


class CustomerUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
	model = Customer
	form_model = CustomerForm
	template = 'main/customer_update_form.html'
	raise_exception = True


class CustomerDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
	model = Customer
	template = 'main/customer_delete_form.html'
	redirect_url = 'customers_list_url'
	raise_exception = True


class TourDetail(ObjectDetailMixin, View):
	model = Tour
	template = 'main/tour_detail.html'


class TourCreate(LoginRequiredMixin, ObjectCreateMixin, View):
	form_model = TourForm
	template = 'main/tour_create.html'
	raise_exception = True


class TourUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
	model = Tour
	form_model = TourForm
	template = 'main/tour_update_form.html'
	raise_exception = True


class TourDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
	model = Tour
	template = 'main/tour_delete_form.html'
	redirect_url = 'tours_list_url'
	raise_exception = True

class PensionDetail(ObjectDetailMixin, View):
	model = Pension
	template = 'main/pension_detail.html'
	

class PensionCreate(LoginRequiredMixin, ObjectCreateMixin, View):
	form_model = PensionForm
	template = 'main/pension_create_form.html'
	raise_exception = True


class PensionUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
	model = Pension
	form_model = PensionForm
	template = 'main/pension_update_form.html'
	raise_exception = True


class PensionDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
	model = Pension
	template = 'main/pension_delete_form.html'
	redirect_url = 'pensions_list_url'
	raise_exception = True


class VoucherDetail(ObjectDetailMixin, View):
	model = Voucher
	template = 'main/voucher_detail.html'
	

class VoucherCreate(LoginRequiredMixin, ObjectCreateMixin, View):
	form_model = VoucherForm
	template = 'main/voucher_create_form.html'
	raise_exception = True


class VoucherUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
	model = Voucher
	form_model = VoucherForm
	template = 'main/voucher_update_form.html'
	raise_exception = True


class VoucherDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
	model = Voucher
	template = 'main/voucher_delete_form.html'
	redirect_url = 'vouchers_list_url'
	raise_exception = True


class HousingDetail(ObjectDetailMixin, View):
	model = Housing
	template = 'main/housing_detail.html'
	

class HousingCreate(LoginRequiredMixin, ObjectCreateMixin, View):
	form_model = HousingForm
	template = 'main/housing_create_form.html'
	raise_exception = True


class HousingUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
	model = Housing
	form_model = HousingForm
	template = 'main/housing_update_form.html'
	raise_exception = True


class HousingDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
	model = Housing
	template = 'main/housing_delete_form.html'
	redirect_url = 'housings_list_url'
	raise_exception = True
