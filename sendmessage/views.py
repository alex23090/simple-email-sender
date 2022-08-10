from django.shortcuts import render
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.


def messageForm(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        content = request.POST.get('content')
        send_mail(
            subject,
            content,
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False,
        )
        messages.success(request, 'Message was successfully sent!')
    else:
        messages.error(request, 'Something went wrong try to retype!')
    return render(request, 'message-form.html')
