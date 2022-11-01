from email import message
from multiprocessing import context
from django.shortcuts import render, redirect
from mensajes.models import Mensaje
# Create your views here.

def lista_mensaje(request):
    mensaje_lista = Mensaje.objects.all()

    context = {
        'object_list' : mensaje_lista
    }

    return render(request, 'mensajes/lista.html',context)

def nuevo_mensaje(request):
    
    context = {}
    if request.method == 'POST':
        print("es post")

        #print(request.POST) Diccionario post

        texto = request.POST['mensaje']
        fecha = request.POST['fecha'] #Obtengo fecha, pero si el formulario no tiene nada, le pongo un valor por defecto

        if fecha == '':
            fecha = None

        Mensaje.objects.create(
            texto = texto,
            fecha = fecha
        )
        context.update({'mensaje': "Mensaje enviado correctamente"})

    return render(request,'mensajes/crear.html', context)


def actualizar_mensaje(request, pk):

    mensaje = Mensaje.objects.get(pk=pk) # select * from mensajes_mensaje where id = pk;

    context = {
        'object' : mensaje
    }

    if request.method == 'POST':
        print("es post")

        #print(request.POST) Diccionario post

        texto = request.POST['mensaje']
        fecha = request.POST['fecha'] #Obtengo fecha, pero si el formulario no tiene nada, le pongo un valor por defecto

        if fecha == '':
            fecha = None

        mensaje.texto = texto
        mensaje.fecha = fecha
        mensaje.save()

        context.update({'mensaje': "Mensaje enviado correctamente"})

    return render(request,'mensajes/actualizar.html', context)

    
def borrar_mensaje(request, pk):

    Mensaje.objects.get(pk=pk).delete() # select * from mensajes_mensaje where id = pk;

    context = {
        'mensaje' : "Borrado correctamente"
    }



    return redirect('lista_mensajes')