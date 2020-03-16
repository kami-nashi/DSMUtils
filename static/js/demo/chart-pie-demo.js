// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#292b2c';

$.getJSON("http://journal.kami-nashi.com/skatetrax.maintenance/overview.php", function(jsonFromFile) {
  let hoursMaintSkated = jsonFromFile[0].hours_maint_skated;
  let hoursMaintRemaining = jsonFromFile[0].hours_maint_remaining;
  let hoursMaintCost = jsonFromFile[0].cost_maint_total;
  // Pie Chart Example
  let ctx = document.getElementById("myPieChart");
  let myPieChart = new Chart(ctx, {
    type: 'doughnut',
    data: {
      labels: ["Time On", "Time Remaining"],
      datasets: [{
        data: [hoursMaintSkated, hoursMaintRemaining],
        backgroundColor: ["#009900", "#70db70"],
      }],
    },
    options: {
      rotation: Math.PI * -0.5
    }
  });

  $('#hoursSkated').html('' + hoursMaintSkated);
  $('#hoursRemaining').html('' + hoursMaintRemaining);
  $('#hoursCost').html('$' + hoursMaintCost);
});
