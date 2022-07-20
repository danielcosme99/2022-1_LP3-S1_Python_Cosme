from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
layout = """
    
"""
def index(request):
    estudiantes = ['Luis Serna',
                    'Antony Ccaccya',
                    'Miguel Yauricasa',
                    'Carlos Granados']
    
    return render(request, 'index.html',{
        'titulo':'Inicio',
        'mensaje': 'Proyecto Web con Django (Desde el view)',
        'estudiantes': estudiantes
    })

def saludo(request):
    return render(request, 'saludo.html',{
        'titulo':'Saludo',
        'autor_saludo':'Carlos Daniel Cosme Hernandez'
    })

def rango(request):
    a = 10
    b = 20
    rango_numeros = range(a, b+1)
    return render(request, 'rango.html',{
        'titulo':'Rango',
        'a': a,
        'b': b,
        'rango_numeros': rango_numeros
    })
    resultado = f"""
        <h2> Numéros de [{a},{b}] </h2>
        Resultado: <br>
        <ul>
    """
    while a<=b:
        resultado+= f"<li> {a} </li>"
        a+=1
    resultado+= "</ul>"
    return HttpResponse(layout + resultado)

def rango2(request, a=0, b=100):
    if a>b:
        return redirect('rango2',a=b,b=a)
    resultado = f"""
        <h2>Numeros de [{a},{b}]</h2>
    """
    resultado = f"""
        <h2> Numeros de  [{a},{b}] </h2>
        Resultado: <br>
        <ul>
    """
    while a<=b:
        resultado+= f"<li> {a} </li>"
        a+=1
    resultado+= "</ul>"
    return HttpResponse(layout + resultado)
