from django.contrib import admin

from Main.models import DataSetFile, Dataset  # isort: skip


@admin.register(Dataset)
class DatasetAdmin(admin.ModelAdmin):

    list_display = ("Name", "Sex", "Ticket", "Pclass")
    search_fields = ("Name", )
    ordering = ("Created", )


admin.site.register(DataSetFile)
