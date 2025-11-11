from django.apps import AppConfig


class ClockoApiConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "Clocko_api"

    def ready(self):
        from django.urls import include, path

        from Clocko.urls import urlpatterns

        urlpatterns.append(
            path("api/", include("Clocko_api.urls")),
        )
        super().ready()

