from django.contrib import admin
from .models import Carousel, Category, Post


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name_uz',
        'name_ru'
    ]


@admin.action(description="Faollashtirish")
def carousel_status_active(modeladmin, request, queryset):
    queryset.update(status=Carousel.STATUS_ACTIVE)


@admin.action(description="Nofaollashtirish")
def carousel_status_inactive(modeladmin, request, queryset):
    queryset.update(status=Carousel.STATUS_INACTIVE)


# carousel_status_inactive.short_description = "Faol qilish"


@admin.register(Carousel)
class CarouselAdmin(admin.ModelAdmin):
    actions = [
        carousel_status_active, carousel_status_inactive
    ]

    list_display = [
        'id',
        'header',
        'status',
        'order'
    ]

    def get_action_choices(self, request):
        default_choise = [("", "None")]
        return super().get_action_choices(request, default_choise)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'user',
        'subject_uz',
        'subject_ru'
    ]

    fields = [
        'subject_uz',
        'subject_ru',
        'content_uz',
        'content_ru'
    ]
