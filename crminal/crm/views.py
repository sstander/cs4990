#from django.http import HttpResponseRedirect
#from django import forms
#from django.views.generic.detail import SingleObjectMixin
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.views.generic import FormView, ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib.auth.models import User
from django.db.models import Count, Q
import datetime
from itertools import chain
#from viewsets import ModelViewSet
from .models import Stage, Company, Contact, Campaign, Opportunity, Reminder, Report, CallLog, OpportunityStage

# Create your views here.
class Dashboard(ListView):
    model = OpportunityStage
    template_name = "crm/dashboard.html"

    def get_context_data(self, **kwargs):
        context = super(Dashboard, self).get_context_data(**kwargs)

        #AddingOpportunityStages to the template's context
	context["opportunity_stages"] = OpportunityStage.objects.all().order_by('-time_stamp')[:5]
	context["reminders"] = Reminder.objects.all().order_by('-date')[:5]
	context["opp_users"] = User.objects.filter(opportunitystage__stage__value = 100).annotate(num_opp=Count('opportunitystage'))[:5]
	context["stage_by_opp"] = Stage.objects.order_by('-order').annotate(opp_count = Count('opportunity'))
	context["opportunity_list"] = Opportunity.objects.all().order_by('-create_date')[:5]

	return context

class SearchResults(TemplateView):
    template_name = 'crm/search_results.html'
    def get_context_data(self, **kwargs):
	context = super(SearchResults, self).get_context_data(**kwargs)

        # If we don't have a search term in the URL, just return the context as is.
	# Otherwise, populate the template context with potential search results.

	if not self.request.GET.get("q", None):
	    return context

	term = self.request.GET["q"] # save off the search term for convenience
	context['searchterm'] = term # send the search term to the template's context
	context['contact_list'] = Contact.objects.all().filter(
	    Q(first_name__icontains = term) | Q(last_name__icontains = term))
	context['company_list'] = Company.objects.all().filter(name__icontains = term)
	context['reminder_list'] = Reminder.objects.all().filter(note__icontains = term)
	context['calllog_list'] = CallLog.objects.all().filter(note__icontains = term)
	context['opportunity_list'] = Opportunity.objects.all().filter(
	    Q(contact__first_name__icontains = term) | Q(contact__last_name__icontains = term) | Q(stage__name__icontains = term))
	return context

class Reports(ListView):
    model = Report
    template_name = "reports/dashboard.html"

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
        if opportunity.stage.value != self.get_object().stage.value:
            opportunity_stage = OpportunityStage()
            opportunity_stage.opportunity = Opportunity.objects.all().filter(id = self.get_object().pk)[0]
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
