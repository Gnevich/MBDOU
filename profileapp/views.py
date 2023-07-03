from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User, Group
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render
from djangoProject.forms import UserForm, ProfileForm, UserGroupUpdateForm
from profileapp.models import Profile


def index(request):
    """View function for home page of site."""
    return render(request, 'index.html')


@login_required
def profile(request):
    access = request.user.groups.filter(name="Старший воспитатель").exists() \
             or request.user.groups.filter(name="Заведующий").exists()
    topaccess = request.user.groups.filter(name="Заведующий").exists()
    context = {
        'access': access,
        'topaccess': topaccess
    }
    return render(request, 'users/profile.html', context)




@login_required
@permission_required('Заведующий')
def users(request):
    access = request.user.groups.filter(name="Старший воспитатель").exists() \
             or request.user.groups.filter(name="Заведующий").exists()
    topaccess = request.user.groups.filter(name="Заведующий").exists()

    if request.method == "POST":
        UForm = UserForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if UForm.is_valid() and profile_form.is_valid():
            user = UForm.save()
            user.groups.add(UForm.data.get('group'))
            user.refresh_from_db()  # load the profile instance created by the signal
            profile_form = ProfileForm(request.POST,
                                       instance=user.profile)  # Reload the profile form with the profile instance
            profile_form.full_clean()  # Manually clean the form this time. It is implicitly called by "is_valid()" method
            profile_form.save()  # Gracefully save the form

    user_list = User.objects.filter(~Q(groups=0))

    context = {
        'user_list': user_list,
        'access': access,
        'topaccess': topaccess,
        'UserForm': UserForm(),
        'ProfileForm': ProfileForm(),
    }
    return render(request, 'users/users.html', context)


@login_required
@permission_required('Заведующий')
def user_delete(request, pk):
    get_group = User.objects.get(pk=pk)
    get_group.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required
@permission_required('Заведующий')
def user_detail(request, pk):
    UserInfo = User.objects.get(id=pk)
    context = {
        'UserInfo': UserInfo,
    }
    return render(request, 'users/user_info.html', context)


@login_required
@permission_required('Заведующий')
def user_update(request, pk):
    UserInfo = User.objects.get(id=pk)
    ProfileInfo = Profile.objects.get(id=pk)
    if request.method == "POST":
        Uform = UserGroupUpdateForm(request.POST, instance=UserInfo)
        Pform = ProfileForm(request.POST, instance=ProfileInfo)
        if Pform.is_valid() and Uform.is_valid():
            groups_pk = Uform.cleaned_data['group']
            group_pk = Group.objects.all().get(name=groups_pk)
            groups = Group.objects.filter(pk=group_pk.id)
            UserInfo.groups.set(groups)
            Uform.save()
            Pform.save()
    context = {
        'UserForm': UserGroupUpdateForm(instance=UserInfo),
        'ProfileForm': ProfileForm(instance=ProfileInfo),
    }
    return render(request, 'users/user_update.html', context)



