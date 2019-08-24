from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from .forms import SignUpForm
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from .forms import ProfileForm
from .forms import ContactForm, ReviewForm
from .models import Restraunt
from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.template.loader import get_template
from .models import Review, Restraunt
import numpy as np
from .models import Profile
import os
from django.views.generic import UpdateView
from django.db import transaction

def rest_list(request):
    restraunts = Restraunt.objects.filter(type='Restaurant').order_by('name')
    return render(request, 'main_app/rest_list.html', {'restraunts':restraunts})

def hot_list(request):
    restraunts = Restraunt.objects.filter(type='Hotel').order_by('name')
    return render(request, 'main_app/hot_list.html', {'restraunts':restraunts})

def toprated(request):
    restraunts = Restraunt.objects.all().order_by('-average')
    return render(request, 'main_app/toprated.html', {'restraunts':restraunts})

def caf_list(request):
    restraunts = Restraunt.objects.filter(type='Cafe').order_by('-average')
    return render(request, 'main_app/caf_list.html', {'restraunts':restraunts})

def bar_list(request):
    restraunts = Restraunt.objects.filter(type='Bar').order_by('-average')
    return render(request, 'main_app/bar_list.html', {'restraunts':restraunts})

from main_app.models import Bookmark
from django.urls import resolve

def bookmarks(request):
    try:
        name1 = request.GET.get('bookmark')
        restraunt = Restraunt.objects.get(name=name1)
        bk = Bookmark.objects.get_or_create(name=name1,user=request.user,restaurant=restraunt)
        restraunts = User.objects.get(username=request.user.username).bookmarks.all()
        print(request.path_info)
        return redirect(request.META.get('HTTP_REFERER', request.path_info))
        return render(request, 'main_app/book_list.html',{'restraunts':restraunts})
    except:
        restraunt = None
        path = request.get_full_path()
        bk = None
        print(request.path_info)
        restraunts = User.objects.get(username=request.user.username).bookmarks.all()
        return render(request, 'main_app/book_list.html',{'restraunts':restraunts})

def bookmarks2(request):
    if request.method == 'GET':
        print(request.GET)
    name1 = request.GET.get('bok')
    print(name1)

    # restraunt = Restraunt.objects.get(name=name1)
    # bk = Bookmark.objects.get_or_create(name=name1,user=request.user,restaurant=restraunt)
    restraunts = User.objects.get(username=request.user.username).bookmarks.all()

    return redirect(request.META.get('HTTP_REFERER', request.path_info))
    return render(request, 'main_app/book_list.html',{'restraunts':restraunts})


def remove_bk(request):
    name1 = request.GET.get('bookmark')
    print(name1)
    restraunt = Restraunt.objects.get(name=name1)
    bk = Bookmark.objects.get(name=name1,user=request.user,restaurant=restraunt).delete()
    return redirect(request.META.get('HTTP_REFERER', request.path_info))


