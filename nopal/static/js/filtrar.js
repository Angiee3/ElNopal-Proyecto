$(document).ready(function(){
  $("#myInput").on("keyup", function() {
    let value = $(this).val().toLowerCase();
    $(".myDIV .blog-inner").filter(function() {
     let campos_agregar = $(this).text().toLowerCase().indexOf(value) > -1 
      if(!campos_agregar){
       document.getElementById('alerta_busqueda').style = 'display:block !important;'
      }else{
        document.getElementById('alerta_busqueda').style = 'display:none !important; '
      }
      $(this).toggle(campos_agregar)
    });
  });
});