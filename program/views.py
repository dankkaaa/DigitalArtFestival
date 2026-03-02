from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Event
from registrations.models import Registration

def program_list(request):
    fmt = request.GET.get("format", "").strip()
    upcoming = request.GET.get("upcoming", "1").strip()  # по умолчанию показываем будущие

    qs = Event.objects.all()
    if upcoming == "1":
        qs = qs.filter(starts_at__gte=timezone.now())

    if fmt:
        qs = qs.filter(format=fmt)

    return render(request, "program/list.html", {"events": qs, "fmt": fmt, "upcoming": upcoming})

def program_detail(request, pk: int):
    event = get_object_or_404(Event, pk=pk)
    is_registered = False
    if request.user.is_authenticated:
        is_registered = Registration.objects.filter(user=request.user, event=event).exists()

    return render(
        request,
        "program/detail.html",
        {"event": event, "is_registered": is_registered},
    )