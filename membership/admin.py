from django.contrib import admin

from .models import User, Billing, BillingPlan


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    search_fields = [
        'user_id',
    ]

    list_display = (
        'user_id',
    )


@admin.register(Billing)
class BillingAdmin(admin.ModelAdmin):
    pass


@admin.register(BillingPlan)
class BillingPlanAdmin(admin.ModelAdmin):
    pass
