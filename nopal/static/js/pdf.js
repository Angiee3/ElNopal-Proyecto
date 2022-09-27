const doc = new jsPDF();
let fecha = document.getElementById('fecha_reporte').textContent
let proveedor = document.getElementById('proveedor').textContent
let celular = document.getElementById('celular').textContent
let correo = document.getElementById('correo').textContent
let valorTotal = document.getElementById('valorTotal').textContent
console.log(fecha, proveedor, celular, correo, valorTotal);

document.querySelector('#botonReporte').addEventListener('click', ()=>{
    doc.autoTable({ html: '#my-table' })
    autoTable(doc, {
        head: [['Fecha', 'Proveedor', 'Celular', 'Correo', 'valorToatl']],
        body: [
          [`${fecha}`, `${proveedor}`, `${celular}`, `${correo}`, `${valorTotal}`],
        ],
      })
    // doc.save("reporte.pdf");
    
    let tabla =  document.getElementById('my-table')
    console.log(tabla);
    doc.save('table.pdf')
})

