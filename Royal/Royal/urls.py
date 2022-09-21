"""GSons URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path
from DOME import views as views
urlpatterns = [
    path('admin/',admin.site.urls),
   #BASIC 
    path('portal',views.portal),
    path('logout',views.logout), 
    path('validate',views.validate), 
    path('ltc',views.ltc),
    path('stocks',views.stocks),
   #INVOICING 
    path('newsale',views.newinvoice), 
    path('newinvsaving',views.invoice),
    path('showinvoices',views.tempinvlist),
    path('invlistgenerator',views.generateinvlist),
    path('editinvoice',views.editinv),
    path('inveditor',views.inveditor),
    path('updateinvsave',views.updateinvsave), 
   #PURCHASE CENTRE
    path('newpurchase',views.newpurchase),
    path('newpursaving',views.purchase),
    path('showpurchases',views.temppurlist),
    path('purlistgenerator',views.generatepurlist),
    path('editpurchase',views.editpur),
    path('pureditor',views.pureditor),
    path('updatepursave',views.updatepursave), 
   #EXPENSES
    path('newexpense',views.newexp),
    path('newexpsaving',views.expense), 
    path('showexpenses',views.tempexplist),
    path('explistgenerator',views.generateexplist),
    path('editexpense',views.editexp),
    path('expeditor',views.expeditor),
    path('updateexpsave',views.updateexpsave),
   #STOCK MANAGEMENT 
    path('newitemsaving',views.newitemsaving),
    path('itemcodes',views.showitemslist),
    path('delitem',views.delitem),
   #BILL EXPORTING
    path('exportinvoice',views.exportinv),
    path('invexporter',views.invexporter),
    path('billcreated',views.billing),
    re_path('$',views.login),
   
]
