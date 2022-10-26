from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.http import JsonResponse
from django.http import HttpRequest
import json

# from gyaandweep.brhm.models import Shabdkosh
from brhm.models import Shabdkosh,Blogpage, Suktam , mantra, strotam, shlokas
# from brhm.models import Varnamala

# Create your views here.

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

def ShabdKosh(request):
    foo_list={}
    varn_list=[('ka','क'),('kh','ख'),('ga','ग'),('gh','घ'),('ca','च'),('ch','छ'),('ja','ज'),('jha','झ'),('ta','त'),('th','थ'),('da','द'),('dha','ध'),('na','न'),('pa','प'),('pha','फ'),('ba','ब'),('bha','भ'),('ma','म'),('ya','य'),('ra','र'),('la','ल'),('va','व'),('Sha','श'),('sh','ष'),('sa','स'),('ha','ह'),('a','अ'),('A','आ'),('i','इ'),('I','ई'),('u','उ'),('U','ऊ'),('R','ऋ'),('e','ए'),('ai','ऐ'),('o','ओ'),('au','औ')]
    for i in varn_list:
        foo_list[i] = Shabdkosh.objects.filter(varna=i[0]).values()
    return render(request, 'content/kosh.html',{'kosh_ins' : foo_list})   

# class KoshlListView(ListView):
#     model = Shabdkosh
#     template_name = '/content/kosh.html'
#     print("bhola")

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["kosh_json"] = json.dumps(list(Shabdkosh.objects.values()),default=str)
#         print(context)
#         return context

# def search_view(request):
#     return render(request, {})


        
def search_results(request):
    if is_ajax(request=request):
        res = None
        shabd = request.POST.get('shabd')
        search = Shabdkosh.objects.filter(meaning__startswith=shabd)
        if len(shabd)>0 and len(search)>0:
            data=[]
            for pos in search:
                item = {
                    'pk': pos.pk,
                    'meaning' : pos.meaning,
                    'sanskt' : pos.sanskt,
                    'eng' : pos.eng,
                    'gramgp' : pos.gramgp, 
                }
                data.append(item)
            res = data
        else:
            res = "No words found..."
        return JsonResponse({'data': res})
    return JsonResponse({})


    #this python function is responsible for blogs page.

def Blog(request):
    # if request.user.is_anonymous:
    #    return redirect("/login")
    blog_list=Blogpage.objects.values().order_by('date_uploaded')  
    # if request.method == 'POST':
    #    hash = request.POST.get('hashtag')
    #    hashlist = Blogpage.objects.values().filter(hashtag__contains=hash)
    #    blog_list=hashlist
    return render(request, 'content/blog.html' , {'blog' : blog_list})

def Bloghash(request):
    if is_ajax(request=request):
        res = None
        hash = request.GET.get('hashtag')
        hashed = Blogpage.objects.filter(hashtag__contains=hash)
        print(hashed)
        data=[]
        for pos in hashed:
            item = {
                'pk': pos.pk,
                'hashtag' : pos.hashtag,
                'title' : pos.title,
                'desc' : pos.desc,
                'img' : str(pos.img), 
                'link' : pos.link,
                'read_time' : pos.read_time,
                'author_name' : pos.author_name,
                'date_uploaded' : pos.date_uploaded,
            }
            data.append(item)
            res = data
        return JsonResponse({'data': res})
    return JsonResponse({})

def Auvid(request):
    # if request.user.is_anonymous:
    #     return redirect("/login")
    return render(request, 'content/auvid.html')

# These functions are built for rendering content in articles page. Need to be made dynamic in future.

def Showblog(request):
    return render(request, 'content/showblog.html')
    
def Vedas(request):
    return render(request, 'Blogfull/Vedas.html')    

def shivavtr(request):
    return render(request, 'Blogfull/shivavtr.html')  

def Vishnu(request):
    return render(request, 'Blogfull/vishnu.html')       

def kundalini(request):
    return render(request, 'Blogfull/kundalini.html')     

def Navdurga(request):
    return render(request, 'Blogfull/navdurga.html') 

def Nadis(request):
    return render(request, 'Blogfull/nadis.html')    

def Edufath(request):
    return render(request, 'Blogfull/edufath.html')          

def Prana(request):
    return render(request, 'Blogfull/prana.html')   

def Lokas(request):
    return render(request, 'Blogfull/lokas.html') 

def Kosha(request):
    return render(request, 'Blogfull/kosha.html')

def Gurukul(request):
    return render(request, 'Blogfull/gurukul.html')   
    
def Yogasutra(request):
    return render(request, 'Blogfull/yogasutra.html')

def Swastika(request):
    return render(request, 'Blogfull/swastika.html')

def Vishnunama(request):
    return render(request, 'Blogfull/vishnamval.html')    

