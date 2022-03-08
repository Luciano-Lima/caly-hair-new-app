from django.shortcuts import render, redirect, reverse
# from .models import Cutting, Styling, Colour, Highlights, Toners, Treatment
from .models import Cutting


# Create your views here.
# def home(request):
#     cutting = Cutting.objects.all().order_by('name')
#     styling = Styling.objects.all().order_by('name')
#     colour = Colour.objects.all().order_by('name')
#     highlights = Highlights.objects.all().order_by('name')
#     toners = Toners.objects.all().order_by('name')
#     treatment = Treatment.objects.all().order_by('name')
#     return render(request, 'index.html',
#         {'cutting': cutting, 'styling': styling, 'colour': colour, 
#         'highlights': highlights, 'toners': toners, 'treatment': treatment})

def home(request):
    cutting = Cutting.objects.all().order_by('name')
    return render(request, 'index.html',
    {'cutting': cutting,})
        
    

