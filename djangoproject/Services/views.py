from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from .models import Requested_document,Complaint,Suggestion
from django.db import models

User = get_user_model()

@login_required
def requested_doc(request):
	context = {
		'documents': Requested_document.objects.all()
	}
	return render(request,'Requested_docs.html',context)

@login_required
def sent_complaint(request):
	context = {
		'complaints': Complaint.objects.all()
	}
	return render(request,'recieved-complaints.html',context)

@login_required
def sent_suggestion(request):
	context = {
		'suggestions': Suggestion.objects.all()
	}
	return render(request,'recieved-suggestions.html',context)