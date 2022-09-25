// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#292b2c';

// Obtener una referencia al elemento canvas del DOM
const $graficas = document.querySelector("#graficas");
// Las etiquetas son las que van en el eje X. 


const MONTHS = [
  'Enero',
  'Febrero',
  'Marzo',
  'Abril',
  'Mayo',
  'Junio',
  'Julio',
  'Agosto',
  'Septiembre',
  'Octubre',
  'Noviembre',
  'Diciembre'
];
var dt = new Date();
function months(config) {
  var cfg = config || {};
  var count = cfg.count || 12;
  var section = cfg.section;
  var values = [];
  var i, value;

  for (i = 0; i < count; ++i) {
    value = MONTHS[Math.ceil(i) % 12];
    values.push(value.substring(0, section));
  }

  return values;
}

// Podemos tener varios conjuntos de datos. Comencemos con uno

const mesess = document.getElementById('entrega-mensual')

new Chart(mesess, {
  type: 'bar',// Tipo de gráfica
  data: {
      labels: months({count: dt.getMonth()+1}),
      datasets: [
        {
          label: "Ventas mensuales",
          data: $('#data-bar').html().slice(1,-1).split(','),
          backgroundColor: 'rgba(230, 57, 70, 0.1)', // Color de fondo
          borderColor: 'rgba(230, 57, 70)', // Color del borde
          borderWidth: 1.5,// Ancho del borde
          pointBackgroundColor: 'rgba(230, 57, 70, 0.3)',
          pointRadius: 5,
        },

      ]
  },
  
    options: { 
      plugins: {
          title: {
            display: true,
            text: 'Ventas mensuales'
          },
      },
      responsive: true,
      scales: {
        xAxes: [{
          stacked: true
        }],
          yAxes: [{
            stacked: true,
            ticks: {
              beginAtZero: true,
              min: 0,
              max: 200,
              maxTicksLimit: 5
            }
        }],
      },
  }
});
