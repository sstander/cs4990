#from django.http import HttpResponseRedirect
#from django import forms
#from django.views.generic.detail import SingleObjectMixin
from django.shortcuts import render
from django.views.generic import ListView, DetailView, FormView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy, reverse
from django.contrib.auth.models import User
from django.db.models import Count
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.views.generic import FormView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib.auth.models import User
from django.db.models import Count
import datetime
from itertools import chain
#from viewsets import ModelViewSet
from .models import Stage, Company, Contact, Campaign, Opportunity, Reminder, Report, CallLog, OpportunityStage

def search(request):
    if request.method == 'GET':
        if request.GET.get('q'):
            contact_results = []
	    opp_results = []
	    company_results = []
	    search_words = "%s" % (request.GET.get('q'))
	    search_word_list = search_words.split(' ')
	    for search_word in search_word_list:
	        print search_word
	        contact_firstname = Contact.objects.filter(first_name__icontains = search_word)
	        contact_lastname = Contact.objects.filter(last_name__icontains = search_word)
		contact.company = Contact.objects.filter(company__name__icontains = search_word)
		opp_firstname = Opportunity.objects.filter(contact__first_name__incontains = search_word)
		opp_lastname = Opportunity.objects.filter(contact__last_name__icontains = search_word)
		opp_stage = Opportunity.objects.filter(stage__name__icontains = search_word)
		company = Company.objects.filter(name__icontains = search_word)
		contact_results = contact_results + list(contact_firstname) + list(contact_lastname) + list(contact_company)
		opp_results = opp_results + list(opp_firstname) + list(opp_lastname) + list(opp_stage)
		company_results = company_results + list(company)
	    return render_to_response('crm/search_results.html', {'search':search_words, 'contacts': contact_results, 'opps': opp_results, 'companies': company_results}, context_instance=RequestContext(request))
    return render_to_response('crm/search_results.html', context_instance=RequestContext(request))

# Create your views here.
class Dashboard(ListView):
    model = OpportunityStage
    template_name = "crm/dashboard.html"

    def get_context_data(self, **kwargs):
        context = super(Dashboard, self).get_context_data(**kwargs)

        #AddingOpportunityStages to the template's context
	context["opportunity_stages"] = OpportunityStage.objects.all().order_by('-time_stamp')
	context["reminders"] = Reminder.objects.all().order_by('-date')[:5]
	context["opp_users"] = User.objects.annotate(num_opp=Count('opportunitystage'))
	context["stage_by_opp"] = Stage.objects.annotate(opp_count = Count('opportunity'))
	context["opportunity_list"] = Opportunity.objects.all().order_by('-create_date')[:5]

	return context

class StageList(ListView):
    model = Stage
    queryset = Stage.objects.order_by('order')

class StageDetail(DetailView):
    model = Stage

class CreateStage(CreateView):
    model = Stage
    fields = ['name', 'order', 'description', 'value']
    success_url = reverse_lazy('crm:stage_list')

class UpdateStage(UpdateView):
    model = Stage
    fields = ['name', 'order', 'description', 'value']
    success_url = reverse_lazy('crm:stage_list')

class DeleteStage(DeleteView):
    model = Stage
    success_url = reverse_lazy('crm:stage_list')

class CompanyList(ListView):
    model = Company

class CompanyDetail(DetailView):
    model = Company

class CreateCompany(CreateView):
    model = Company
    fields = ['name', 'website', 'address1', 'address2', 'city', 'state', 'zipcode', 'country', 'phone']
    success_url = reverse_lazy('crm:company_list')

class UpdateCompany(UpdateView):
    model = Company
    fields = ['name', 'website', 'address1', 'address2', 'city', 'state', 'zipcode', 'country', 'phone']
    success_url = reverse_lazy('crm:company_list')

class DeleteCompany(DeleteView):
    model = Company
    success_url = reverse_lazy('crm:company_list')

class ContactList(ListView):
    model = Contact