def index(request):
    form_class = ContactForm()
    # new logic!
    rests = Restraunt.objects.all().order_by('-average')[:3]
    if request.method == 'POST':
        form = ContactForm(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get(
                'contact_name'
            , '')
            contact_email = request.POST.get(
                'contact_email'
            , '')
            form_content = request.POST.get('content', '')

            # Email the profile with the
            # contact information
            template = get_template('main_app/contact_template.txt')
            context = {
                'contact_name': contact_name,
                'contact_email': contact_email,
                'form_content': form_content,
            }
            content = template.render(context)

            email = EmailMessage(
                "New contact form submission",
                content,
                "Your website" +'',
                ['vagal2003@gmail.com'],
                headers = {'Reply-To': contact_email }
            )
            email.send()

            return redirect('index')
            print(profile_catcher())


    return render(request,'main_app/index.html',{'contact_form':form_class,'rests':rests})


def detail(request,pk):
    average = []
    form = ReviewForm()
    restraunt = get_object_or_404(Restraunt,pk=pk)
    reviews = Review.objects.filter(restraunt=restraunt)
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            rating = request.POST['rating']
            print(rating)
            # print(request.POST['rating'])
            review = form.save(commit=False)
            review.restraunt = restraunt
            review.user = request.user
            review.rating = int(rating) / 10
            print(review.rating)
            if review.rating == 5.0:
                review.rating = 5
                print(review.rating)
            elif review.rating == 4.0:
                review.rating = 4
                print(review.rating)
            elif review.rating == 3.0:
                review.rating = 3
                print(review.rating)
            elif review.rating == 2.0:
                review.rating = 2
                print(review.rating)
            elif review.rating == 1.0:
                review.rating = 1
                print(review.rating)
            if review.rating == 0.4:
                review.rating = review.rating * 10
                print(review.rating)
            elif review.rating == 0.2:
                review.rating = review.rating * 10
                print(review.rating)
            elif review.rating == 0.1:
                review.rating = review.rating * 10
                print(review.rating)
            elif review.rating == 0.3:
                review.rating = review.rating * 10
                print(review.rating)
            elif review.rating == 0.5:
                review.rating = int(review.rating * 10)
                print(review.rating)
            elif review.rating == 0:
                review.rating = 0.5
            review.save()
            for rev in reviews:
                average.append(rev.rating)
            restraunt.average = round(np.mean(average))
            print(restraunt.average)
            restraunt.save()
            return redirect('detail', pk=restraunt.pk)
        else:
            return HttpResponse('Not all fields were filled in')
    else:
        form = ReviewForm()
    return render(request,'main_app/detail.html',{'restraunt':restraunt,'form':form})

def listing(request):
    return render(request,'main_app/listing.html',{})


from django.views.decorators.http import require_http_methods
from django.http import HttpResponse

@require_http_methods(['GET'])
def search(request):
    q = request.GET.get('q')
    area = request.GET.get('area')
    if q and area:
        restraunts = Restraunt.objects.filter(name__contains=q,area__contains=area)
        area = restraunts[0].area
    elif area and not q:
        restraunts = Restraunt.objects.filter(area__contains=area)
        area = restraunts[0].area
    elif q and not area:
        restraunts = Restraunt.objects.filter(name__contains=q)
    else:
        restraunts = Restraunt.objects.filter(name__contains=q)
    return render(request, 'main_app/search_results.html', {'restraunts': restraunts, 'query': q,'area':area})
    # return HttpResponse('Please submit a search term.')

@require_http_methods(['GET'])
def search2(request):
    q2 = request.GET.get('q2')
    area2 = request.GET.get('area2')
    if q2 and area2:
        restraunts = Restraunt.objects.filter(name__contains=q2,area__contains=area2)
        area = restraunts[0].area
    elif area2 and not q2:
        restraunts = Restraunt.objects.filter(area__contains=area2)
        area = restraunts[0].area
    elif q2 and not area2:
        restraunts = Restraunt.objects.filter(name__contains=q2)
    else:
        restraunts = Restraunt.objects.filter(name__contains=q2)
        print('this')
    return render(request, 'main_app/search_results.html', {'restraunts': restraunts, 'query': q2,'area':area2})
    # return HttpResponse('Please submit a search term.')


from django.contrib.auth import login, authenticate,logout
from django.shortcuts import render, redirect

from .forms import SignUpForm

# def signup(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=raw_password)
#             login(request, user)
#
#             # profile = pic_form.save(commit=False)
#             # profile.user = user
#             #
#             # if 'profile_pic' in request.FILES:
#             #     profile.profile_pic = request.FILES['profile_pic']
#             #
#             # profile.save()
#             return redirect('index')
#     else:
#         form = SignUpForm()
#         # pic_form = ImageUploadForm()
#     return render(request, 'main_app/signup.html', {'form':form})
def signup(request):
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST,request.FILES)
        form = SignUpForm(request.POST)
        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            user.is_active = False
            user.save()
            profile = profile_form.save(commit=False)
            if 'image' in request.FILES:
                profile.image = request.FILES['image']
            profile.user = user
            profile.save()
            current_site = get_current_site(request)
            subject = 'Activate Your Masa.az Account'
            message = render_to_string('main_app/account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject, message)
            return redirect('account_activation_sent')
    else:
        form = SignUpForm()
        profile_form = ProfileForm()
    return render(request, 'main_app/signup.html', {'form': form,'profile_form':profile_form})

from .tokens import account_activation_token

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.profile.email_confirmed = True
        user.save()
        login(request, user,backend='django.contrib.auth.backends.ModelBackend')
        return redirect('/')
    else:
        return render(request, 'main_app/account_activation_invalid.html')

def account_activation_sent(request):
    return render(request, 'main_app/account_activation_sent.html')

# @login_required
# def add_review_to_restraunt(request, pk):
#     restraunt = get_object_or_404(Restraunt, pk=pk)
#     for rev in reviews:
#         if rev.rating > 14:
#             average.append(rev.rating / 10)
#         else:
#             average.append(rev.rating)
#     if request.method == "POST":
#         rating = request.POST['rating']
#         print('Rating is:' + str(rating))
#         form = ReviewForm(request.POST)
#         if form.is_valid():
#             print(request.POST['rating'])
#             review = form.save(commit=False)
#             review.restraunt = restraunt
#             review.user = request.user
#             review.save()
#             return redirect('detail', pk=restraunt.pk)
#     else:
#         form = ReviewForm()
#     return render(request, 'main_app/add_review_to_restraunt.html', {'form': form})
from django.contrib import messages
from django.shortcuts import redirect
import requests # requests==2.5.0
import json
import jwt
from django.contrib.auth.forms import UserCreationForm

@login_required
@transaction.atomic
def update_profile(request):
    current_pic = request.user.profile.image.url
    user_form = UserCreationForm()
    profile_form = ProfileForm()
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST,instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        current_pic = request.user.profile.image.url
        if profile_form.is_valid() and user_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            if 'image' in request.FILES:
                profile.image = request.FILES['image']
            else:
                print(request.FILES)
            profile.user = user
            user.profile = profile
            profile.save()
            print(profile.image.url)
            login(request, user,backend='django.contrib.auth.backends.ModelBackend')
            return redirect('/')
        else:
            messages.error(request, ('Please correct the error below.'))
    else:
        profile_form = ProfileForm(instance=request.user.profile)
        user_form = UserCreationForm(instance=request.user)
    return render(request, 'main_app/update_picture.html', {
        'user_form': user_form,
        'profile_form': profile_form,
        'current_pic': current_pic
    })
