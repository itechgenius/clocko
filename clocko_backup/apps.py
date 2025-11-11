from django.apps import AppConfig


class BackupConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "Clocko_backup"

    def ready(self):
        from django.urls import include, path

        from Clocko.urls import urlpatterns

        urlpatterns.append(
            path("backup/", include("Clocko_backup.urls")),
        )
        super().ready()

