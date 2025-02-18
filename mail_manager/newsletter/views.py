from celery import shared_task
from datetime import datetime
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.template import Template, Context
from django.template.loader import render_to_string
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt

from .models import User, Newsletter, Subscriber


@login_required
def index(request):
    template = 'templates/index.html'
    return render(request, template)


@login_required
@csrf_exempt
def get_newsletters(request):
    newsletters = Newsletter.objects.filter(
        owner=request.user
    ).order_by('-id')
    newsletters_html = render_to_string(
        'templates/includes/newsletter.html',
        {'newsletters': newsletters}
    )
    return JsonResponse(
        {
            'newsletters': newsletters_html
        },
        safe=False
    )


@login_required
@csrf_exempt
def create_newsletter(request):
    if request.method == "POST":
        content = request.POST.get("content")
        name = request.POST.get("name")
        newsletter = Newsletter.objects.create(
            name=name,
            content=content,
            owner=request.user
        )
        return JsonResponse({
            "message": "Newsletter created successfully!",
            "id": newsletter.id
        })
    return JsonResponse(
        {"error": request.method + " method not allowed!"},
        status=400
    )


@login_required
@csrf_exempt
def edit_newsletter(request):
    if request.method == "POST":
        newsletter_id = request.POST.get("id")
        name = request.POST.get("name")
        content = request.POST.get("content")
        newsletter = get_object_or_404(
            Newsletter,
            id=newsletter_id,
            owner=request.user
        )
        newsletter.name = name
        newsletter.content = content
        newsletter.save()
        return JsonResponse({
            "message": "Newsletter edited successfully!"
        })
    return JsonResponse(
        {
            "error": request.method + " method not allowed!"
        },
        status=400
    )


@login_required
@csrf_exempt
def add_subscriber(request):
    if request.method == 'POST':
        name = request.POST.get('sub_name')
        surname = request.POST.get('sub_surname')
        email = request.POST.get('email')
        birth_date = request.POST.get('birth_date')
        newsletter_id = request.POST.get('newsletter_id')
        newsletter = Newsletter.objects.get(id=newsletter_id)
        subscriber_exists = Subscriber.objects.filter(
            email=email
        ).exists()
        if subscriber_exists:
            subscriber = Subscriber.objects.get(
                email=email
            )
        else:
            subscriber = Subscriber.objects.create(
                name=name,
                surname=surname,
                email=email,
                birth_date=birth_date
            )
        subscribed = subscriber in newsletter.subscribers.all()
        if subscribed:
            return JsonResponse({
                "message": "This email is already subscribed!"
            })
        newsletter.subscribers.add(subscriber)
        return JsonResponse({
            "message": "Successfully added new subscriber!"
        })
    return JsonResponse(
        {
            "error": request.method + " method not allowed!"
        },
        status=400
    )


@login_required
def is_newsletter_exists(request, newsletter_id):
    exists = Newsletter.objects.filter(id=newsletter_id).exists()
    return JsonResponse({
        "exists": exists
    })


@shared_task
def send_email_task(subject, template, context, recipient):
    template = Template(template)
    context = Context(context)
    html_message = template.render(context)
    send_mail(
        subject,
        ' ',
        settings.EMAIL_HOST_USER,
        [recipient],
        html_message=html_message
    )


def send_group_email(
        subject,
        template,
        recipient_list,
        countdown,
        eta
):
    for recipient in recipient_list:
        context = {
            "name": recipient.name,
            "surname": recipient.surname,
            "birth_date": recipient.birth_date.strftime('%Y-%m-%d')
        }
        email = recipient.email
        send_email_task.apply_async(
            args=[subject, template, context, email],
            countdown=countdown,
            eta=eta
        )


@login_required
@csrf_exempt
def launch_newsletter(request):
    if request.method == 'POST':
        newsletter_id = request.POST.get('newsletter_to_start_id')
        eta = request.POST.get('eta')
        countdown = request.POST.get('countdown')
        newsletter = get_object_or_404(
            Newsletter.objects.prefetch_related('subscribers'),
            id=newsletter_id
        )
        send_group_email(
            newsletter.name,
            newsletter.content,
            list(newsletter.subscribers.all()),
            int(countdown) if countdown else 0,
            datetime.strptime(eta, "%Y-%m-%d") if eta else timezone.now()
        )
        return JsonResponse({
            "message": "Successfully sent"
        })
    return JsonResponse(
        {
            "error": request.method + " method not allowed!"
        },
        status=400
    )
