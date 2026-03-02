from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, get_object_or_404, render
from django.contrib import messages

from program.models import Event
from registrations.models import Registration


@login_required
def register_for_event(request, event_id: int):
    event = get_object_or_404(Event, id=event_id)

    obj, created = Registration.objects.get_or_create(
        user=request.user,
        event=event,
    )

    if created:
        messages.success(request, "Вы успешно записались на событие.")
    else:
        messages.info(request, "Вы уже записаны на это событие.")

    return redirect("program_detail", pk=event.id)


@login_required
def unregister_from_event(request, event_id: int):
    event = get_object_or_404(Event, id=event_id)

    deleted, _ = Registration.objects.filter(
        user=request.user,
        event=event
    ).delete()

    if deleted:
        messages.success(request, "Запись отменена.")
    else:
        messages.info(request, "Вы не были записаны.")

    return redirect("program:detail", pk=event.id)


@login_required
def my_registrations(request):
    regs = (
        Registration.objects
        .filter(user=request.user)
        .select_related("event")
        .order_by("-created_at")
    )

    return render(request, "registrations/my.html", {"regs": regs})