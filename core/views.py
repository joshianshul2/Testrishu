from django.db.models import Q, Count
from django.shortcuts import render, get_object_or_404
from rest_framework import generics
from rest_framework.response import Response
# from .serializers import JournalSerializer
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.views.generic import ListView,TemplateView
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.views.decorators.cache import cache_control
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.db.models import Sum,Avg
import bcrypt
from django.utils.decorators import method_decorator
from .models import User,UserManager,PropertyMaster,Property_TypeMaster,TypeMaster,AvgMaster
import requests
import pdb
import operator
from django.db.models import F
import random
import re
from django.db.models import Q, Count
from django.shortcuts import render, get_object_or_404
from rest_framework import generics
from rest_framework import generics
from rest_framework.response import Response
from django.urls import reverse
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'index2.html')

def register(request):
    errors = User.objects.validator(request.POST)
    if len(errors):
        for tag, error in errors.items():
            messages.error(request, error, extra_tags=tag)
        return redirect('/')

    # hashed_password = bcrypt.hashpw(request.POST['password'].encode('utf-8'), bcrypt.gensalt())
    # password= User.objects.create()
    user = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], password=request.POST['password'], email=request.POST['email'])
    user.save()
    request.session['id'] = user.id
    return redirect('/success')

def Alert(request):
    qs = AvgMaster.objects.all()
    # qs = filter2(request)

    # if request.method == 'POST':
    #     view_percentage = request.GET.get('view_percentage')
    #     view_state = request.GET.get('view_state')
    #     print(view_state, view_percentage)
    #     print("Rishu")
    # return render(request,'bootstrap_form.html')
    if request.method == 'GET':
        print("Anjali Dubey")
        view_percentage = request.GET.get('view_percentage')
        view_state = request.GET.get('view_state')
        print(view_state, view_percentage)
        # # qws = PropertyMaster.objects.get(state='view_state')
        # # print(qws)
        # qr = PropertyMaster.objects.values('state','county').annotate(Aj=Sum('price')/Sum('acres')).distinct()
        #     # .annotate(Aj=Sum('price')/Sum('acres')).distinct()
        # # query = PropertyMaster.objects.filter('student__state' = request.user)
        # # print(qr)
        # # # ab = AvgMaste.objects.create()
        # # # print(qr[Aj])
        # for course in qr:
        #     # qw = AvgMaster.objects.create(state=course['state'],NetPrAr=course['Aj'])
        #     print(course["state"],course["county"],course["Aj"])
        # # qw.save()
        # # # a=view_state
        # # for i in qr:
        # #     a.append(i)
        # #     print(i.values())
        # print(a)
        if PropertyMaster.objects.filter(state=request.GET.get('view_state')).exists():
            qw = PropertyMaster.objects.filter(state=request.GET.get('view_state'))[0]
            # if (bcrypt.checkpw(request.POST['login_password'].encode('utf-8'), user.password.encode('utf-8'))):
            if (request.GET.get('view_state') == qw.state):
                # print(qw.state)
                print("Rishu")
                print(view_state)
                qr = PropertyMaster.objects.filter(state=view_state).annotate(
                    Aj=Sum('price') / Sum('acres')).distinct().values()
                ar = list(PropertyMaster.objects.filter(state=view_state).values('state', 'county').distinct())
                print(ar)
                rishu = 1 - float(view_percentage) / 100
                for course in qr:
                    qw = AvgMaster.objects.create(state=course['state'], county=course['county'], NetPrAr=course['Aj'],
                                                  Rate=course['price'] / course['acres'], UserPercentage=rishu,
                                                  FinaleValue=rishu * course['Aj'],
                                                  accountId=course['accountId'], acres=course['acres'],
                                                  adTargetingCountyId=course['adTargetingCountyId'],
                                                  address=course['address'], baths=course['baths'],
                                                  beds=course['beds'], brokerCompany=course['brokerCompany'],
                                                  brokerName=course['brokerName'],
                                                  Url=course['Url'],
                                                  city=course['city'],
                                                  cityID=course['cityID'],
                                                  companyLogoDocumentId=course['companyLogoDocumentId'],
                                                   countyId=course['countyId'],
                                                  description=course['description'], hasHouse=course['hasHouse'],
                                                  hasVideo=course['hasVideo'],
                                                  hasVirtualTour=course['hasVirtualTour'],
                                                  imageCount=course['imageCount'], latitude=course['latitude'],
                                                  longitude=course['longitude'],
                                                  imageAltTextDisplay=course['imageAltTextDisplay'],
                                                  isHeadlineAd=course['isHeadlineAd'], types=''.join(course['types']),
                                                  lwPropertyId=course['lwPropertyId'], isALC=course['isALC'],
                                                     price=course['price'],
                                                  status=course["status"],
                                                   zip=course['zip']
                                                  )
                    print(course["state"], course["county"], course["Aj"], course["Rate"])
                    akp = AvgMaster.objects.filter(Rate__gte=F('FinaleValue'),UserPercentage__lte=abs(rishu)).values()

                # akp = AvgMaster.objects.filter(Rate__gte=F('FinaleValue')).values()
                print(akp)
                print("Zakir Khan")
                qs = filter2(request)
                for i in akp:
                    print("ANshul",i["state"], i["county"], i["Rate"], i["FinaleValue"])
                # qw.save()
                # # a=view_state
                # for i in qr:
                #     a.append(i)
                #     print(i.values())
                # print(a)

            else:
                print("Anshul")
    anji = AvgMaster.objects.all()
    akp = filter(request)
    context = {
                 'aj': akp,
        # 'status': StatusMaster.objects.all()
                }
    return render(request, "rishu.html", context)

