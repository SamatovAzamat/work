from django.shortcuts import render, redirect, resolve_url
from django.views.generic import TemplateView
from .forms import RegistrationForm, LoginForm
from django.utils.translation import gettext_lazy as _
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout

def account_registration(request):
    request.page_title = _("Ro'yxatdan o'tish")
    request.button_title = request.page_title

    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()


            messages.success(request, _("Siz ro'yxatdan muvaffaqiyatli o'tdingiz!"))

            return redirect('main:index')

    return render(request, "account/registration.html", {
        'form': form
    })


def account_login(request):
    if request.user.is_authenticated or request.method != 'POST':
        return redirect('main:index')

    request.button_title = request.page_title = _("Tizimga kirish")

    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'],
                                password=form.cleaned_data['password'])

            if user is not None:

                login(request, user)

                messages.success(request, _("Xush kelibsiz, {}".format(user.username)))

                return redirect('main:index')

            # form.add_error('password', _("Login va/yoki parol noto'g'ri."))

    request.session['login_error'] = form.cleaned_data['username']

    # messages.error(request, _("Login va/yoki parol noto'g'ri."))

    return redirect(resolve_url("main:index") + "?modal=1")
    # return render(request, 'account/login.html', {
    #     'form': form
    # })



def account_logout(request):
    if not request.user.is_authenticated:
        return redirect('main:index')

    messages.success(request, _("Kelib turing, {}".format(request.user.username)))
    logout(request)

    return redirect('main:index')