def Darshana(request):
    return render(request, 'Blogfull/darshana.html')      

def Deepawali(request):
    return render(request, 'Blogfull/deepavali.html')    

def Eclipse(request):
    return render(request, 'Blogfull/eclipse.html')        


# These functions are built for rendering list of content in chants page. Need to be made dynamic in future.     

def Sukt(request):
    name_set = Suktam.objects.values('suktam').distinct()
    return render(request, 'Chantfull/suktam.html', {'name_set' : name_set})    


def Strot(request):
    name_set = strotam.objects.values('strota').distinct()
    return render(request, 'Chantfull/strotam.html', {'name_set' : name_set})


def Mantr(request):
    name_set = mantra.objects.values('mantra').distinct()
    return render(request, 'Chantfull/mantra.html', {'name_set' : name_set})

# This section is for Suktams


def Panch(request):
    panch_list = Suktam.objects.filter(suktam__startswith="Panch").order_by('id')
    return render(request, 'chantfull/Panch.html', {'panch' : panch_list})

def Sri(request):
    sri_list = Suktam.objects.filter(suktam__startswith="Shri").order_by('id')
    return render(request, 'chantfull/Srisukt.html', {'srisubsukt' : sri_list})

def Kseth(request):
    kseth_list = Suktam.objects.filter(suktam__startswith="Kshetrapati").order_by('id')
    return render(request, 'chantfull/kseth.html', {'ksetrsubsukt' : kseth_list})    

def Durga(request):
    durga_list = Suktam.objects.filter(suktam__startswith="Durga").order_by('id')
    return render(request, 'chantfull/durgasukt.html', {'durgasuktam' :durga_list})     
        


# This section is for Shlokas

def Shlok(request):
   shlk_set = shlokas.objects.filter(shloka__startswith="Ganesh").order_by('id')
   return render(request, 'Chantfull/ganeshshlk.html', {'ganeshshlk' : shlk_set})

def Chalisa(request):
   hanu_set = shlokas.objects.filter(shloka__startswith="Hanuman").order_by('id')
   return render(request, 'Chantfull/hanumanchalisa.html', {'hanuchalisa' : hanu_set})

def Laksharti(request):
   laksh_set = shlokas.objects.filter(shloka__startswith="Lakshmi").order_by('id')
   return render(request, 'Chantfull/lakshmiaarti.html', {'lakshmiarti' : laksh_set})
   
def Mornpray(request):
    return render(request, 'chantfull/mornprayer.html')      

# This section is for Mantras

def gana(request):
    gana_list = mantra.objects.filter(mantra__startswith="Ganesh").order_by('id')
    return render(request, 'chantfull/ganatharv.html', {'ganatharvashsm' : gana_list}) 

def gayamant(request):
    return render(request, 'chantfull/gayatrimant.html')

def kshamamant(request):
    return render(request, 'chantfull/kshamant.html')

def lakshmimant(request):
    return render(request, 'chantfull/lakshmimant.html')

def saraswatimant(request):
    return render(request, 'chantfull/saraswatimantra.html')        

# This section is for Strotam    

def shvtand(request):
    tand_list = strotam.objects.filter(strota__startswith="Shiva").order_by('id')
    return render(request, 'chantfull/shivtand.html', {'shivatandavam' : tand_list}) 

def kanaka(request):
    kana_list = strotam.objects.filter(strota__startswith="Kanakadhara").order_by('id')
    return render(request, 'chantfull/kanaka.html', {'kanakadharam' : kana_list})     

def srwtstrt(request):
    swstrt_list = strotam.objects.filter(strota__startswith="Saraswati Strotam").order_by('id')
    return render(request, 'chantfull/srwtstrt.html', {'srswtstrtm' : swstrt_list})      

def mhlkasht(request):
    mhlkash_list = strotam.objects.filter(strota__startswith="Mahalakshmi Ashtakam").order_by('id')
    return render(request, 'chantfull/lakshmiastkm.html', {'lakshmiashtakam' : mhlkash_list})    

def lkshsupra(request):
    lkshsup_list = strotam.objects.filter(strota__startswith="Lakshmi Suprabhatam").order_by('id')
    return render(request, 'chantfull/lakshmisupra.html', {'lakshmisuprabhatam' : lkshsup_list})        

def gurustrt(request):
    gurust_list = strotam.objects.filter(strota__startswith="Guru Strotam").order_by('id')
    return render(request, 'chantfull/gurustrotam.html', {'gurustrotam' : gurust_list})       

def ashlakstrt(request):
    ashtlkst_list = strotam.objects.filter(strota__startswith="Ashtalakshmi Strotam").order_by('id')
    return render(request, 'chantfull/ashtalakshmi.html', {'ashlakshmistrt' : ashtlkst_list})
