from django.shortcuts import render, get_object_or_404
from .models import  Program, University



def homepage_view(request):
    masters_program = Program.objects.filter(program_type='MSc')
    pdh_program = Program.objects.filter(program_type='PhD')
    return render(request, 'study_abroad/index.html', {'masters':masters_program, 'phds':pdh_program})


def program_detail_view(request, pk):
    program = get_object_or_404(Program, pk=pk)
    return render(request, 'study_abroad/program_detail.html', {'program':program})