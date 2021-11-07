Chart.defaults.global.defaultFontColor = 'white'
var ctx = document.getElementById('myChart');
var myChart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: ['23/02', '15/03', '25/03', '04/04', '23/04', '07/05'],
        datasets: [{
            label: 'Peso (kg)',
            data: [94, 92, 92, 89, 86, 84],
            backgroundColor: 'rgba(158, 6, 6, 0.4)',
            borderColor: 'rgb(158, 6, 6)',
            lineTension: '0'
        }]
    },
    options: {
        scales: {
            yAxes: [{
                ticks: {
                    min: 50,
                    max: 120,
                },
                gridLines: {
                    color: 'rgba(0,0,0,0.9)'
                }
            }],
            xAxes: [{
                gridLines: {
                    offset: true,
                    color: 'rgba(0,0,0,0)'
                }
            }]
        },
    }
});

