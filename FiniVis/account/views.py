from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import LoginForm


def user_login(request): 
	if request.method == 'POST':
		
		form = LoginForm(request.POST)
		if form.is_valid():

			cd = form.cleaned_data
			user = authenticate(username=cd['username'],
								password=cd['password'])
			
			if user is not None:
				if user.is_active:
					login(request, user)
					return HttpResponse('Authenticated successfully')

				else:
					return HttpResponse('Disabled account')

			else:
				return HttpResponse('Invalid Login')
	
	else:
		form = loginForm()

	return render(request, 'account/login.html', {'form': form })