#coding:utf-8
'''
Created on 2012-11-8
@author: zhou
'''
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
import Image
import os 
import time
import urllib2
import uuid
from beansblog import settings
from beansblog.admin.models import Blog
from beansblog.admin.forms import ContactForm
@csrf_exempt
def post_blog(request):

	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			blog = Blog(title=cd['title'],content=cd['content'])
			blog.save()

	return HttpResponseRedirect('/show_articles/')
	
def show_articles(request):
	
	if request.method == 'GET':
	   articles = Blog.objects.all()

	return render_to_response('show_articles.html',{'articles':articles})

def __myuploadfile(fileObj, source_pictitle, source_filename, fileorpic='pic'):
	
	'''
	一个共用的上传文件处理
	'''
	if fileObj:
		filename = fileObj.name.decode('utf-8','ignore')
		fileExt = filename.split('.')[1]
		file_name = str(uuid.uuid1())
		subfolder=time.strftime("%Y%m")
		path=str('/home/zhou/media/'+ file_name + '.' + fileExt)

		if fileExt.lower() in ('jpg','jpeg','bmp','gif','png','rar','doc','docx','zip','pdf','txt','swf','wmv'):
			phisypath = path
			destination = open(phisypath,'wb+')
			for chunk in fileObj.chunks():
				destination.write(chunk)
			destination.close()

			if fileorpic == 'pic':
				if fileExt.lower() in ('jpg','jpeg','bmp','gif','png'):
					im = Image.open(phisypath)
					im.thumbnail((720,720))
					im.save(phisypath)

			real_url = '/static/' + file_name + '.' + fileExt
			myresponse =  "{'original':'%s','url':'%s','title':'%s','state':'%s'}" % (source_filename, real_url, source_pictitle, 'SUCCESS')

	return myresponse


@csrf_exempt
def ueditor_ImgUp(request):
	'''
	上传图片
	'''
	fileObj = request.FILES.get('upfile',None)
	source_pictitle = request.POST.get('pictitle','')
	source_filename = request.POST.get('fileName','')
	response = HttpResponse()
	myresponse = __myuploadfile(fileObj, source_pictitle, source_filename,'pic')
	response.write(myresponse)
	return response



