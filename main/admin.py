from django.contrib import admin
from .models import *

admin.site.register(User)
admin.site.register(Ticket)
admin.site.register(Booking)
admin.site.register(Hall)
admin.site.register(Seat)
admin.site.register(HallSeat)
admin.site.register(Session)
admin.site.register(Favorites)
admin.site.register(Category)
admin.site.register(Movie)
admin.site.register(Genres)
