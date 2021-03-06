// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#292b2c';

var myLineChart;
var chartLabels = [];
var timestamp = [];
var rpm = [];
var airflow = [];
var fronto2 = [];
var timing = [];
var inttemp = [];
var cooltemp = [];
var knockret = [];
var speed = [];
var throtpos = [];

/**
 *
 */
var getJSON = function(url, callback) {
  var xhr = new XMLHttpRequest();
  xhr.open('GET', url, true);
  xhr.responseType = 'json';
  xhr.onload = function() {
    var status = xhr.status;
    if (status === 200) {
      callback(null, xhr.response);
    } else {
      callback(status, xhr.response);
    }
  };
  xhr.send();
};

getJSON(api_url, function(err, data) {
  if (err !== null) {
    alert('Something went wrong: ' + err);
  } else {
    for (let i=0; i<data.length; ++i) {
      chartLabels.push(data[i].timestamp);
      rpm.push(Number.parseFloat(data[i].rpm));
      airflow.push(Number.parseFloat(data[i].airflow));
      fronto2.push(Number.parseFloat(data[i].fronto2));
      timing.push(Number.parseFloat(data[i].timing));
      inttemp.push(Number.parseFloat(data[i].inttemp));
      cooltemp.push(Number.parseFloat(data[i].cooltemp));
      knockret.push(Number.parseFloat(data[i].knockret));
      speed.push(Number.parseFloat(data[i].speed));
      throtpos.push(Number.parseFloat(data[i].throtpos));
    }

    myLineChart = new Chart(document.getElementById("myAreaChart"), {
      type: 'line',
      data: {
        labels: chartLabels,
        datasets: [{
          label: "RPM",
          lineColor: "DarkGreen",
          lineTension: 0.3,
          backgroundColor: "rgba(2,117,216,0.2)",
              borderColor: "rgba(2,117,216,1)",
              pointRadius: 1,
              pointBackgroundColor: "rgba(2,117,216,1)",
              pointBorderColor: "rgba(255,255,255,0.8)",
              pointHoverRadius: 2,
              pointHoverBackgroundColor: "rgba(2,117,216,1)",
              pointHitRadius: 35,
              pointBorderWidth: 1,
      	      yAxisID: 'RPM',
              data: rpm,
            },
          {
          label: "Front o2",
          lineColor: "Red",
          lineTension: 0.3,
//          backgroundColor: "rgba(2,117,216,0.2)",
              borderColor: "rgba(2,117,216,1)",
              pointRadius: 1,
              pointBackgroundColor: "rgba(2,117,216,1)",
              pointBorderColor: "rgba(255,255,255,0.8)",
              pointHoverRadius: 2,
              pointHoverBackgroundColor: "rgba(2,117,216,1)",
              pointHitRadius: 35,
              pointBorderWidth: 1,
              yAxisID: 'fronto2',
              data: fronto2,
            },
            {
            label: "Timing",
            lineColor: "DarkCyan",
            lineTension: 0.3,
//            backgroundColor: "rgba(2,117,216,0.2)",
                borderColor: "rgba(2,117,216,1)",
                pointRadius: 1,
                pointBackgroundColor: "rgba(2,117,216,1)",
                pointBorderColor: "rgba(255,255,255,0.8)",
                pointHoverRadius: 2,
                pointHoverBackgroundColor: "rgba(2,117,216,1)",
                pointHitRadius: 35,
                pointBorderWidth: 1,
                yAxisID: 'timing',
                data: timing,
              },
              {
              label: "Intake Temp",
              lineColor: "DarkOrange",
              lineTension: 0.3,
//              backgroundColor: "rgba(2,117,216,0.2)",
                  borderColor: "rgba(2,117,216,1)",
                  pointRadius: 1,
                  pointBackgroundColor: "rgba(2,117,216,1)",
                  pointBorderColor: "rgba(255,255,255,0.8)",
                  pointHoverRadius: 2,
                  pointHoverBackgroundColor: "rgba(2,117,216,1)",
                  pointHitRadius: 35,
                  pointBorderWidth: 1,
                  yAxisID: 'inttemp',
                  data: inttemp,
                },
                {
                label: "Coolant Temp",
                lineColor: "FireBrick",
                lineTension: 0.3,
//                backgroundColor: "rgba(2,117,216,0.2)",
                    borderColor: "rgba(2,117,216,1)",
                    pointRadius: 1,
                    pointBackgroundColor: "rgba(2,117,216,1)",
                    pointBorderColor: "rgba(255,255,255,0.8)",
                    pointHoverRadius: 2,
                    pointHoverBackgroundColor: "rgba(2,117,216,1)",
                    pointHitRadius: 35,
                    pointBorderWidth: 1,
                    yAxisID: 'cooltemp',
                    data: cooltemp,
                  },
                  {
                  label: "Knock Ret",
                  lineColor: "LightSalmon",
                  lineTension: 0.3,
//                  backgroundColor: "rgba(2,117,216,0.2)",
                      borderColor: "rgba(2,117,216,1)",
                      pointRadius: 1,
                      pointBackgroundColor: "rgba(2,117,216,1)",
                      pointBorderColor: "rgba(255,255,255,0.8)",
                      pointHoverRadius: 2,
                      pointHoverBackgroundColor: "rgba(2,117,216,1)",
                      pointHitRadius: 35,
                      pointBorderWidth: 1,
	              yAxisID: 'knockret',
                      data: knockret,
                    },
                    {
                    label: "Speed (MPH)",
                    lineColor: "MediumOrchid",
                    lineTension: 0.3,
//                    backgroundColor: "rgba(2,117,216,0.2)",
                        borderColor: "rgba(2,117,216,1)",
                        pointRadius: 1,
                        pointBackgroundColor: "rgba(2,117,216,1)",
                        pointBorderColor: "rgba(255,255,255,0.8)",
                        pointHoverRadius: 2,
                        pointHoverBackgroundColor: "rgba(2,117,216,1)",
                        pointHitRadius: 35,
                        pointBorderWidth: 1,
                        yAxisID: 'speed',
                        data: speed,
                      },
                      {
                      label: "Throttle Position (Percent)",
                      lineColor: "MidnightBlue",
                      lineTension: 0.3,
//                      backgroundColor: "rgba(2,117,216,0.2)",
                          borderColor: "rgba(2,117,216,1)",
                          pointRadius: 1,
                          pointBackgroundColor: "rgba(2,117,216,1)",
                          pointBorderColor: "rgba(255,255,255,0.8)",
                          pointHoverRadius: 2,
                          pointHoverBackgroundColor: "rgba(2,117,216,1)",
                          pointHitRadius: 35,
                          pointBorderWidth: 1,
                          yAxisID: 'throtpos',
                          data: throtpos,
                        },
            {
              label: "Air Flow",
              lineTension: 0.3,
//              backgroundColor: "rgba(141, 93, 162, 0.5)",
              borderColor: "rgb(142,94,162)",
              pointRadius: 1,
              pointBackgroundColor: "rgb(142,60,165)",
              pointBorderColor: "rgba(255,255,255,0.8)",
              pointHoverRadius: 2,
              pointHoverBackgroundColor: "rgba(2,117,216,1)",
              pointHitRadius: 35,
              pointBorderWidth: 1,
              yAxisID: 'airflow',
              data: airflow,
            }],
          },
          options: {
            display: false,
            scales: {
              xAxes: [{
                time: {
                  unit: 'date'
                },
                gridLines: {
                  display: false
                },
                ticks: {
                  maxTicksLimit: 8,
                  display: false
                }
              }],
              yAxes: [{
//                stacked: true,
              ticks: {
              min: 0,
              //max: Math.max.apply(Math, rpm)+0.5,
              maxTicksLimit: 5,
              display: false
            },
            gridLines: {
              color: "rgba(0, 0, 0, .125)",
            }
            },{
                id: 'RPM',
		            type: 'linear',
		            position: 'left',
                ticks: {display: false}
              },{
                id: 'speed',
                type: 'linear',
                position: 'left',
                ticks: {display: false}
              },{
                id: 'fronto2',
                type: 'linear',
                position: 'left',
                ticks: {display: false}
              },{
                id: 'inttemp',
                type: 'linear',
                position: 'left',
                ticks: {display: false}
              },{
                id: 'cooltemp',
                type: 'linear',
                position: 'left',
                ticks: {display: false}
              },{
                id: 'throtpos',
                type: 'linear',
                position: 'left',
                ticks: {display: false}
              },{
                id: 'knockret',
                type: 'linear',
                position: 'left',
                ticks: {display: false}
              },{
                id: 'timing',
                type: 'linear',
                position: 'left',
                ticks: {display: false}
	            },{
		            id: 'airflow',
		            type: 'linear',
		            position: 'left',
                ticks: {display: false}
	            }],
        },
        legend: {
          display: true
        }
          }
    });
  }
});
