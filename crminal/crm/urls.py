from django.contrib.auth.decorators import login_required
from django.conf.urls import url, include
#from viewsets import ModelViewSet
from . import views
from .views import *
from .models import Stage, Company, Contact, Campaign, Opportunity, Reminder, Report, CallLog, OpportunityStage

urlpatterns = [
    url(r'^$', login_required(views.Dashboard.as_view()), name="dashboard"),
 
    url(r'^search/$', login_required(views.search), name="search"),
 
    url(r'^stages/$', login_required(views.StageList.as_view()), name="stage_list"),
    url(r'^stages/(?P<pk>\d+)/$', login_required(views.StageDetail.as_view()), name="stage_detail"),
    url(r'^stages/create/$', login_required(views.CreateStage.as_view()), name="stage_create"),
    url(r'^stages/(?P<pk>\d+)/update/$', login_required(views.UpdateStage.as_view()), name="stage_update"),
    url(r'^stages/(?P<pk>\d+)/delete/$', login_required(views.DeleteStage.as_view()), name="stage_delete"),
	
    url(r'^companies/$', login_required(views.CompanyList.as_view()), name="company_list"),
    url(r'^companies/(?P<pk>\d+)/$', login_required(views.CompanyDetail.as_view()), name="company_detail"),
    url(r'^companies/create/$', login_required(views.CreateCompany.as_view()), name="company_create"),
    url(r'^companies/(?P<pk>\d+)/update/$', login_required(views.UpdateCompany.as_view()), name="company_update"),
    url(r'^companies/(?P<pk>\d+)/delete/$', login_required(views.DeleteCompany.as_view()), name="company_delete"),
    
    url(r'^contacts/$', login_required(views.ContactList.as_view()), name="contact_list"),
    url(r'^contacts/(?P<pk>\d+)/$', login_required(views.ContactDetail.as_view()), name="contact_detail"),
    url(r'^contacts/create/$', login_required(views.CreateContact.as_view()), name="contact_create"),
    url(r'^contacts/(?P<pk>\d+)/update/$', login_required(views.UpdateContact.as_view()), name="contact_update"),
    url(r'^contacts/(?P<pk>\d+)/delete/$', login_required(views.DeleteContact.as_view()), name="contact_delete"),
	
    url(r'^campaigns/$', login_required(views.CampaignList.as_view()), name="campaign_list"),
    url(r'^campaigns/(?P<pk>\d+)/$', login_required(views.CampaignDetail.as_view()), name="campaign_detail"),
    url(r'^campaigns/create/$', login_required(views.CreateCampaign.as_view()), name="campaign_create"),
    url(r'^campaigns/(?P<pk>\d+)/update/$', login_required(views.UpdateCampaign.as_view()), name="campaign_update"),
    url(r'^campaigns/(?P<pk>\d+)/delete/$', login_required(views.DeleteCampaign.as_view()), name="campaign_delete"),
   
    url(r'^opportunities/$', login_required(views.OpportunityList.as_view()), name="opportunity_list"),
    url(r'^opportunities/(?P<pk>\d+)/$', login_required(views.OpportunityDetail.as_view()), name="opportunity_detail"),
    url(r'^opportunities/create/$', login_required(views.CreateOpportunity.as_view()), name="opportunity_create"),
    url(r'^opportunities/(?P<pk>\d+)/update/$', login_required(views.UpdateOpportunity.as_view()), name="opportunity_update"),
    url(r'^opportunities/(?P<pk>\d+)/delete/$', login_required(views.DeleteOpportunity.as_view()), name="opportunity_delete"),

    url(r'^reminders/$', login_required(views.ReminderList.as_view()), name="reminder_list"),
    url(r'^reminders/(?P<pk>\d+)/$', login_required(views.ReminderDetail.as_view()), name="reminder_detail"),
    url(r'^reminders/create/$', login_required(views.CreateReminder.as_view()), name="reminder_create"),
    url(r'^reminders/(?P<pk>\d+)/update/$', login_required(views.UpdateReminder.as_view()), name="reminder_update"),
    url(r'^reminders/(?P<pk>\d+)/delete/$', login_required(views.DeleteReminder.as_view()), name="reminder_delete"),

    url(r'^calllogs/$', login_required(views.CallLogList.as_view()), name="calllog_list"),
    url(r'^calllogs/(?P<pk>\d+)/$', login_required(views.CallLogDetail.as_view()), name="calllog_detail"),
    url(r'^calllogs/create/$', login_required(views.CreateCallLog.as_view()), name="calllog_create"),
    url(r'^calllogs/(?P<pk>\d+)/update/$', login_required(views.UpdateCallLog.as_view()), name="calllog_update"),
    url(r'^calllogs/(?P<pk>\d+)/delete/$', login_required(views.DeleteCallLog.as_view()), name="calllog_delete"),

    url(r'^opportunitystages/(?P<pk>\d+)/$', login_required(views.OpportunityStageDetail.as_view()), name="opportunitystage_detail"),
]
