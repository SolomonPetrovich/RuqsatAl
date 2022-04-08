from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'main/index.html')


def contact(request):
    return render(request, 'main/Contact_Us.html')


def about(request):
    return render(request, 'main/about.html')


def e_ticket(request):
    return render(request, 'main/e-ticket.html')


def sign_in(request):
    return render(request, 'main/sign_in.html')


def ticket_booking(request):
    return render(request, 'main/ticket-booking.html')


def seat_seat(request):
    return render(request, 'main/seat_sel.html')


def movies(request):
    return render(request, 'main/movies.html')