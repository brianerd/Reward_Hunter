from django.contrib import admin
from .models import CreditCards

# Register your models here.
class Member_admin(admin.ModelAdmin):
    list_display = ("bank_name", "card_name")

admin.site.register(CreditCards, Member_admin)
