from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db.models import Q 

from .models import *      # models 의 모든 모델 import
from .forms import TodoForm

# Create your views here.
def index(request):
    print('메인 화면...')
    return render(request, 'todo/index.html', {})

def todo(request):
    print('할 일 목록 화면...')
    # 할 일 목록 조회 
    # Todo 모델의 대기 목록 조회 
    wait_list = Todo.objects.filter(status='WAIT')
    # Todo 모델의 진행 목록 조회
    ing_list = Todo.objects.filter(Q(status='ING') | Q(status='DONE')).order_by('-status')
    
    form = TodoForm()
    
    content = {'wait_list' : wait_list, 'ing_list':ing_list, 'form':form,}
    # render(request, 템플릿 경로, 데이터{})
    # - 데이터{} : 템플릿에 데이터를 전달 
    return render(request, 'todo/todo.html', content)

def create(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('todo'))
        else:
            # 유효성 검사 실패 시 다시 목록으로 + 에러 포함 렌더링
            print("유효성 검사 실패")
            print(form.errors)
            wait_list = Todo.objects.filter(status='WAIT')
            ing_list = Todo.objects.filter(Q(status='ING') | Q(status='DONE')).order_by('-status')
            content = {
                'wait_list': wait_list,
                'ing_list': ing_list,
                'form': form,
            }
            return render(request, 'todo/todo.html', content)

def delete(request):
    print('삭제 요청...')
    # 파라미터 
    no = request.POST['no']
    print('no : {}'.format(no))
    try:
        todo = Todo.objects.get(no=no)
        todo.delete()       # 할 일 삭제 요청 
    except Todo.DoesNotExist:
        print('삭제할 할 일이 없습니다. ')
    return HttpResponseRedirect(reverse('todo'))

def ing(request):
    print('진행 상태로 변경...')
    no = request.POST['no']
    print('no : {}'.format(no))
    try:
        todo = Todo.objects.get(no=no)
        # 할 일 상태 수정 
        todo.status = 'ING'      
        todo.save()
    except Todo.DoesNotExist:
        print('삭제할 할 일이 없습니다. ')
    return HttpResponseRedirect(reverse('todo'))

def done(request):
    print('완료 상태로 변경...')
    no = request.POST['no']
    print('no : {}'.format(no))
    try:
        todo = Todo.objects.get(no=no)
        # 할 일 상태 수정   
        if todo.status == 'DONE':
            todo.status == 'ING'
        else:
            todo.status = 'DONE'
        todo.save()
    except Todo.DoesNotExist:
        print('삭제할 할 일이 없습니다. ')
    return HttpResponseRedirect(reverse('todo'))


def wait(request):
    print('대기 상태로 변경...')
    no = request.POST['no']
    print('no : {}'.format(no))
    try:
        todo = Todo.objects.get(no=no)
        # 할 일 상태 수정   
        todo.status = 'WAIT'
        todo.save()
    except Todo.DoesNotExist:
        print('삭제할 할 일이 없습니다. ')
    return HttpResponseRedirect(reverse('todo'))

def update(request):
    if request.method == 'POST':
        no = request.POST.get('no')
        todo = get_object_or_404(Todo, no=no)
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
        # else 처리 안 해도 됨: 인라인 폼이기 때문 (원상복구로 처리됨)
    return HttpResponseRedirect(reverse('todo'))