class ContactDetail(DetailView):
    model = Contact

class CreateContact(CreateView):
    model = Contact
    fields = ['company', 'first_name', 'last_name', 'address1', 'address2', 'city', 'state', 'zipcode', 'country', 'phone', 'email']
    success_url = reverse_lazy('crm:contact_list')

class UpdateContact(UpdateView):
    model = Contact
    fields = ['company', 'first_name', 'last_name', 'address1', 'address2', 'city', 'state', 'zipcode', 'country', 'phone', 'email']
    success_url = reverse_lazy('crm:contact_list')

class DeleteContact(DeleteView):
    model = Contact
    success_url = reverse_lazy('crm:contact_list')

class CampaignList(ListView):
    model = Campaign

class CampaignDetail(DetailView):
    model = Campaign

class CreateCampaign(CreateView):
    model = Campaign
    fields = ['name', 'description']
    success_url = reverse_lazy('crm:campaign_list')

class UpdateCampaign(UpdateView):
    model = Campaign
    fields = ['name', 'description']
    success_url = reverse_lazy('crm:campaign_list')

class DeleteCampaign(DeleteView):
    model = Campaign
    success_url = reverse_lazy('crm:campaign_list')

class OpportunityList(ListView):
    model = Opportunity

    def get_context_data(self, **kwargs):
        context = super(OpportunityList, self).get_context_data(**kwargs)

        #Adding OpportunityStages to the templates' context
        context["opportunity_stages"] = OpportunityStage.objects.all()

        return context

class OpportunityDetail(DetailView):
    model = Opportunity

class CreateOpportunity(CreateView):
    model = Opportunity
    fields = ['stage', 'company', 'contact', 'value', 'source', 'user']
    success_url = reverse_lazy('crm:opportunity_list')

class UpdateOpportunity(UpdateView):
    model = Opportunity
    fields = ['stage', 'company', 'contact', 'value', 'source', 'user']
    success_url = reverse_lazy('crm:opportunity_list')

    def form_valid(self, form):
        opportunity = form.save(commit=False)

        #Checks to make sure the stage being moved to is the next stage and not a previous stage
        if opportunity.stage.value > self.get_object().stage.value:
            opportunity_stage = OpportunityStage()
            opportunity_stage.opportunity = Opportunity.objects.all().filter(id = self.get_objects().pk)[0]
	    opportunity_stage.stage = form.cleaned_data['stage']
	    opportunity_stage.user = self.request.user
	    opportunity_stage.save()
        opportunity.save()
        return super(UpdateOpportunity, self).form_valid(form)

class DeleteOpportunity(DeleteView):
    model = Opportunity
    success_url = reverse_lazy('crm:opportunity_list')

class ReminderList(ListView):
    model = Reminder
    queryset = Reminder.objects.order_by('complete').order_by('-date')

class ReminderDetail(DetailView):
    model = Reminder

class CreateReminder(CreateView):
    model = Reminder
    fields = ['opportunity', 'date', 'note', 'completed']
    success_url = reverse_lazy('crm:reminder_list')

class UpdateReminder(UpdateView):
    model = Reminder
    fields = ['opportunity', 'date', 'note', 'completed']
    success_url = reverse_lazy('crm:reminder_list')

class DeleteReminder(DeleteView):
    model = Reminder
    success_url = reverse_lazy('crm:reminder_list')

class CallLogList(ListView):
    model = CallLog

class CallLogDetail(DetailView):
    model = CallLog

class CreateCallLog(CreateView):
    model = CallLog
    fields = ['opportunity', 'note', 'user']
    success_url = reverse_lazy('crm:calllog_list')

class UpdateCallLog(UpdateView):
    model = CallLog
    fields = ['opportunity', 'note', 'user']
    success_url = reverse_lazy('crm:calllog_list')

class DeleteCallLog(DeleteView):
    model = CallLog
    success_url = reverse_lazy('crm:calllog_list')

class OpportunityStageDetail(DetailView):
    model = OpportunityStage
