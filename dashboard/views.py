from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from ticket.models import *

@login_required
def dashboard(request):
    #customer
    all_ticket_for_customer = Ticket.objects.filter(created_by =request.user).order_by('-id')[:5]
    all_ticket =Ticket.objects.filter(created_by =request.user).count()
    pending_ticket =Ticket.objects.filter(created_by =request.user,status='Pending').count()
    active_ticket =Ticket.objects.filter(created_by =request.user,status='Active').count()
    closed_ticket =Ticket.objects.filter(created_by =request.user,status='Completed').count()


    #admin
    all_ticket_for_admin = Ticket.objects.all().order_by('-id')[:5]
    all_ticket_n = Ticket.objects.all().count()
    pending_ticket_n =Ticket.objects.filter(status='Pending').count()
    active_ticket_n =Ticket.objects.filter(status='Active').count()
    closed_ticket_n =Ticket.objects.filter(status='Completed').count()
    


    context ={
        "all_ticket_for_customer":all_ticket_for_customer,
        "all_ticket":all_ticket,
        "pending_ticket":pending_ticket,
        "active_ticket":active_ticket,
        "closed_ticket":closed_ticket,
        "all_ticket_for_admin":all_ticket_for_admin,
        "all_ticket_n":all_ticket_n,
        "pending_ticket_n":pending_ticket_n ,
        "active_ticket_n":active_ticket_n,
        "closed_ticket_n":closed_ticket_n,
    }
    return render(request,'dashboard.html',context)