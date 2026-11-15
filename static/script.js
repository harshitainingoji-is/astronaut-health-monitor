const chart = document.getElementById("healthChart");

if (chart) {
    new Chart(chart, {
        type: "line",
        data: {
            labels: ["08:00", "10:00", "12:00", "14:00", "16:00", "18:00"],
            datasets: [{
                label: "Heart Rate (BPM)",
                data: [70, 74, 72, 78, 75, 72],
                borderColor: "#45d6ed",
                backgroundColor: "rgba(69,214,237,0.15)",
                fill: true,
                tension: 0.4
            }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: {
                    labels: { color: "#e8f1ff" }
                }
            },
            scales: {
                x: {
                    ticks: { color: "#a9bad0" }
                },
                y: {
                    ticks: { color: "#a9bad0" }
                }
            }
        }
    });
}