def show(request):

    a=[]
    qs = PropertyMaster.objects.all()
    qs = filter(request)
    auths = PropertyMaster.objects.order_by('acres')
    ordered = sorted(auths, key=operator.attrgetter('acres'))
    if request.method == 'GET':
        for row in PropertyMaster.objects.all().reverse():
            print("AJ")
            if PropertyMaster.objects.filter(lwPropertyId=row.lwPropertyId).count() > 1:
                row.delete()
        view_percentage = request.GET.get('view_percentage')
        view_state = request.GET.get('view_state')
        print(view_state,view_percentage)
        # # qws = PropertyMaster.objects.get(state='view_state')
        # # print(qws)
        # qr = PropertyMaster.objects.values('state','county').annotate(Aj=Sum('price')/Sum('acres')).distinct()
        #     # .annotate(Aj=Sum('price')/Sum('acres')).distinct()
        # # query = PropertyMaster.objects.filter('student__state' = request.user)
        # # print(qr)
        # # # ab = AvgMaste.objects.create()
        # # # print(qr[Aj])
        # for course in qr:
        #     # qw = AvgMaster.objects.create(state=course['state'],NetPrAr=course['Aj'])
        #     print(course["state"],course["county"],course["Aj"])
        # # qw.save()
        # # # a=view_state
        # # for i in qr:
        # #     a.append(i)
        # #     print(i.values())
        # print(a)
        if PropertyMaster.objects.filter(state=request.GET.get('view_state')).exists():
            qw = PropertyMaster.objects.filter(state=request.GET.get('view_state'))[0]
            # if (bcrypt.checkpw(request.POST['login_password'].encode('utf-8'), user.password.encode('utf-8'))):
            if (request.GET.get('view_state') == qw.state):
                # print(qw.state)
                print("Rishu")
                print(view_state)
                qr = PropertyMaster.objects.filter(state=view_state).annotate(Aj=Sum('price') / Sum('acres')).distinct().values()
                ar =list(PropertyMaster.objects.filter(state=view_state).values('state','county',).distinct())
                # print(ar)
                rishu = 1- float(view_percentage)/100
                for course in qr:
                    qw = AvgMaster.objects.create(state=course['state'],county=course['county'],NetPrAr=course['Aj'],Rate=course['price'] / course['acres'],UserPercentage=rishu,FinaleValue=rishu*course['Aj'])
                    print(course["state"], course["county"], course["Aj"],course["Rate"])
                akp = AvgMaster.objects.filter(Rate__lt=F('FinaleValue')).values()
                print("Zakir Khan")
                qs = filter(request)
                for i in akp:
                    print(i["state"], i["county"], i["Rate"],i["FinaleValue"])
                # qw.save()
                # # a=view_state
                # for i in qr:
                #     a.append(i)
                #     print(i.values())
                # print(a)

            else:
                print("Anshul")
    anji = AvgMaster.objects.all()
    context = {
        'queryset': qs,
        'aj' : anji,
        # 'status': StatusMaster.objects.all()
        }
    return render(request,"bootstrap_form.html",context)

