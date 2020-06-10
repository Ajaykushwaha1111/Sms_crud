from django.shortcuts import render,HttpResponse,HttpResponseRedirect

# Create your views here.
from .models import Question
def home(request):
    return render(request, 'home.html')

def startexam(request):
    allQuestion =Question.objects.all()
    data ={
        'allQuestion':allQuestion
    }
    return render(request, 'startexam.html', data)

def endexam(request):
    return render(request, 'endexam.html')

def end_exam(request):
    return render(request,'end.html')




import json
def count_quetion(request):
    res ='no'
    data = json.loads(request.GET.get('data1', ''))
    correct = 0
    attempt =0
    for dd in data:
        attempt = attempt + 1
        q =Question.objects.filter(id=int(dd['id']),correct_answer=dd['opt'])
        if q:
            correct =correct+1


    result = {
            'attempt':attempt,
            'correct':correct,
            'missed':attempt-correct
        }

    if result:

        s =request.session['exam_r'] = result
        print(s,"ddddddd")


    return HttpResponse(correct)

def end_exam(request):
    data =request.session.get('exam_r')
    print(data,' gethhhh')
    return render(request,'end.html',data)































# import json
# def count_quetion(request):
#     res=False
#     data = json.loads(request.GET.get('data1', ''))
#     correct = 0
#     attempt =0
#
#     for dd in data:
#         q =Question.objects.filter(id=int(dd['id']),correct_answer=dd['opt'])
#         if q:
#             correct =correct+1
#         attempt = attempt + 1
#
#     result ={
#         'attempt':attempt,
#         'correct':correct,
#         'missed':attempt-correct
#     }
#
#     if result:
#         request.session['exam_result'] = result
#         res =True
#     exam_result =request.session.get('exam_result')
#     print(exam_result)
#
#     return HttpResponse('/')