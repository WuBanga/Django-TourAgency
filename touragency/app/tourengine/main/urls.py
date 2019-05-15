from django.urls import path

from .views import *

urlpatterns = [
	path('', info_list, name='customers_list_url'),
	path('customer/create/', CustomerCreate.as_view(), name='customer_create_url'),
	path('customer/<str:slug>/', CustomerDetail.as_view(), name='customers_detail_url'),
	path('customer/<str:slug>/update/', CustomerUpdate.as_view(), name='customer_update_url'),
	path('customer/<str:slug>/delete/', CustomerDelete.as_view(), name='customer_delete_url'),
	path('tours/', tours_list, name='tours_list_url'),
	path('tour/create/', TourCreate.as_view(), name='tour_create_url'),
	path('tour/<str:slug>/', TourDetail.as_view(), name='tour_detail_url'),
	path('tour/<str:slug>/update/', TourUpdate.as_view(), name='tour_update_url'),
	path('tour/<str:slug>/delete/', TourDelete.as_view(), name='tour_delete_url'),
	path('pensions/', pensions_list, name='pensions_list_url'),
	path('pension/create/', PensionCreate.as_view(), name='pension_create_url'),
	path('pension/<str:slug>/', PensionDetail.as_view(), name='pension_detail_url'),
	path('pension/<str:slug>/update/', PensionUpdate.as_view(), name='pension_update_url'),
	path('pension/<str:slug>/delete/', PensionDelete.as_view(), name='pension_delete_url'),
	path('vouchers/', vouchers_list, name='vouchers_list_url'),
	path('voucher/create/', VoucherCreate.as_view(), name='voucher_create_url'),
	path('voucher/<str:slug>/', VoucherDetail.as_view(), name='voucher_detail_url'),
	path('voucher/<str:slug>/update/', VoucherUpdate.as_view(), name='voucher_update_url'),
	path('voucher/<str:slug>/delete/', VoucherDelete.as_view(), name='voucher_delete_url'),
	path('housing/', housings_list, name='housings_list_url'),
	path('housing/create/', HousingCreate.as_view(), name='housing_create_url'),
	path('housing/<str:slug>/', HousingDetail.as_view(), name='housing_detail_url'),
	path('housing/<str:slug>/update/', HousingUpdate.as_view(), name='housing_update_url'),
	path('housing/<str:slug>/delete/', HousingDelete.as_view(), name='housing_delete_url'),

]