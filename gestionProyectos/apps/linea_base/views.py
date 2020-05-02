from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import LineaBaseForm
from .models import LineaBase
from apps.proyecto.models import Proyecto
from apps.tarea.models import Tarea
from django.contrib.auth.decorators import login_required


