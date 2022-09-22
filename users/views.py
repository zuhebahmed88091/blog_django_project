from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm

def register(request):
    if request.method == "POST":
        # form = UserCreationForm(request.POST)
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            # messages.success(request, f'Account created for {username}!')
            messages.success(request, f'Your Account Has Been Created! You Are Now Able To Log In')
            return redirect('login')
            # return redirect('blog-home')
    else:
        # form = UserCreationForm()
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form':form})


# messages.warning
# messages.error
# messages.info
# messages.success
# messages.debug

