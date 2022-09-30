$(document).ready(function(){
  $("#myInput").on("keyup", function() {
    let value = $(this).val().toLowerCase();
    $(".myDIV .blog-inner").filter(function() {
      console.log($(this));
     let campos_agregar = $(this).text().toLowerCase().indexOf(value) > -1;
      $(this).toggle(campos_agregar)
    });
  });
});