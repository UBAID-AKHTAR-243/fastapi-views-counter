const BASE_URL = "https://counter-sks5.onrender.com"; // replace with your Render URL

async function loadViews(reelId) {
  const response = await fetch(`${BASE_URL}/views/${reelId}`);
  const data = await response.json();
  document.getElementById("view-count").innerText = data.views;
}

async function addView(reelId) {
  const response = await fetch(`${BASE_URL}/views/${reelId}`, { method: "POST" });
  const data = await response.json();
  document.getElementById("view-count").innerText = data.views;
}

// When page loads, increment and show views
addView("reel1");
