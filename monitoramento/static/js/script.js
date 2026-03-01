
function criar_grafico(id_canvas, tipo, id_labels, id_dados, titulo, nome_grafico, cores) {

    const eixo_x = JSON.parse(document.getElementById(id_labels).textContent);  // eixo X
    const eixo_y = JSON.parse(document.getElementById(id_dados).textContent);  // eixo y
    
    const canvas = document.getElementById(id_canvas);
    new Chart(canvas, {
        type: tipo,
        data: {
            labels: eixo_x,
            datasets: [{
                label: titulo,
                data: eixo_y,
                backgroundColor: cores,
                borderRadius: 5,
                borderWidth: 0,
                hoverBorderWidth: 8,
            }]
        },
        
        options: {
            indexAxis: 'x', // deixa o grafico de barras na horixontal
            responsive: true,
            maintainAspectRatio: false,
            plugins : {
                title: { 
                    display: true,
                    text: nome_grafico,
                    color: 'black',
                    font: {
                        size: 30 
                    }
                },
                legend: {display: tipo !== 'bar'},
                datalabels: {
                    color: '#444',
                    anchor: 'end',
                    align: 'top',
                    font: {weight: 'bold'}
                }
            }
        }
    });
}

criar_grafico(
       'grafico_1', 
       'bar', 
       'eixo_x', 
       'eixo_y', 
       'Planejamentos no ano',
       'PLANAFS', 
       ['#198754', '#0d6efd', '#000000', '#dc3545', '#0dcaf0', '#6c757d']
   );
