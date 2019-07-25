from django.shortcuts import render
from rest_framework import viewsets
from .models import Language
from .serializers import LanguageSerializer



def language(request):
	context = {
		'programmings':Language.objects.all()
	}
	return render(request,"language.html",context)



class LanguageView(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
