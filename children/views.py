from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

from children.models import ChildrenGroup, Children
from djangoProject.forms import GroupForm, ChildrenForm, UpdateChildrenForm


def children_download(request, pk):
    children = Children.objects.get(pk=pk)
    response = HttpResponse(content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename=' + str(children) + '.txt'
    lines = [
        "ФИО: " + str(children) + "\n",
        "Дата рождения: " + str(children.BornDate) + "\n",
        "Группа: " + str(children.Group) + "\n",
        "Информация: " + str(children.Info) + "\n",
    ]
    response.writelines(lines)
    return response
@login_required
def children_detail(request, pk):
    children = Children.objects.get(pk=pk)
    context = {
        'children': children,
    }
    return render(request, 'children/children_detail.html', context)
@login_required
def group(request):
    access = request.user.groups.filter(name="Старший воспитатель").exists() \
             or request.user.groups.filter(name="Заведующий").exists()
    topaccess = request.user.groups.filter(name="Заведующий").exists()

    if request.method == "POST":
        form = GroupForm(request.POST)
        if form.is_valid():
            form.save()
    if access:
        list_group = ChildrenGroup.objects.all()
    else:
        list_group = ChildrenGroup.objects.filter(Mentor=request.user.id)
    context = {
        'list_group': list_group,
        'access': access,
        'topaccess': topaccess,
        'form': GroupForm(),
    }
    return render(request, 'group/group.html', context)


@login_required
def group_detail(request, pk):
    Group = ChildrenGroup.objects.get(id=pk)
    list_children = Children.objects.filter(Group=pk)
    access = request.user.groups.filter(name="Старший воспитатель").exists() or \
             request.user.groups.filter(name="Заведующий").exists()
    topaccess = request.user.groups.filter(name="Заведующий").exists()
    if request.method == "POST":
        form = ChildrenForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.Group = Group
            instance.save()
    context = {
        'access': access,
        'group': Group,
        'list_children': list_children,
        'topaccess': topaccess,
        'form': ChildrenForm
    }
    return render(request, 'group/group_detail.html', context)


@login_required
def group_update(request, pk):
    get_group = ChildrenGroup.objects.get(pk=pk)
    if request.method == "POST":
        form = GroupForm(request.POST, instance=get_group)
        if form.is_valid():
            form.save()
    context = {
        'form': GroupForm(instance=get_group)
    }
    return render(request, 'group/group_update.html', context)


@login_required
def children_update(request, pk):
    get_children = Children.objects.get(pk=pk)
    if request.method == "POST":
        form = UpdateChildrenForm(request.POST, instance=get_children)
        if form.is_valid():
            form.save()
    context = {
        'get_children': get_children,
        'update': True,
        'form': UpdateChildrenForm(instance=get_children)
    }
    return render(request, 'children/children_update.html', context)


@login_required
def children_delete(request, pk):
    get_children = Children.objects.get(pk=pk)
    get_children.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def group_delete(request, pk):
    get_group = ChildrenGroup.objects.get(pk=pk)
    get_group.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

