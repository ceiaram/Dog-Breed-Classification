function displayChart(prediction) {
  const ctx = document.getElementById("my-chart");
  const prediction_labels = [];
  const prediction_probs = [];
  const LIMIT = 10;

  // Append the top 10 dog breed labels and predictions to a list to be displayed
  for (let i = 0; i < LIMIT; i++) {
    prediction_labels.push(prediction[i][0]);
    prediction_probs.push(prediction[i][1]);
  }

  // console.log(prediction_labels);
  // console.log(prediction_probs);

  new Chart(ctx, {
    type: "doughnut",
    data: {
      labels: prediction_labels,
      datasets: [
        {
          data: prediction_probs,
          borderWidth: 1,
        },
      ],
    },

    options: {
      title: {
        display: true,
        text: "Top Predictions",
      },
    },
  });
}
