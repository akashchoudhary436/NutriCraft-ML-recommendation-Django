from django.contrib import admin
from .models import Food  # Import the Food model from your application's models
from .models import Contact
from .models import MealDRI

admin.site.register(Food)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('s_no', 'Name', 'Email', 'Subject', 'Message')


@admin.register(MealDRI)
class MealDRIAdmin(admin.ModelAdmin):
    list_display = ('meal_type', 'calories', 'protein', 'fat', 'carbohydrates')
