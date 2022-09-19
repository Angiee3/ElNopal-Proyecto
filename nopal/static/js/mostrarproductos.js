$('.blog-inner').on('click', '.botonAgregar' , function(e){
    let $this = $(this)
    let imagen = $this.parents('.blog-inner').find('#modalimagen').attr('src')
    let nombre = $this.parents('.blog-inner').find('.card-title').text()
    let precio = $this.parents('.blog-inner').find('#precio_producto').text()
    let id =  $this.parents('.blog-inner').find('.id').text()
    let stock = $this.parents('.blog-inner').find('.stock').text()
    let description = $this.parents('.blog-inner').find('.descripcion').text()
    document.querySelector('#modalproduct .card-title').textContent = nombre
    document.querySelector('#modalproduct img').setAttribute('src', imagen)
    document.querySelector('#modalproduct #precio_modal').textContent = precio
    document.querySelector('#modalproduct #modal_description').textContent = description
    document.querySelector('#modalproduct #modal_stock').textContent = stock
    let enlace = `agregar/${id}`.replace(/ /g,'')
    document.querySelector('#modalproduct #agregar_carrito').setAttribute('href', enlace )
    $('#modalproduct').modal('show');
    e.preventDefault()
    return false;
}) 

