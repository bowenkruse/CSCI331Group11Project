from django.shortcuts import render
from Profile.models import UserProfile
from django.views.decorators.csrf import csrf_exempt
from .models import *
from django.http import JsonResponse


# Create your views here.
@csrf_exempt
def message_user(request):
    recipient = request.GET.get('q', None)
    print(recipient)
    recipient_user_object = UserProfile.objects.get(user__username__exact=recipient)
    sender_user_object = request.user.userprofile
    all_messages = Message_model.objects.all()

    messages_all = []
    for i in all_messages:
        if i.recipient == recipient_user_object and i.sender == sender_user_object:
            messages_all.append(i)
        elif i.recipient == sender_user_object and i.sender == recipient_user_object:
            messages_all.append(i)

    context = {
        'recipient': recipient_user_object,
        'messages_all': messages_all
    }
    return render(request, 'Profile/messages.html', context)


@csrf_exempt
def send_message(request):
    recipient = request.POST.get('message_recipient')
    message_body = request.POST.get('message_body')
    recipient_user_object = UserProfile.objects.get(user__username__exact=recipient)
    sender_user_object = request.user.userprofile
    new_message = Message_model(sender=sender_user_object, recipient=recipient_user_object, body=message_body)
    new_message.save()
    print(new_message)
    data = {
        'Success': True
    }
    return JsonResponse(data)
