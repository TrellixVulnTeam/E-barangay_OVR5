from django.urls import path
from . import views
# from .models import Post

urlpatterns = [
	path('request-document/',views.requested_doc,name="services-document"),
	path('sent-complaint/',views.sent_complaint,name="services-comlplaint"),
	path('sent-suggestion/',views.sent_suggestion,name="services-suggestion"),
	]