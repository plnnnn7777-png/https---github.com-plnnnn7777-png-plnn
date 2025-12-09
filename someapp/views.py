from django.shortcuts import get_object_or_404, render

from .models import Service


def home(request):
    """Landing page showing services and intro."""
    all_services = Service.objects.all()
    return render(
        request,
        "someapp/home.html",
        {"services": all_services},
    )


def service_detail(request, slug: str):
    """Detailed view for a single service."""
    service = get_object_or_404(Service, slug=slug)
    related = Service.objects.exclude(id=service.id)[:3]
    return render(
        request,
        "someapp/service_detail.html",
        {"service": service, "related_services": related},
    )
