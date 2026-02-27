function bootValidation() {
  const form = document.getElementById("pedForm");
  if (!form) return;

  form.addEventListener(
    "submit",
    function (event) {
      if (!form.checkValidity()) {
        event.preventDefault();
        event.stopPropagation();
      }
      form.classList.add("was-validated");
    },
    false
  );
}

function bootCharts() {
  if (!window.PED_RESULT) return;
  if (!window.Chart) return;

  const result = window.PED_RESULT;
  const demandCtx = document.getElementById("chartDemand");
  const pctCtx = document.getElementById("chartPct");
  if (!demandCtx || !pctCtx) return;

  const demandPoints = [
    { x: result.q1, y: result.p1 },
    { x: result.q2, y: result.p2 },
  ].sort((a, b) => a.x - b.x);

  new Chart(demandCtx, {
    type: "scatter",
    data: {
      datasets: [
        {
          label: "Observed points",
          data: demandPoints,
          borderColor: "#06b6d4",
          backgroundColor: "rgba(6, 182, 212, 0.9)",
          showLine: true,
          pointRadius: 5,
          pointHoverRadius: 7,
          tension: 0,
        },
      ],
    },
    options: {
      responsive: true,
      plugins: {
        legend: { display: false },
        tooltip: {
          callbacks: {
            label: (ctx) => `Q=${ctx.parsed.x}, P=${ctx.parsed.y}`,
          },
        },
      },
      scales: {
        x: {
          title: { display: true, text: "Quantity (Q)" },
          grid: { color: "rgba(148,163,184,0.14)" },
          ticks: { color: "#cbd5e1" },
        },
        y: {
          title: { display: true, text: "Price (P)" },
          grid: { color: "rgba(148,163,184,0.14)" },
          ticks: { color: "#cbd5e1" },
        },
      },
    },
  });

  new Chart(pctCtx, {
    type: "bar",
    data: {
      labels: ["%ΔPrice", "%ΔQuantity"],
      datasets: [
        {
          label: "Percent change",
          data: [result.pct_change_p, result.pct_change_q],
          backgroundColor: ["rgba(99,102,241,0.85)", "rgba(34,197,94,0.85)"],
          borderColor: ["#6366f1", "#22c55e"],
          borderWidth: 1,
        },
      ],
    },
    options: {
      responsive: true,
      plugins: {
        legend: { display: false },
        tooltip: {
          callbacks: {
            label: (ctx) => `${ctx.parsed.y}%`,
          },
        },
      },
      scales: {
        x: {
          grid: { display: false },
          ticks: { color: "#cbd5e1" },
        },
        y: {
          title: { display: true, text: "Percent (%)" },
          grid: { color: "rgba(148,163,184,0.14)" },
          ticks: { color: "#cbd5e1" },
        },
      },
    },
  });
}

document.addEventListener("DOMContentLoaded", () => {
  bootValidation();
  bootCharts();
});

