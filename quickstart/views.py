from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from quickstart.serializers import ContactSerializer,FaqSerializer,NewsSerializer,UserSerializer, GroupSerializer
from .models import News,Faq,Contact

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm,SignUpForm

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes,force_text
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from .tokens import account_activation_token

from django.utils.http import urlsafe_base64_decode 
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    return render(request, 'home.html')

# from django.template.loader import render_to_string
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all().order_by('title')
    serializer_class = NewsSerializer

class FaqViewSet(viewsets.ModelViewSet):
    queryset = Faq.objects.all().order_by('question')
    serializer_class = FaqSerializer

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all().order_by('subject')
    serializer_class= ContactSerializer


def contactView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            surname = form.cleaned_data['surname']
            from_email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            mess= "Email: " +from_email + " sent you message."+ "\n\n Name: "+ name + "\n\n Surname: "+ surname + "\n\n Subject: " + subject + "\n\n Message: " + message + "\n\n Phone: " +phone
            try:
                send_mail(subject, mess, from_email, ['your_destination_mail']) # Sends mail . 
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "email.html", {'form': form})

def successView(request):
    return HttpResponse('Success! Thank you for your message.')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.is_staff=True 
            user.save() # Saves User
            current_site = get_current_site(request)
            subject = 'Activate Your Account'
            message = render_to_string('account_activation_email.html', { # custom html email. You can change from template.
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject, message)
            my_group = Group.objects.get(name='User') # Adds normal user role
            my_group.user_set.add(user)
            try:
                send_mail(subject, "message", "sender_email", ['destination_mail'],html_message=message) # Sends mail . Check settings.py for details.
            except BadHeaderError:
                return HttpResponse('Invalid header found.')

            return redirect('account_activation_sent')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def account_activation_sent(request):
    return render(request, 'account_activation_sent.html')

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
        login(request, user)
        return redirect('home')
    else:
        return render(request, 'account_activation_invalid.html')