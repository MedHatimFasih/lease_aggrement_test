from django.contrib.auth.forms import UserCreationForm 
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import LoginForm
from .models import Property
from django.shortcuts import get_object_or_404
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from .forms import CustomPasswordChangeForm
from .forms import PropertyForm
from .forms import ReservationForm
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm
from django.http import HttpResponseForbidden

def home(request):
    return render(request, 'home.html')


def room(request):
    return render(request, 'room.html')

def search_view(request):
    query = request.GET.get('query')
    # Logique de recherche basée sur 'query'
    context = {
        'query': query,
        # Autres données de contexte pour le template de résultats
    }
    return render(request, 'search_results.html', context)

def city_properties(request, city_name):
    # Logique pour récupérer et afficher les propriétés de la ville
    return HttpResponse(f"Propriétés pour la ville de {city_name}")


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.first_name = form.cleaned_data.get('first_name')
            user.last_name = form.cleaned_data.get('last_name')
            user.email = form.cleaned_data.get('email')
            user.phone_number = form.cleaned_data.get('phone_number')
            user.save()
            auth_login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Rediriger l'utilisateur vers une page après connexion
                return redirect('home')  # Remplacez 'home' par le nom de votre vue d'accueil
            else:
                messages.error(request, "Nom d'utilisateur ou mot de passe incorrect.")
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})

def profile_view(request):
    properties = Property.objects.filter(owner=request.user)
    context = {
        'properties': properties,
    }
    return render(request, 'profile.html', context)


def edit_profile(request):
    
    return render(request, 'base/edit_profile.html')

def change_password(request):
    if request.method == 'POST':
        form = CustomPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important, to keep the user logged in after password change
            return redirect('profile')
        else:
            for error in form.errors:
                print(error)
    else:
        form = CustomPasswordChangeForm(request.user)
    return render(request, 'change_password.html', {
        'form': form
    })

def delete_account_view(request):
    # Logique pour supprimer le compte de l'utilisateur
    if request.method == 'POST':
        # Code pour supprimer le compte
        request.user.delete()
        logout(request)  # Déconnexion de l'utilisateur après la suppression du compte
        return redirect('home')  # Redirection vers la page d'accueil ou une autre page

    return render(request, 'base/delete_account.html')

@login_required
def edit_profile(request):
    
    return render(request, 'edit_profile.html')

def logout_view(request):
    logout(request)
    return redirect('home')

def property_list(request):
    properties = Property.objects.all()
    return render(request, 'property_list.html', {'properties': properties})

def city_properties(request, city):
    properties = Property.objects.filter(city=city)
    return render(request, 'property_list.html', {'properties': properties, 'city': city})

def property_detail(request, pk):
    property = get_object_or_404(Property, pk=pk)
    return render(request, 'property_detail.html', {'property': property})


def add_property(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('property_success')
    else:
        form = PropertyForm()
    return render(request, 'add_property.html', {'form': form})

def property_success(request):
    return render(request, 'property_success.html')

def about(request):
    return render(request, 'about.html')

def faq(request):
    return render(request, 'faq.html')

def reservation_view(request):
    return render(request, 'reservation.html')

def reserve_property(request, property_id):
    property = get_object_or_404(Property, id=property_id)
    
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.property = property
            reservation.user = request.user
            reservation.save()
            return render(request, 'reservation_success.html', {'property': property})
    else:
        form = ReservationForm()

    return render(request, 'reservation.html', {'form': form, 'property': property})



