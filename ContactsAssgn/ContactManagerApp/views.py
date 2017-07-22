from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.views import generic
from .forms import PostForm

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

class ContactView(generic.edit.FormView):
    template_name = 'ContactManagerApp/contacts.html'
    form_class = PostForm
    success_url = '/'

    def form_valid(self, form):
        firtsname = form.cleaned_data['FirstName']
        lastname = form.cleaned_data['LastName']
        email = form.cleaned_data['Email']
        mobileno = form.cleaned_data['MobileNo']
        contact = Contacts(FirstName = firtsname, LastName=lastname, Email=email, MobileNo=mobileno)
        contact.save()
        return super(ContactView, self).form_valid(form)

class DeleteContactView(generic.DeleteView):    
    template_name = 'ContactManagerApp/contacts.html'
    success_url = '/'


class UpdateContactView(generic.UpdateView):



#def contact_new(request):
#    if request.method == "POST":
#        form = PostForm(request.POST)
#        if form.is_valid():
#            Contacts = form.save(commit=False)
#            Contacts.save()
#            return HttpResponseRedirect('/')
#    else:
#        form = PostForm()
#    return render(request, 'ContactManagerApp/contacts.html', {'form': form})