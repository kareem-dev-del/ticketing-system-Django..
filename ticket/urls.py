from django.urls import path
from .views import *
urlpatterns = [
    path('create_ticket',create_ticket,name='create_ticket'),
    path('update_ticket/<int:pk>/',update_ticket,name='update_ticket'),
    
    path('all_tickets',all_tickets,name='all_tickets'),
    path('ticket_queue',ticket_queue,name='ticket_queue'),
    path('accept_ticket/<int:pk>/',accept_ticket,name='accept_ticket'),
    path('workspace',workspace,name='workspace'),
    path('all_tickets_closed',all_tickets_closed,name='all_tickets_closed'),
    path('detail_ticket/<int:pk>/',detail_ticket,name='detail_ticket'),
    path('closedt_ticket/<int:pk>/',closedt_ticket,name='closedt_ticket'),
    path('delete_ticket/<int:pk>/',delete_ticket,name='delete_ticket'),
]   
