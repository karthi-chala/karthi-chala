from django.http import HttpResponse
import os
from django.shortcuts import render

def samrend(request):
    return render(request,'sample.html')