def login(request):
    if User.objects.filter(email=request.POST.get('login_email')).exists():
        user = User.objects.filter(email=request.POST.get('login_email'))[0]
        # if (bcrypt.checkpw(request.POST['login_password'].encode('utf-8'), user.password.encode('utf-8'))):
        if (request.POST.get('login_password') == user.password):
            request.session['id'] = user.id
            if request.POST.get('next',None) :
                print("Dipu")
                return  HttpResponseRedirect(request.GET['next'])
            return redirect('/show')
    return redirect('/')

def success(request):
    user = User.objects.get(id=request.session['id'])
    context = {
        "user": user
    }
    # job(request)

    return render(request, 'test111.html', context)

def set_password(self, pw):
    pwhash = bcrypt.hashpw(pw.encode('utf8'), bcrypt.gensalt())
    self.password_hash = pwhash.decode('utf8') # decode the hash to prevent is encoded twice

def is_valid_queryparam(param):
    return param != '' and param is not None

def filter(request):
    qs = PropertyMaster.objects.all()
    wq = AvgMaster.objects.all()
    category = PropertyMaster.objects.all()
    title_contains_query = request.GET.get('title_contains')
    id_exact_query = request.GET.get('id_exact')
    title_or_author_query = request.GET.get('title_or_author')
    view_count_min = request.GET.get('view_count_min')
    view_count_max = request.GET.get('view_count_max')
    date_min = request.GET.get('date_min')
    date_max = request.GET.get('date_max')
    view_acres = request.GET.get('view_acres')
    status = request.GET.get('status')
    title2_contains_query = request.GET.get('title2_contains')
    view_state = request.GET.get('view_state')
    types = request.GET.get('types')
    view_percentage = request.GET.get('view_percentage')

    #
    # if is_valid_queryparam(title_contains_query):
    #     qs = qs.filter(city__icontains=title_contains_query)
    #
    # elif is_valid_queryparam(id_exact_query):
    #     qs = qs.filter(id=id_exact_query)
    #
    # elif is_valid_queryparam(view_state):
    #     qs = qs.filter(Q(city__icontains=view_state)
    #                    | Q(state=view_state)
    #                    ).distinct()
    if is_valid_queryparam(title_contains_query):
        qs = qs.filter(Q(city__icontains=title_contains_query)
                       | Q(state__icontains=title_contains_query) | Q(county__icontains=title_contains_query)
                       ).distinct()

    elif is_valid_queryparam(id_exact_query):
        qs = qs.filter(id=id_exact_query)

    elif is_valid_queryparam(title_or_author_query):
        qs = qs.filter(Q(city__icontains=title_or_author_query)
                       | Q(state__name__icontains=title_or_author_query) | Q(county__icontains=title_contains_query)
                       ).distinct()


    if is_valid_queryparam(view_count_min):
        qs = qs.filter(price__gte=view_count_min)

    if is_valid_queryparam(view_count_max):
        qs = qs.filter(price__lt=view_count_max+"1")

    if is_valid_queryparam(date_min):
        qs = qs.filter(publish_date__gte=date_min)

    if is_valid_queryparam(status) and status != 'Choose...':
        qs = qs.filter(status=status)

    if is_valid_queryparam(date_max):
        qs = qs.filter(publish_date__lt=date_max)

    if is_valid_queryparam(view_acres):
        qs = qs.filter(acres__gte=view_acres)

    if is_valid_queryparam(types):
        qs = qs.filter(types__icontains=types)

    elif is_valid_queryparam(id_exact_query):
        qs = qs.filter(id=id_exact_query)

    elif is_valid_queryparam(types):
        qs = qs.filter(Q(types__icontains=types)).distinct()



    # if is_valid_queryparam(view_state):
    #     qs = qs.filter(state__icontains=view_state)
    #
    # elif is_valid_queryparam(id_exact_query):
    #     qs = qs.filter(id=id_exact_query)

    # elif is_valid_queryparam(types):
    #     qs = qs.filter(Q(state__icontains=view_state)).distinct()
    #
    # if is_valid_queryparam(view_percentage):
    #     wq = wq.filter(__gte=view_percentage)
    #

    # if is_valid_queryparam(acres) :
    #     qs = qs.filter(acres__values=acres)
    # export_users_csv2(request,qs)
    return qs

