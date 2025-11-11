from django.urls import include, path

urlpatterns = [
    path("auth/", include("Clocko_api.api_urls.auth.urls")),
    path("asset/", include("Clocko_api.api_urls.asset.urls")),
    path("base/", include("Clocko_api.api_urls.base.urls")),
    path("employee/", include("Clocko_api.api_urls.employee.urls")),
    path("notifications/", include("Clocko_api.api_urls.notifications.urls")),
    path("payroll/", include("Clocko_api.api_urls.payroll.urls")),
    path("attendance/", include("Clocko_api.api_urls.attendance.urls")),
    path("leave/", include("Clocko_api.api_urls.leave.urls")),
]

