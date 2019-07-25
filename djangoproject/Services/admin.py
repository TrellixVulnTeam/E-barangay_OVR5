from django.contrib import admin
from .models import Requested_document,Complaint,Suggestion


class AdminComplaint(admin.ModelAdmin):
	list_display = ['complaint_sender','complaint_description','status_of_complaint','date_sent']
	list_filter = ['date_sent']


class AdminRequestedDoc(admin.ModelAdmin):
	list_display = ['requested_document_sender','type_of_document','purpose','status_of_document','date_sent']
	list_filter = ['date_sent']

class AdminSuggestion(admin.ModelAdmin):
	list_display = ['suggestion_sender','suggestion_description','date_sent']
	list_filter = ['date_sent']

admin.site.register(Requested_document,AdminRequestedDoc)
admin.site.register(Complaint,AdminComplaint)
admin.site.register(Suggestion,AdminSuggestion)
