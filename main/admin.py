from django.contrib import admin
from .models import *


class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'original_title', 'original_language', 'popularity', 'release_date', 'vote_average', 'vote_count')
    list_display_links = ('id', 'title', 'original_title', 'original_language', 'popularity', 'release_date', 'vote_average', 'vote_count')
    search_fields = ('title',)


admin.site.register(User)
admin.site.register(Category)
admin.site.register(Booking)
admin.site.register(Hall)
admin.site.register(Seat)
admin.site.register(Session)
admin.site.register(Movie, MovieAdmin)
admin.site.register(Genres)
admin.site.register(Favorites)

