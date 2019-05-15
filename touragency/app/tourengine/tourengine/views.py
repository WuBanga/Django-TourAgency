from django.shortcuts import redirect

def redirect_main(requesst):
	return redirect('customers_list_url', permanent=True)