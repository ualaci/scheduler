from django.shortcuts import render,redirect
from .models import Meeting,User
from .forms import MeetingForm,UserForm

def meeting_list(request):
    meetings = Meeting.objects.all()
    return render(request, 'meetings/meeting_list.html', {'meetings':meetings})

def create_meeting(request):
    if request.method == 'POST':
        form = MeetingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('meeting_list')
                
    else:
        form = MeetingForm()
    
    return render(request, 'meetings/create_meeting.html', {'form':form})

def create_user(request):
    if request.method == 'POST':
        form = UserForm
        if form.is_valid():
            form.save()
            return redirect('create_meeting.html')
        
    else:
        form = UserForm()

    return render(request, 'user/create_user.html', {'form': form})