from django.contrib.auth.decorators import login_required
from django.shortcuts import  render, get_object_or_404
from polls.models import  Encuesta, Respuesta, Pregunta, PosibleRespuesta, OpcionElegida
from clientes.models import Cliente
from django.contrib import  messages

def index(request):
    encuestas = Encuesta.objects.all()
    return render(request,'polls/index.html',{'encuestas': encuestas})

@login_required()
def create(request, poll_id, client_id):
    encuesta = get_object_or_404(Encuesta, pk=poll_id)
    if(int(client_id) == 0):
        clientes = Cliente.objects.all().order_by('nombre')
    else:
        clientes = Cliente.objects.filter(pk=client_id).order_by('nombre')
        cliente = Cliente.objects.get(pk=client_id)
    posibles = []
    textos = {}
    if request.method == 'POST':
        respuestas = getDictArray(request.POST, poll_id)
        cliente = Cliente.objects.get(pk=request.POST.get('cliente_id'))
        for k,respuesta in respuestas.iteritems():
            # buscando la respuesta asociada a la pregunta
            p = Pregunta.objects.get(pk=k, encuesta__id = poll_id)
            if p:
                r = Respuesta.objects.filter(pregunta__id = p.id, cliente__id = cliente.id)[:1]
                if r:
                    r = r[0]
                    r.elegidas.all().delete()
                else:
                    r = Respuesta.objects.create(pregunta = p)
                elegidas = PosibleRespuesta.objects.filter(id__in = request.POST.getlist(poll_id+"["+str(k)+"]"+"[choice]") )
                if respuesta.has_key("add"):
                    r.texto = respuesta["add"]
                else:
                    r.texto = ''
                for elegida in elegidas:
                    opcion = OpcionElegida(elegida = elegida, respuesta = r)
                    r.elegidas.add(opcion)
                r.user = request.user
                r.cliente = cliente
                r.encuesta = encuesta
                r.save()
                messages.success(request, 'Encuesta almacenada satisfactoriamente.')
    try:
        preguntas = encuesta.preguntas.all()
        if cliente:
            for pregunta in preguntas:
                respuesta = Respuesta.objects.filter(pregunta__id = pregunta.id, cliente__id = cliente.id)[:1]
                if respuesta:
                    respuesta = respuesta[0]
                    for elegida in respuesta.elegidas.all():
                        posibles.append(elegida.elegida.id)
                    textos[respuesta.pregunta.id] = respuesta.texto
    except:
        pass
    return render(request, 'polls/create.html',
        {'encuesta': encuesta,'clientes':clientes,'client_id': int(client_id), 'elegidas':posibles,'textos':textos})


@login_required()
def polls(request, poll_id):
    encuesta = get_object_or_404(Encuesta, pk=poll_id)
    respts = Respuesta.objects.filter(encuesta__id = poll_id).order_by('creada')
    rids, respuestas = [],[]
    for r in respts:
        if r.cliente.id not in rids:
            rids.append(r.cliente.id)
            respuestas.append(r)
    return render(request, 'polls/polls.html', {'respuestas': respuestas, 'encuesta': encuesta})

def getDictArray(post, name):
    dic = {}
    for k in post.keys():
        if k.startswith(name):
            rest = k[len(name):]

            # split the string into different components
            parts = [p[:-1] for p in rest.split('[')][1:]
            print parts
            id = int(parts[0])

            # add a new dictionary if it doesn't exist yet
            if id not in dic:
                dic[id] = {}

            # add the information to the dictionary
            dic[id][parts[1]] = post.get(k)
    return dic