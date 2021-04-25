from django.contrib import admin

from coaches.models import Coach

# admin.site.register(Coach)

@admin.register(Coach)
class CoachAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'last_name', 'role', 'phone', 'email', 'created', 'modified')
    list_display_links = ('id', 'name', 'last_name', 'role')
    list_editable = ('phone', )
    search_fields = (
        # 'coach__id',
        'coach__username',
        'coach__email',
        'coach__last_name',
        'phone',
        'role',
        'location',
        )
    # fieldsets = (
    #     ('Coach', {
    #         'fields': (('name', 'last_name'),),
    #     }),
    #     ('Extra info', {
    #         'fields': (
    #             ('role',),
    #             ('created',)
    #             )
    #     }),
    #     ('Metadata', {
    #         'fields': (('modified',))
    #     })
    # )

    readonly_fields = ('created', 'modified',)