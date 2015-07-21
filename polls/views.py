from django.contrib.auth import logout as auth_logout
from django.utils import timezone
from django.contrib.auth.hashers import make_password,check_password
from django.shortcuts import get_object_or_404, redirect
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from polls.models import (Userdata, Choice)
from .models import Question
from django.contrib import messages
from django.contrib.messages import get_messages, constants

import re

def checkUserAvailability(request):
    return HttpResponse(isuseravailable(request))

def checkEmailAvailability(request):
    return HttpResponse(isemailnotregistered(request))


def isuseravailable(request):
    name = request.POST.get('username')
    if Userdata.objects.filter(username__iexact=name):
        response = False
    else:
        response = True
    return response

def isemailnotregistered(request):
    email = request.POST.get('email')
    if Userdata.objects.filter(email__iexact=email):
        return False
    else:
        return True

def userlogin(request):
    if request.session.__contains__('user_id') :
        return True
    return False


def handler404(request):
    return render(request, '404.html')


def login(request):
    if request.method == 'GET':
      context={}
      storage = get_messages(request)
      for message in storage:
            context.update({'success': message})
      if request.session.__contains__('user_id'):
          return redirect('/polls/')
      return render(request, 'polls/login.html',context)
    else:
      context = {}
      try:
        user = Userdata.objects.get(username=request.POST['username'])
        if user is None:
            context['error'] = 'No such user exits'
        elif check_password(request.POST['password'],user.password):
            request.session['user_id'] = user.id
            return redirect('/polls/')
        else:
            context['error'] = 'Wrong password'
      except:
        context['error'] = 'No such user exits'
      return render(request, 'polls/login.html', context)

def logout(request):
    context={}
    try:
        auth_logout(request)
        del request.session['user_id']
    except:
        context['error']='Some error occured'
    return redirect('/polls/login/',context)

def signup(request):
    if request.method == 'GET':
        if userlogin(request):
            return redirect('/polls/')
        return render(request, 'polls/signup.html')
    elif request.method == 'POST':
          context = {}

          username = request.POST.get('username')
          if not username:
            context['user_name_error'] = 'User name is required'
          else:
            a=re.compile("^[a-zA-Z0-9_-]{4,20}$")
            if not a.match(username):
                context['user_name_error'] = 'User name can have 4-15 characters without any special characters'
            else:
                usercheck = isuseravailable(request)
                if usercheck is False:
                  context['user_name_error'] = "This username is already taken"

          email = request.POST.get('email')
          if not email:
            context['email_error'] = 'EmailID is required'
          else:
            a=re.compile("^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$")
            if not a.match(email):
                context['email_error'] = 'Please enter valid EmailID'
            elif not isemailnotregistered(request):
                context['email_error'] = "This EmailID is already taken"

          phone = request.POST.get('phone')
          if not phone:
            context['phone_error'] = 'Phone number is required'
          else:
            a=re.compile("^[1-9]{1}[0-9]{9}$")
            if not a.match(phone):
                context['phone_error'] = 'Please enter valid phone number'
            elif len(phone) < 10:
                context['phone_error'] = "Your phone number must be at least 10 digits long"

          password = request.POST.get('password')
          if not password:
            context['password_error'] = 'password is required'
          else:
            a=re.compile("^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%&_]).*$")
            if not a.match(password):
                context['password_error'] = "Password should contain: at least one lower case character, at least one upper case character, at least one number and at least one special character ( @ # $ % & _ )"
            elif len(password) < 8:
                context['password_error'] = "Your password must be at least 8 characters long"

          if bool(context):
              context['username']=username
              context['email']=email
              context['phone_no']=phone
              context['password']=password
              return render(request, 'polls/signup.html', context)
          else:
              password=make_password(password, None, 'pbkdf2_sha256')

              user = Userdata.objects.create(username=username, email=email, phone_no=phone, password=password)

              user.save()
              messages.add_message(request, constants.SUCCESS,'You are successfully signed in. Please Login to continue.')
              return redirect('/polls/login/',context)


def index(request):
    test = userlogin(request)
    if test==True:
        user = Userdata.objects.get(id=request.session.get('user_id'))
        latest_question_list = Question.objects.order_by('-pub_date')[:10]
        context = {'latest_question_list': latest_question_list ,'username': user.username}
        storage = get_messages(request)
        for message in storage:
            context.update({'success': message})
        return render(request, 'polls/index.html', context)
    return redirect('/polls/login/')

def addquestion(request):
    if request.method=='GET':
        return render(request, 'polls/addquestion.html')
    elif request.method == 'POST':
        question = Question.objects.create(question_text=request.POST['questiontext'], pub_date =timezone.now())
        choice1=Choice.objects.create(question=question, choice_text=request.POST['choice1'])
        choice2=Choice.objects.create(question=question, choice_text=request.POST['choice2'])
        choice3=Choice.objects.create(question=question, choice_text=request.POST['choice3'])
        choice1.save()
        choice2.save()
        choice3.save()
        question.save()
        messages.add_message(request, constants.SUCCESS, 'Question added successfully.')
        return redirect('/polls/')


def detail(request, question_id):
   if userlogin(request):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})
   return redirect('/polls/login/')

def results(request, question_id):
   if userlogin(request):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})
   return redirect('/polls/login/')

def vote(request, question_id):
   if userlogin(request):
    p = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))
   return redirect('/polls/login/')