from django.conf.urls import url
from django.shortcuts import render,redirect
from django.http import JsonResponse,Http404

import json
from hashids import Hashids

from .models import URLField

try:
    from keys import SALT_STRING
except ImportError:
    from keys import SALT_STRING

currVal = 1

# Create your views here.
def home_view(request):
	return render(request,"home.html")

def process_url(request):
	global currVal
	data = {
		'urlentered':request.GET.get('urlentered'),
		'choiceentered':request.GET.get('choiceentered',None)
	}
	responseData = {'status':None}
	if request.method == 'GET':
		urlEntered = data.get('urlentered',None)
		choiceEntered = data.get('choiceentered',None)
		if urlEntered:
			if choiceEntered:
				# process it to see if it can be made a short url
				try:
					urlObject = URLField.objects.get(shortURL=choiceEntered)
					responseData['status']=404
					responseData['error']='Choice not available!!'
				except Exception as e:
					urlObject = URLField.objects.create(originalURL=urlEntered,shortURL=choiceEntered)
					responseData['data']=json.dumps({'originalURL':urlObject.originalURL,'shortURL':urlObject.shortURL})
					responseData['status']=200
			else:
				# create a new hash
				hashids = Hashids(salt=SALT_STRING,min_length=4)
				hashid = hashids.encode(currVal)
				currVal += 1
				try:
					urlObject = URLField.objects.create(originalURL=urlEntered,shortURL=hashid)
					responseData['data']=json.dumps({'originalURL':urlObject.originalURL,'shortURL':urlObject.shortURL}) 
					responseData['status']=200
				except Exception as e:
					responseData['status']=500
					responseData['error']='Something went wrong while inserting data!!'
		else:
			responseData['error']='URL not provided!!' 
			responseData['status']=405
	else:
		responseData['status']=405
	return JsonResponse(data=responseData)

def redirect_url(request,key=None):
	try:
		urlObject = URLField.objects.get(shortURL=key)
		originalURL = urlObject.originalURL
		if 'http' not in originalURL:
			originalURL = 'https://'+originalURL
		return redirect(originalURL)
	except Exception as e:
		raise Http404
