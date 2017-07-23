from django.shortcuts import redirect
from django.views import generic
from django.views.generic.edit import UpdateView, CreateView
from .forms import PostForm
from django.core.urlresolvers import reverse_lazy

from .models import Contacts

class ContactsListview(generic.ListView):
    template_name = 'ContactManagerApp/manage_contact.html'
    context_object_name = 'contactList'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(ContactsListview, self).get_context_data(**kwargs)
        context['pagesize'] = self.paginate_by
        return context

    def get_queryset(self):
        try:
            name = self.request.GET.get('keyword')
        except:
            name = ''
        if (name != None):
            object_list = Contacts.objects.filter(FirstName__icontains = name)
        else:
            object_list = Contacts.objects.all()
        return object_list

    def get_paginate_by(self, queryset):
        if len(self.request.GET) == 0:
            return self.request.GET.get('paginate_by', self.paginate_by)
        else:
            if {'paginate_by'}.issubset(self.request.GET):
                self.paginate_by = self.request.GET['paginate_by']
                return self.request.GET.get('paginate_by', self.paginate_by)
            else:                
                return self.request.GET.get('paginate_by', self.paginate_by)

class ContactView(CreateView):
    model = Contacts
    template_name = 'ContactManagerApp/contacts.html'
    success_url = reverse_lazy('contactlist')
    fields = ['FirstName', 'LastName', 'Email', 'MobileNo']

class EditContact(UpdateView):
    model = Contacts
    template_name = 'ContactManagerApp/contacts.html'
    success_url = reverse_lazy('contactlist')
    fields = ['FirstName', 'LastName', 'Email', 'MobileNo']

def deleteContact(request, pk, template_name='ContactManagerApp/contact_delete.html'):
    contact = get_object_or_404(Contacts, pk=pk)
    contact.delete()
    return redirect('contactlist')
