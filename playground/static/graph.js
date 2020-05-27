var vis_data = document.getElementById('vis_data').value;
vis_data = JSON.parse(vis_data);
var col1 = document.getElementById('x_col').value;
var col2 = document.getElementById('y_col').value;



new Chart.Scatter(document.getElementById("myChart1"), {
    type: 'scatter',
    data: {
        datasets: [{
            label: 'Scatter Plot',
            data: vis_data,
            showLine: false,
            borderColor: "red",
            backgroundColor: "red"
            }]
        },
        options: {
            responsive: false,
            scales: {
                yAxes: [{
                    scaleLabel: {
                        display: true,
                        labelString: col2
                    }
                }],
                xAxes: [{
                    scaleLabel: {
                        display: true,
                        labelString: col1
                    }
                }]
            }
        }
    });