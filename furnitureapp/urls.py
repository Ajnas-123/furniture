from django.urls import path
from furnitureapp import  views

urlpatterns = [

	
	path('',views.disp),
	path('about/',views.abt),
	path('blog/',views.blog),
	path('contact/',views.cntct),
	path('login/',views.log),
	path('register/',views.register),

	path('single/',views.singl),
	path('logout/',views.logout),
	path('view/',views.view),
	path('update/',views.update),
	path('savechanges/',views.savechanges),





	

]