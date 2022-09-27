$(document).ready(function(){
  $("#myInput").on("keyup", function() {
    let value = $(this).val().toLowerCase();
    $(".myDIV .blog-inner").filter(function() {
      console.log($(this));
     let campos_agregar = $(this).text().toLowerCase().indexOf(value) > -1;
     console.log(campos_agregar);
      if(campos_agregar === false){
          document.getElementById('alerta_busqueda').style = 'display:block !important;'
      }else{
        document.getElementById('alerta_busqueda').style = 'display:none !important; '
        console.log(campos_agregar);
      }
      $(this).toggle(campos_agregar)
    });
  });
});
