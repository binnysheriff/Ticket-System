from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.views import View 
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from .models import Ticket, Comment
from django import forms
import contextlib

class Index(TemplateView):
    def get_template_names(self):
        return ['index.html'] 

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'description', 'priority']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'priority': forms.Select(attrs={'class': 'form-control'}),
        }
# Create your views here.

@login_required
def create_ticket(request):
    form = TicketForm(request.POST or None)
    if form.is_valid():
        form.save()
        send_mail(
            'A new ticket  has been created.',
            'binnysheriff@gmailcom',
            ['bsheriff@my.centennialcollege.ca'],
            fail_silently=False,)
        return redirect('ticket_list')        
    
    return render(request, 'tickets/create_ticket.html')

@login_required
def ticket_list(request):
    tickets = Ticket.objects.all()
    return render(request, 'tickets/ticket_list.html', {'tickets': tickets})

@login_required
def view_ticket(request, ticket_id):
    ticket = Ticket.objects.get(pk=ticket_id)
    comments = Comment.objects.filter(ticket=ticket)
    if request.method == 'POST':
        text = request.POST['comment_text']
        Comment.objects.create(
            text=text,
            user=request.user,
            ticket=ticket
        )
    return render(request, 'tickets/view_ticket.html', {'ticket': ticket, 'comments': comments})

@login_required
def close_ticket(request, ticket_id):
    # Verify if ticket_id is valid and perform ticket closing logic
    with contextlib.suppress(Ticket.DoesNotExist):
        ticket = Ticket.objects.get(pk=ticket_id)
        if not ticket.is_closed:
            ticket.is_closed = True
            ticket.save()
        # Redirect to the ticket list or another appropriate page
        return redirect('ticket_list')

class SubmitTicketView(FormView):
    template_name = 'submit_ticket.html'
    form_class = TicketForm
    # you can change this to where you want to redirect after a successful form submission
    success_url = reverse_lazy('submit_ticket')  
    
    def form_valid(self, form):
        # save the form instance if it's valid
        form.save() 
        return super().form_valid(form)