from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from firstApp.models import Importacion

# Create your views here.
#Aqui comienzan las funciones de las importaciones.

def ImportacionData(request):
        importaciones = Importacion.objects.all()
        data = {'importaciones':importaciones}
        return render(request,'firstApp/lista-importaciones.html',data)
def CrearImportacionForm(request):
        return render(request,'firstApp/crear-importacion.html')
    #Aqui comienzan las formulas para manejar los datos.
    #prueba
def CrearImportacion(request):
        Cantidad_unidades_usd = float(request.POST['txt_cant_unidades'])
        costo_unitario_usd = float(request.POST['txt_costo_unitario'])
        costo_envio_usd = float(request.POST['txt_costo_envio'])
        nombre_articulo = request.POST['txt_nombre_art']
        nombre_proveedor = request.POST['txt_nombre_prov']
        codigo_articulo = request.POST['txt_codigo_art']
#Aqui comenzamos a calcular los datos requeridos.
        total_pedido_clp = (costo_unitario_usd * 890) * Cantidad_unidades_usd
        costo_envio_clp = costo_envio_usd * 890
        aduana_clp = (total_pedido_clp + costo_envio_clp) * 0.06
        iva_clp = (total_pedido_clp + costo_envio_clp) * 0.19
        aduana_mas_iva = aduana_clp + iva_clp
        costo_total_clp = total_pedido_clp + aduana_mas_iva
        costo_total_usd = costo_total_clp / 890
        importacion = Importacion(TotalPedidoCLP = total_pedido_clp, CostoEnvioCLP = costo_envio_clp, AduanaCLP= aduana_clp, IVAclp = iva_clp, AduanaMasIVACLP= aduana_mas_iva, CostoTotalCLP= costo_total_clp, CostoTotalUSD= costo_total_usd, NombreArticulo=nombre_articulo, NombreProveedor=nombre_proveedor, CodigoArticulo=codigo_articulo)
        importacion.save()
        importaciones = Importacion.objects.all()
        data = {'importaciones': importaciones}
        return render(request, 'firstApp/lista-importaciones.html', data)
#Aqui comenzamos con las opciones de eliminar y actualizar.
def eliminarImportacion(request, id):
    importacion = Importacion.objects.get(id = id)
    importacion.delete()
    return redirect('/importaciones')
def modificarImportacion(request,id):
    importacion = Importacion.objects.get(id = id)
    return render(request,'firstApp/actualizar-importacion.html', {'importacion':importacion})
def actualizarImportacion(request):
    id_importacion = float(request.POST['txt_id'])
    Cantidad_unidades_usd = float(request.POST['txt_cant_unidades'])
    costo_unitario_usd = float(request.POST['txt_costo_unitario'])
    costo_envio_usd = float(request.POST['txt_costo_envio'])
    nombre_articulo = request.POST['txt_nombre_art']
    nombre_proveedor = request.POST['txt_nombre_prov']
    codigo_articulo = request.POST['txt_codigo_art']
    total_pedido_clp = (costo_unitario_usd * 890) * Cantidad_unidades_usd
    costo_envio_clp = costo_envio_usd * 890
    aduana_clp = (total_pedido_clp + costo_envio_clp) * 0.06
    iva_clp = (total_pedido_clp + costo_envio_clp) * 0.19
    aduana_mas_iva = aduana_clp + iva_clp
    costo_total_clp = total_pedido_clp + aduana_mas_iva
    costo_total_usd = costo_total_clp / 890
    importacion = Importacion(TotalPedidoCLP = total_pedido_clp, CostoEnvioCLP = costo_envio_clp, AduanaCLP= aduana_clp, IVAclp = iva_clp, AduanaMasIVACLP= aduana_mas_iva, CostoTotalCLP= costo_total_clp, CostoTotalUSD= costo_total_usd, NombreArticulo=nombre_articulo, NombreProveedor=nombre_proveedor, CodigoArticulo=codigo_articulo, id = id_importacion)
    importacion.save()
    return redirect('/importaciones')














