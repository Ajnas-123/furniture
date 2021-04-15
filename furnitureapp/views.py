from django.shortcuts import render
from furnitureapp.models import form_tb
from django.http import HttpResponseRedirect



# Create your views here.
def disp(request):
	return render(request,'index.html')

def abt(request):
	return render(request,'about.html')

def blog(request):
	return render(request,'blog.html')

def cntct(request):
	return render(request,'contact.html')


def login(request):
	return render(request,'log1.html')


def register(request):
	return render(request,'register.html')

def singl(request):
	return render(request,'single.html')



def register(request):
	if request.method=='POST':
		ftname=request.POST['fname']
		
		uemail=request.POST['emlname']
		upass=request.POST['passname']

		udob=request.POST['dobname']
		uphon=request.POST['numname']
		uaddr=request.POST['addrname']
		ucity=request.POST['ctyname']
		ustate=request.POST['statname']
		ucountry=request.POST['cntryname']
		query=form_tb(firstname=ftname,email=uemail,password=upass,dob=udob,phone=uphon,address=uaddr,city=ucity,state=ustate,country=ucountry)
		query.save()
		return render(request,"index.html")
	else:
		return render(request,"register.html")

def log(request):
	if request.method=='POST':
		ftname=request.POST['fname']
		upass=request.POST['passname']
		query=form_tb.objects.all().filter(firstname=ftname,password=upass)
		if query:
			for x in query:
				request.session['userid']=x.id
				request.session['username']=x.firstname



				

				
				



				uid=request.session['userid']
			return render(request,"index.html",{'msg':"login successful"})
		else:
			return render(request,"log1.html",{'msg':"incorrect username or passsword"})


	else:
		return render(request,"log1.html")


def logout(request):
	if request.session.has_key('userid'):

		del request.session['userid']
	return render(request,"index.html")


def view(request):
	uid=request.session['userid']
	query=form_tb.objects.all().filter(id=uid)
	return render(request,"table.html",{'queryset':query})


def update(request):
	if request.method=='GET':
		uid=request.GET['userid']
		query=form_tb.objects.all().filter(id=uid)
		return render(request,"update.html",{'queryset':query})




def savechanges(request):
	if request.method=='POST':
		ftname=request.POST['fname']
		userid=request.POST['uid']
		
		uemail=request.POST['emlname']
		

		udob=request.POST['dobname']
		uphon=request.POST['numname']
		uaddr=request.POST['addrname']
		ucity=request.POST['ctyname']
		
		query=form_tb.objects.filter(id=userid).update(firstname=ftname,email=uemail,dob=udob,phone=uphon,address=uaddr,city=ucity)
		
		return HttpResponseRedirect("/view/")
	else:
		return HttpResponseRedirect("/view/")








