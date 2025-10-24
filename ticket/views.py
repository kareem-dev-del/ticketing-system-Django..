from django.shortcuts import render,redirect
from .forms import *
from .models import *
from django.contrib import messages 
import datetime

# Create your views here.
def create_ticket(request):
    if request.POST:
        form = CreateTicketForm(request.POST)
        if form.is_valid():
            new =form.save(commit=False)
            new.created_by =request.user
            new.status = "Pending"
            new.save()  
            messages.success(request ,'make Ticket Succefully...')
            return redirect('dashboard')
        else:
            messages.warning(request,'Error Please Try agin!!!')
            return redirect('create_ticket') 
    else:
        form = CreateTicketForm()
        return render(request , 'create_ticket.html',{'form' : form})   


def update_ticket(request, pk):

    ticket = Ticket.objects.get(id=pk)

    if not ticket.is_resolved:
        if ticket.created_by != request.user:
            messages.error(request, "You can't edit this ticket!")
            return redirect('dashboard')

        if request.POST:
            form = UpdateTicketForm(request.POST, instance=ticket)
            if form.is_valid():
                form.save()
                messages.success(request, 'Update Ticket Succefully...')
                return redirect('dashboard')
            else:
                messages.warning(request, 'Error Please Try agin!!!')
                return redirect('update_ticket', pk=pk)
        else:
            form = UpdateTicketForm(instance=ticket)
            return render(request, 'update_ticket.html', {'form': form})
    else:messages.warning(request,'You canot change this ticket...')
    return redirect('dashboard')

def all_tickets(request):
    ticket = Ticket.objects.filter(created_by = request.user).order_by('-id')
    return render(request , 'all_tickets.html',{'ticket' : ticket})


def ticket_queue(request):
    ticket = Ticket.objects.filter(status = 'Pending').order_by('-id')
    return render(request , 'ticket_queue.html',{'ticket' : ticket})

def accept_ticket(request,pk):    
    ticket = Ticket.objects.get(id=pk)
    ticket.assigned_to = request.user
    ticket.status = 'Active'
    ticket.accepted_date = datetime.datetime.now()
    ticket.save()
    messages.success(request , 'Acepted Ticket successfully ...')
    return redirect('ticket_queue')


def closedt_ticket(request,pk):    
    ticket = Ticket.objects.get(id=pk)
    ticket.is_resolved= True
    ticket.status = 'Completed'
    ticket.accepted_date = datetime.datetime.now()
    ticket.save()
    messages.warning(request , 'Closed Ticket successfully ...',extra_tags='danger')
    return redirect('ticket_queue')

def workspace(request):
    ticket = Ticket.objects.filter(assigned_to =request.user, is_resolved=False)
    return render(request , 'workspace.html',{'ticket':ticket })

def  all_tickets_closed(request):
    ticket = Ticket.objects.filter(assigned_to =request.user, is_resolved=True)
    return render(request , 'all_tickets_closed.html',{'ticket':ticket })

def detail_ticket(request,pk):
    ticket = Ticket.objects.get(id = pk)
    return render(request , 'detail_ticket.html',{'ticket':ticket})

def delete_ticket(request,pk):
    ticket = Ticket.objects.get(id=pk)
    ticket.delete()
    messages.success(request ,'Deleted successfully...')
    return redirect('dashboard')