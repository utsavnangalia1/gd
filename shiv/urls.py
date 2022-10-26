"""gyaandweep URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from shiv import views
from vish import views as view1
from brhm import views as view2
from django.conf import settings
from django.conf.urls.static import static
# from brhm.views import KoshlListView



urlpatterns = [

    #All paths lead to home and then to dhyana

    path("", views.index, name='home'),
    path("wallqa/",views.Wallqna, name='WallQnA'),
    path("vision/",views.Vision, name='Vision'),
    path("setting/",views.Setting, name='Setting'),
    path("Analytics/",views.Analytics, name='Analytics'),
    path("community/",view1.Community, name='Community'),
    path("kosh/",view2.ShabdKosh, name='Shabdkosh'),
    path("kosh/search/",view2.search_results,name='kosh1-search'),

    #All paths lead to blogs and then to nirvana

    path("blog/",view2.Blog, name='Blog'),
    path("blog/hashtag/",view2.Bloghash, name='hashtag-filter'),
    path("blog/showblog/",view2.Showblog, name='Showblog'),
    path("blog/gurukul/",view2.Gurukul, name='Gurukul'),
    path("blog/Vedas/",view2.Vedas, name='Vedas'),
    path("blog/shivavtr/",view2.shivavtr, name='ShivAvatar'),
    path("blog/vishnu/",view2.Vishnu, name='Vishnuavtr'),
    path("blog/kundalini/",view2.kundalini, name='Kundalini'),
    path("blog/navdurga/",view2.Navdurga, name='Navdurga'),
    path("blog/nadis/",view2.Nadis, name='Nadis'),
    path("blog/edufath/",view2.Edufath, name='Gurus'),
    path("blog/prana/",view2.Prana, name='Prana'),
    path("blog/lokas/",view2.Lokas, name='Lokas'),
    path("blog/kosha/",view2.Kosha, name='Koshas'),
    path("blog/yogasutra/",view2.Yogasutra, name='Yoga Sutra'),
    path("blog/swastika/",view2.Swastika, name='Swastika'),
    path("blog/vishnamval/",view2.Vishnunama, name='16 Vishnu Names'),
    path("blog/darshana/",view2.Darshana, name='Indian philosophy'),
    path("blog/deepavali/",view2.Deepawali, name='Deepavali'),
    path("blog/eclipse/",view2.Eclipse, name='Eclispse'),
    path("chants/",view2.Auvid, name='Auvid'),
    path("login/",views.LoginUser, name='Login'),
    path("logout/",views.LogoutUser,name='Logout'),

    # All paths for redirecting to teh list of chants
    path("chants/suktam/",view2.Sukt, name='Suktam'),
    path("chants/strotam/",view2.Strot, name='Strotam'),
    # path("chants/shlokas/",view2.Shlok, name='Shlokas'),
    path("chants/mantra/",view2.Mantr, name='Mantras'),


    # path("kosh/",KoshlListView.as_view(),name='kosh-search'),
     #All paths lead to chants and then to samadhi,this is for Suktam Section
   
    path("suktam/panch-bhuta-suktam/",view2.Panch, name='Panch-bhuta-sukta'),
    path("suktam/sri-suktam/",view2.Sri, name='Sri Suktam'),
    path("suktam/ksetrapati-suktam/",view2.Kseth, name='Ksetrapati Suktam'),
    path("suktam/durga-suktam/",view2.Durga, name='Durga Suktam'),

    #All paths lead to chants and then to samadhi, this for for Mantras Section

    path("mantra/ganesh-atharva/",view2.gana, name='Ganesh Atharvashirsham'),
    path("mantra/gayatri-mantra/",view2.gayamant, name='Gayatri Mantra'),
    path("mantra/kshama-mantra/",view2.kshamamant, name='Kshama Mantra'),
    path("mantra/saraswati-mantra/",view2.saraswatimant, name='Lakshmi Mantra'),
    path("mantra/lakshmi-mantra/",view2.lakshmimant, name='Lakshmi Mantra'),

    #All paths lead to chants and then to samadhi, this for for Strotam Section
    path("strotam/shiva-tandava/",view2.shvtand, name='Shiva Tandava Strotam'),
    path("strotam/kanakadhara-strotam/",view2.kanaka, name='Kanakadhara Strotam'),
    path("strotam/saraswati-strotam/",view2.srwtstrt, name='Saraswati Strotam'),
    path("strotam/mahalakshmi-ashtakam/",view2.mhlkasht, name='Mahalakshmi Ashtakam'),
    path("strotam/lakshmi-suprabhatam/",view2.lkshsupra, name='Lakshmi Suprabhatam'),
    path("strotam/guru-strotam/",view2.gurustrt, name='Guru Strotam'),
    path("strotam/ashtalakshmi-strotam/",view2.ashlakstrt, name='Ashtalakshmi Strotam'),

    #All paths lead to chants and then to samadhi, this for for Shlokas Section

    path("shlokas/ganesh-shloka/",view2.Shlok, name='Ganesh Shlokas'),
    path("shlokas/hanuman-chalisa/",view2.Chalisa, name='Hanuman Chalisa'),
    path("shlokas/lakshmi-aarti/",view2.Laksharti, name='Lakshmi Aarti'),
    path("shlokas/morning-prayer/",view2.Mornpray, name='Morning Prayer')
] 