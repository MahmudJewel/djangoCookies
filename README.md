# Cookies
Cookies, technically called the HTTP cookies, are a piece of information (stored in a file) that is stored on the client-side browser and is sent to the website server when requested for it.

## Set cookies
* set_cookie(cookie_name, value, max_age = None, expires = None) 
* here first part works as dictionary ==> ‘cookie_name’ : value

## Get cookies
* request.COOKIES['key']  #if none, it will show error.
Or
* request.COOKIES.get('key') #If none, no error.

## Delete Cookie
delete_cookie[‘key’]


# Coding:

views.py
```
def setcookies(request):
	resp = render(request,'home.html')
	resp.set_cookie('cookieName','Value')
	return resp

def getcookies(request):
	gt=request.COOKIES.get('cookieName')
	context={
		'gt':gt
	}
	return render(request, 'getcookies.html',context )

def deletecookies(request):
	resp = render(request,'deletecookies.html')
	resp.delete_cookie('cookieName')
	return resp
```




urls.py
```
***
***
***
urlpatterns =[
	path('setcookies', views.setcookies, name='setcookies'),
	path('getcookies', views.getcookies, name='getcookies'),
	path('delcookies', views.delcookies, name='delcookies'),
]
```

