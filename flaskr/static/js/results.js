function displayChart(prediction) {
  const prediction_labels = [];
  const prediction_probs = [];
  const LIMIT = 5;

  // Append the top 10 dog breed labels and predictions to a list to be displayed
  for (let i = 0; i < LIMIT; i++) {
    prediction_labels.push(prediction[i][0]);
    prediction_probs.push(prediction[i][1].toFixed(2));
  }

  displayBubbleChart(prediction_labels, prediction_probs);
  displayBarChart(prediction_labels, prediction_probs);
  // console.log(prediction_labels);
  // console.log(prediction_probs);
}

function displayBubbleChart(prediction_labels, prediction_probs) {
  const ctx = document.getElementById("my-bubble-chart");

  // Display doughnut chart
  new Chart(ctx, {
    type: "doughnut",
    data: {
      labels: prediction_labels,
      datasets: [
        {
          data: prediction_probs,
          borderWidth: 1,
          backgroundColor: ["#4b77a9", "#5f255f", "#d21243", "#B27200"],
        },
      ],
    },

    options: {
      responsive: true,
      maintainAspectRatio: true,
      plugins: {
        labels: {
          render: "percentage",
          fontColor: ["white", "white", "white", "white", "white"],
          precision: 2,
        },
      },
    },
  });
}
function displayBarChart(prediction_labels, prediction_probs) {
  const ctx = document.getElementById("my-bar-chart");

  // Display bar chart
  new Chart(ctx, {
    type: "bar",
    data: {
      labels: prediction_labels,
      datasets: [
        {
          label: "Predictions",
          data: prediction_probs,
          borderWidth: 1,
        },
      ],
    },
    options: {
      plugins: { labels: { render: "value" } },
      scales: {
        y: {
          beginAtZero: true,
          gridLines: {
            display: false,
          },
        },

        x: {
          gridLines: {
            display: false,
          },
        },
      },
    },
  });
}

function displayLocalStorageImage() {
  let image = document.getElementById("local-storage-image");
  let dataImage = localStorage.getItem("imageData");

  image.src = dataImage;
}
