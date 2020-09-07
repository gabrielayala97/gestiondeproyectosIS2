from django.shortcuts import render, redirect
from django.contrib.auth import login as do_login
from django.contrib.auth import logout as do_logout
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
#from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from apps.usuario.forms import UsuarioForm, UsuarioEditForm
from apps.usuario.models import Usuario
from apps.rol.models import Rol
#from django.contrib.auth import get_user_model

# Vistas de creación de usuarios para el sistema
@login_required(login_url='/login')
def crear_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        form.fields['username'].help_text = None
        form.fields['password1'].help_text = None
        form.fields['password2'].help_text = None
        if form.is_valid():
            form.save()
            return redirect('/')
        return render(request, 'usuario/usuario_form.html',{'form': form})
    else:
        form = UsuarioForm()
        form.fields['username'].help_text = None
        form.fields['password1'].help_text = None
        form.fields['password2'].help_text = None
    return render(request, 'usuario/usuario_form.html',{'form': form})

#Vista de bienvenida-dashboard del sistema
@login_required(login_url='/login')     
def welcome(request):
    # Si estamos identificados devolvemos la portada
    if request.user.is_authenticated:
        return render(request, "usuario/welcome.html")
    # En otro caso redireccionamos al login
    return redirect('/login')
    
#Vista de inicio de sesión para usuarios del sistema
def login(request):
    # Creamos el formulario de autenticación vacío
    form = AuthenticationForm()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = AuthenticationForm(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():
            # Recuperamos las credenciales validadas
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Verificamos las credenciales del usuario
            user = authenticate(username=username, password=password)
            # Si existe un usuario con ese nombre y contraseña
            if user is not None:
                # Hacemos el login manualmente
                do_login(request, user)
                # Y le redireccionamos a la portada
                return redirect('/')

    # Si llegamos al final renderizamos el formulario
    return render(request, "usuario/login.html", {'form': form})

"""def register(request):
    # Creamos el formulario de autenticación vacío
    #User = get_user_model()
    form = UserCreationForm()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = UserCreationForm(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():

            # Creamos la nueva cuenta de usuario
            usuario = form.save()

            # Si el usuario se crea correctamente 
            if uusario is not None:
                # Hacemos el login manualmente
                #do_login(request, user)
                # Y le redireccionamos a la portada
                return redirect('/')

    # Si llegamos al final renderizamos el formulario
    return render(request, "usuario/register.html", {'form': form})
"""   
@login_required(login_url='/login')
def logout(request):
    # Finalizamos la sesión
    do_logout(request)
    # Redireccionamos a la portada
    return redirect('/login')

@login_required(login_url='/login')
def listar_usuario(request):
    usuario = Usuario.objects.all().order_by('id')
    contexto = {'usuarios': usuario}
    return render(request, 'usuario/usuario_list.html', contexto)

@login_required(login_url='/login')
def mostrar_perfil(request,id_usuario):
    usuario = Usuario.objects.get(id=id_usuario)
    contexto = {'usuario': usuario}
    return render(request, 'usuario/profile_user.html', contexto)

@login_required(login_url='/login')
def editar_usuario(request, id_usuario):
    # Recuperamos la instancia de la persona
    instancia = Usuario.objects.get(id=id_usuario)

    if request.method == "GET":
        # Actualizamos el formulario con los datos recibidos
        #form = UsuarioForm(instance=instancia)
        form = UsuarioEditForm(instance=instancia)
    else:
        #form = UsuarioForm(request.POST,instance=instancia)
        form = UsuarioEditForm(request.POST,instance=instancia)
        if form.is_valid():
            form.save()
        return redirect('/listar_usuarios')
    return render(request, 'usuario/usuario_form.html',{'form': form})

@login_required(login_url='/login')
def eliminar_usuario(request,id_usuario):
    usuario = Usuario.objects.get(id = id_usuario)
    usuario.delete()
    return redirect('/listar_usuarios')

#def asignar_rol()