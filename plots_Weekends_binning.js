var ratings = [];

for (var i = 0; i < weekends.length; i++) {
  // loop through the cities array, create a new marker, and push it to the cityMarkers array
  ratings.push(weekends[i].guest_satisfaction_overall);
}
console.log(ratings);


// Trace for the Data
let trace1 = {
  x: ratings,
    type: 'histogram',
    nbinsx: 20
};

// Data trace array
let traceData = [trace1];

// Apply title to the layout
let layout = {
title: "Weekends Ratings"
};

// Render the plot to the div tag with id "plot"
Plotly.newPlot("plot", traceData, layout);