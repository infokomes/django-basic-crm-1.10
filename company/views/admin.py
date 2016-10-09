from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect


def choice_view(request):
    if request.user.is_authenticated:
        return render(request, 'company/index.html')
    return redirect('login')
