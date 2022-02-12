from django.shortcuts import render,redirect
from django.http import HttpResponse
from todolist_app.models import TaskList
from .forms import TaskForm
from django.contrib import messages
from django.core.paginator import Paginator
# Create your views here.
from django.contrib.auth.decorators import login_required


@login_required
def todolist(request):
    if request.method=='POST':
    
        form=TaskForm(request.POST or None)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.manage=request.user
            instance.save()

        messages.success(request,'New task added!')
        return redirect('todolist')
    else:
        all_tasks=TaskList.objects.filter(manage=request.user)
        paginator=Paginator(all_tasks,3)
        page=request.GET.get('pg')
        all_tasks=paginator.get_page(page)
        return render(request,'todolist.html',{'all_tasks':all_tasks})
@login_required
def delete_task(request,bucin_id):
    
    task=TaskList.objects.get(pk=bucin_id)
    if task.manage==request.user:    
        task.delete()
    else:
        messages.error(request,'Access denied. You are not allowed!')
    return redirect('todolist')
@login_required
def edit_task(request,bucin_id):
    
    if request.method=='POST':
        task=TaskList.objects.get(pk=bucin_id)
        form=TaskForm(request.POST or None,instance=task)
        if form.is_valid():
            form.save()
        messages.success(request,'Task edited!')
        return redirect('todolist')
    else:
        task_obj=TaskList.objects.get(pk=bucin_id)
        return render(request,'edit.html',{'task_obj':task_obj})
@login_required
def complete_task(request,bucin_id):
    task=TaskList.objects.get(pk=bucin_id)
    if task.manage==request.user:
        task.done=True
        task.save()
    else:
        messages.error(request,'Access denied. You are not allowed!')
    return redirect('todolist')
@login_required
def pending_task(request,bucin_id):
    task=TaskList.objects.get(pk=bucin_id)
    
    task.done=False
    task.save()
    return redirect('todolist')

def index(request):
    context={'index_text':'index homepageg emtmtmt'}
    return render(request,'index.html',context)




def contact(request):
    context={'welcome_text':'conttactd'}
    return render(request,'contact.html',context)

def about(request):
    context={'welcome_text':'babout'}
    return render(request,'about.html',context)