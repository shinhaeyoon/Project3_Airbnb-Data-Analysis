// Load the CSV data using PapaParse
Papa.parse('https://raw.githubusercontent.com/Shinhaeyoon/Project3/main/Resources/weekdays.csv', {
  download: true,
  header: true,
  complete: function(results) {
    // Process the data to calculate the average price per city
    var data = results.data;
    var averages = {};
    for (var i = 0; i < data.length; i++) {
      var city = data[i].loc;
      var price = parseFloat(data[i].realSum);
      if (!averages[city]) {
        averages[city] = {
          sum: price,
          count: 1
        };
      } else {
        averages[city].sum += price;
        averages[city].count++;
      }
    }
    var cityLabels = Object.keys(averages);
    var avgPrices = [];
    for (var i = 0; i < cityLabels.length; i++) {
      var city = cityLabels[i];
      var avg = averages[city].sum / averages[city].count;
      avgPrices.push(avg.toFixed(2));
    }
    
    // Create the Chart.js bar chart
    var ctx = document.getElementById('myChart').getContext('2d');
    var chart = new Chart(ctx, {
      type: 'bar',
      data: {
        labels: cityLabels,
        datasets: [{
          label: 'Average Room Rate Per City (Weekdays)',
          data: avgPrices,
          backgroundColor: 'rgba(54, 162, 235, 0.2)',
          borderColor: 'rgba(54, 162, 235, 1)',
          borderWidth: 1
        }]
      },
      options: {
        scales: {
          yAxes: [{
            ticks: {
              beginAtZero: true
            }
          }]
        }
      }
    });
  }
});
