from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def index(requiest):
    return render(requiest, 'core/index.html')


@login_required
def secrete(requiest):
    return render(requiest, 'core/secrete.html')
