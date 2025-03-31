from django.shortcuts import render,redirect
from .models import Meeting,User,Location
from .forms import MeetingForm,UserForm
from django.utils.timezone import now

def meeting_list(request):
    meetings = Meeting.objects.all()
    future_meetings = Meeting.objects.filter(date_time__gte=now())
    return render(request, 'meetings/meeting_list.html', {'meetings':meetings, 'future_meetings': future_meetings})



def create_meeting(request):
    users = User.objects.all()  # Busca os usuários e passa para o template
    locations = Location.objects.all()
    if request.method == 'POST':
        form = MeetingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('meeting_list')
    else:
        form = MeetingForm()

    return render(request, 'meetings/create_meeting.html', {'form': form, 'users': users, 'locations': locations})


def create_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create_meeting')
        
    else:
        form = UserForm()

    return render(request, 'user/create_user.html', {'form': form})

def user_list(request):
    users = User.objects.all()
    return render(request, 'meetings/create_meeting.html', {'users': users})