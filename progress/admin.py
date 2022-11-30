from django.contrib import admin

from progress.models import Surah, Session, Progress

class ReadOnlyAdmin(admin.ModelAdmin):
    readonly_fields = []

    def get_readonly_fields(self, request, obj=None):
        return list(self.readonly_fields) + \
               [field.name for field in obj._meta.fields] + \
               [field.name for field in obj._meta.many_to_many]


    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class ProgressAdmin(admin.StackedInline):
    model = Progress


@admin.register(Surah)
class SurahAdmin(ReadOnlyAdmin):
    ordering = ('number',)
    list_display = ('number', 'name_ar', 'name_en', )



@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    inlines = [ ProgressAdmin ]
    list_display = ('student', 'attendance', 'date', 'created_at', )