def filter2(request):
    qs = AvgMaster.objects.all()
    category = PropertyMaster.objects.all()
    title_contains_query = request.GET.get('title_contains')
    id_exact_query = request.GET.get('id_exact')
    title_or_author_query = request.GET.get('title_or_author')
    view_count_min = request.GET.get('view_count_min')
    view_count_max = request.GET.get('view_count_max')
    date_min = request.GET.get('date_min')
    date_max = request.GET.get('date_max')
    view_acres = request.GET.get('view_acres')
    status = request.GET.get('status')
    title2_contains_query = request.GET.get('title2_contains')
    view_state = request.GET.get('view_state')
    types = request.GET.get('types')
    view_percentage = request.GET.get('view_percentage')


    if is_valid_queryparam(title_contains_query):
        qs = qs.filter(city__icontains=title_contains_query)

    elif is_valid_queryparam(id_exact_query):
        qs = qs.filter(id=id_exact_query)

    elif is_valid_queryparam(title_or_author_query):
        qs = qs.filter(Q(city__icontains=title_or_author_query)).distinct()
                       # | Q(author__name__icontains=title_or_author_query



    if is_valid_queryparam(view_count_min):
        qs = qs.filter(price__gte=view_count_min)

    if is_valid_queryparam(view_count_max):
        qs = qs.filter(price__lt=view_count_max+"1")

    if is_valid_queryparam(date_min):
        qs = qs.filter(publish_date__gte=date_min)

    if is_valid_queryparam(status) and status != 'Choose...':
        qs = qs.filter(status=status)

    if is_valid_queryparam(date_max):
        qs = qs.filter(publish_date__lt=date_max)

    if is_valid_queryparam(view_acres):
        qs = qs.filter(acres__gte=view_acres)

    if is_valid_queryparam(types):
        qs = qs.filter(types__icontains=types)

    elif is_valid_queryparam(id_exact_query):
        qs = qs.filter(id=id_exact_query)

    elif is_valid_queryparam(types):
        qs = qs.filter(Q(types__icontains=types)).distinct()



    # if is_valid_queryparam(view_state):
    #     qs = qs.filter(state__icontains=view_state)
    #
    # elif is_valid_queryparam(id_exact_query):
    #     qs = qs.filter(id=id_exact_query)

    # elif is_valid_queryparam(types):
    #     qs = qs.filter(Q(state__icontains=view_state)).distinct()
    #
    # if is_valid_queryparam(view_percentage):
    #     wq = wq.filter(__gte=view_percentage)
    #

    # if is_valid_queryparam(acres) :
    #     qs = qs.filter(acres__values=acres)
    export_users_csv2(request,qs)
    return qs

def infinite_filter(request):
    limit = request.GET.get('limit')
    offset = request.GET.get('offset')
    return PropertyMaster.objects.all()[int(offset): int(offset) + int(limit)]


def is_there_more_data(request):
    offset = request.GET.get('offset')
    if int(offset) > PropertyMaster.objects.all().count():
        return False
    return True

@cache_control(no_cache=True, must_revalidate=True)
def logout_view(request):
    # logout(request)
    return render(request,'index2.html')
