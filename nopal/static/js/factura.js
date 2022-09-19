(()=>{
    let objecto = {}
    let contacto =   ()=>{
      //busco los valores de los campos de producto y precio
     let nombre_producto = document.querySelectorAll('#nombre_producto')
     let nombre_precio = document.querySelectorAll('#nombre_precio')
     let cantidad = document.querySelectorAll('#nombre_cantidad')
     //creo un objeto con los valores de los campos de producto y precio
     let contador = 0
     nombre_producto.forEach(item=>{
      objecto[item.textContent] =  [`con precio total ${ nombre_precio[contador].textContent}` ,  ` y con cantidad ${ cantidad[contador].textContent}` ]  
      contador++
     })
     console.log(objecto)
     
      //creo una tabla con los valores de los campos de producto y precio
     const productos = Object.entries(objecto).map((key) =>` ${key} `).join('');
     //creo un enlace para enviar el mensaje
      let mensaje = `https://api.whatsapp.com/send?phone=+573102881044&text= Supermercado El Nopal, quisiera por favor generar mi factura de la compra de los siguientes productos:${productos.replace(/,/g, ' ')}`
      console.log(mensaje)
      new Promise( (resolve, reject) =>{
          if(mensaje){
              //envio el mensaje con el enlace
              if (Object.keys(objecto).length > 0) {
                  location.href = mensaje;
                  resolve('procesando mensaje');
              }else{
                  reject('porfavor compre al menos un producto');
              }
          }else{
              reject('error al procesar mensaje')
          }
      } ).then( (mensaje) =>{alert(mensaje)} ).catch( (error) =>{alert(error)} )
      
  }
  let boton_factura = document.getElementById('agregar_factura')
  if(boton_factura){
      boton_factura.addEventListener('click' , ()=>{
          contacto()
      })
  }
})()