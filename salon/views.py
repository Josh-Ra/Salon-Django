from django.shortcuts import render, redirect
from .forms import StylistRegisterForm, BookingForm, ContactForm
from .models import stylist, services
from django.core.mail import send_mail
from .forms import ContactForm
from django.views.decorators.csrf import csrf_protect


# Create your views here.
def home(request):
    return render(request, "home.html")


def about(request):
    stylists = stylist.objects.all()
    return render(request, "about.html", context={"stylists": stylists})


def whatwedo(request):
    service = services.objects.all()
    return render(request, "services.html", context={"services": service})

@csrf_protect
def booking(request):
    form = BookingForm(request.POST)
    if form.is_valid():
        booking = form.save()
        return redirect("home")
    else:
        form = BookingForm()
    return render(request, "booking.html", {"form": form})


def contact(request):
    form = ContactForm(request.POST)
    if form.is_valid():
        name = form.cleaned_data["name"]
        email = form.cleaned_data["email"]
        description = form.cleaned_data["description"]
        

        subject = "New Contact Us Submission"
        message_body = f"Name: {name}\nEmail: {email}\nMessage:\n{description}"
        from_email = "testemail@veno.com"
        to_email = ["testemail@test.com"]

        send_mail(subject, message_body, from_email, to_email, fail_silently=False)
        return redirect("home")
    else:
        form = ContactForm()
    return render(request, "contact.html", {"form": form})


def registerStylist(request):
    form = StylistRegisterForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        return render(request, "home.html")
    else:
        form = StylistRegisterForm()
        return render(request, "stylistregister.html", {"form": form})
