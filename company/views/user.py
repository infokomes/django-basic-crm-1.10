from django.contrib.auth.decorators import login_required,permission_required
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from company.forms import AddUserForm, EditUserForm
from django.contrib.auth.models import User


@permission_required('user.is_superuser', login_url='login')
def user_list(request):
    users = User.objects.all()
    return render(request, 'user/user_list.html', {'users': users})

@login_required(login_url='login')
def user_details(request, pk):
    usera = get_object_or_404(User, pk=pk)
    if request.user.is_superuser:
        return render(request, 'user/user_details.html', {'user': usera})
    if request.user.pk == usera.pk:
        return render(request, 'user/user_details.html', {'user': usera})
    return redirect('home')


@permission_required('user.is_superuser', login_url='login')
def user_new(request):
    if request.method == "POST":
        form = AddUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.is_superuser = bool(request.POST.get('is_superuser'))
            user.save()
            return user_list(request)
    else:
        form = AddUserForm()
    return render(request, 'user/user_add.html', {'form': form})


@login_required(login_url='login')
def user_edit(request, pk):
    usera = get_object_or_404(User, pk=pk)
    if request.user.is_superuser:
        if request.method == "POST":
            form = EditUserForm(request.POST, instance=usera)
            if form.is_valid():
                usera = form.save(commit=True)
                usera.is_superuser = bool(request.POST.get('is_superuser'))

                password = str(request.POST.get('new_password'))
                if password:
                    usera.set_password(password)
                    usera.save()
                return user_list(request)
        else:
            form = EditUserForm(instance=usera)
        return render(request, 'user/user_edit.html', {'form': form})
    if request.user.pk == usera.pk:
        if request.method == "POST":
            form = EditUserForm(request.POST, instance=usera)
            if form.is_valid():
                usera = form.save(commit=True)
                password = str(request.POST.get('new_password'))
                if password:
                    usera.set_password(password)
                    usera.save()
                return render(request, 'user/user_details.html', {'user': usera})
        else:
            form = EditUserForm(instance=usera)
        return render(request, 'user/user_edit.html', {'form': form})
    return redirect('home')

@permission_required('user.is_superuser', login_url='login')
def user_delete(request, pk):
    User.objects.filter(pk=pk).delete()
    return user_list(request)
