from datetime import datetime
from pytz import timezone 
from django.contrib import messages
from django.shortcuts import redirect, render
from django.core.mail import EmailMessage
from django.contrib.auth.decorators import login_required

from meetings import forms

from .models import Meet

# Create your views here.

@login_required(login_url = "accounts:login")
def request_meet(request):
    if request.method == "POST":
        form = forms.CreateMeetRequest(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.attendee = request.user
            instance.save()
            messages.success(request, "Your mock interview request has been sent to available interviwers someone will accept soon.")
            return redirect(request.user.get_absolute_url())
            
        # return redirect("meetings:requestmeet")

    else:
        form = forms.CreateMeetRequest()
    
    return render(request, "meetings/meet_request.html", 
                {'form':form, 'type': "Request"})

@login_required(login_url = "accounts:login")
def list_request_meet(request):
    isStaff = False
    if request.user.is_staff:
        meetings = Meet.objects.filter(accepted=False)
        isStaff = True
    else:
        meetings = Meet.objects.filter(attendee=request.user, accepted=False)

    return render(request, "meetings/list_meet_request.html", 
            {'meetings':meetings, 'isStaff': isStaff})

@login_required(login_url = "accounts:login")
def accept_meet(request):
    if request.user.is_staff:
        if request.method == "POST":
            meet_id = request.POST['meet_id']
            instance = Meet.objects.filter(pk=int(meet_id))
            if len(instance) == 1:
                instance = instance[0]
                attendee = instance.attendee
                addition_time = instance.addition_time.astimezone(timezone("Asia/Kolkata")).ctime()
                meet_time = datetime.strptime(request.POST["meettime"], '%Y-%m-%dT%H:%M').ctime()

                # send email to interviewee
                mail_subject = "Mock Interview with Gaddopur Coder"
                message = "Hi {name} \n\nYour interview request on {type_of_meet} created at {addition_time} (IST) is accepted by {interviewer} and scheduled at {meet_time} (IST).\nYou will get google meet invite shortly. \n\nThank You!".format(type_of_meet=instance.type_of_meeting, addition_time=addition_time, interviewer=request.user.name, meet_time=meet_time, name=attendee.name)
                to_email = attendee.email
                email = EmailMessage(
                    mail_subject, message, to=[to_email]
                )
                email.send()

                # send email to interviewer
                mail_subject = "Mock Interview with {name}".format(name=attendee.name)
                message = "Hi {name} \n\nYou have accepted interview request of {attendee} on {type_of_meet} and scheduled at {meet_time} (IST).\nPlease send the google meet invite on his email below are details of interviewee.\n\nEmail: {email}\nResume Link: {resume_link}\nLinkedin Profile: {linkedin_profile} \n\nThank You!".format(type_of_meet=instance.type_of_meeting, attendee=attendee.name, meet_time=meet_time, name=request.user.name, email=attendee.email, linkedin_profile=instance.linkedin_profile, resume_link=instance.resume_link)
                to_email = request.user.email
                email = EmailMessage(
                    mail_subject, message, to=[to_email]
                )
                email.send()
                print(mail_subject)
                print(message)
                print(to_email)
                instance.accepted = True
                instance.save()
            return redirect("meetings:listrequestmeet")

    return redirect(request.user.get_absolute_url())
    
@login_required(login_url = "accounts:login")
def done_meet(request):
    if request.user.is_staff:
        if request.method == "POST":
            meet_id = request.POST['meet_id']
            instance = Meet.objects.filter(pk=int(meet_id))
            if len(instance) == 1:
                instance = instance[0]
                attendee = instance.attendee
                addition_time = instance.addition_time.astimezone(timezone("Asia/Kolkata")).ctime()
                mail_subject = "Mock Interview Request With Gaddopur Coder Rejected"
                message = "Hi {name} \n\nYour interview request on {type_of_meet} created at {addition_time} (IST) is cancelled by intervewer since you have not entered asked data correctly. \n\nThank You!".format(name=attendee.name, type_of_meet=instance.type_of_meeting, addition_time=addition_time)
                to_email = attendee.email
                email = EmailMessage(
                    mail_subject, message, to=[to_email]
                )
                email.send()
                instance.delete()
            return redirect("meetings:listrequestmeet")

    return redirect(request.user.get_absolute_url())
        
