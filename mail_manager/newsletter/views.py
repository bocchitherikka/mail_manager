from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from .models import User, Newsletter


@login_required
def index(request):
    template = 'templates/index.html'
    user = request.user
    newsletters = Newsletter.objects.filter(

    )
    context = {
        'user': user,
        'newsletters': newsletters
    }
    return render(request, template, context)
