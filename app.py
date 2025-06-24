import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Roulette Wheel", layout="wide")

st.markdown("<h1 style='text-align: center;'>🎯 Spin the Wheel!</h1>", unsafe_allow_html=True)

html_code = """
<!DOCTYPE html>
<html>
<head>
  <style>
    html, body {
      margin: 0;
      padding: 0;
      height: 100%;
      background-color: #add8e6; /* 🔹 Full-screen light blue */
      font-family: 'Segoe UI', sans-serif;
      display: flex;
      justify-content: center;
      align-items: center;
    }

    .container {
      display: flex;
      flex-direction: row;
      gap: 40px;
      align-items: center;
    }

    .wheel-container {
      position: relative;
      width: 350px;
      height: 350px;
    }

    .wheel {
      width: 100%;
      height: 100%;
      border-radius: 50%;
      border: 8px solid #fff;
      box-shadow: 0 0 20px rgba(0, 0, 0, 0.3);
      transform-origin: center;
    }

    .pointer {
      position: absolute;
      top: -30px;
      left: 50%;
      transform: translateX(-50%);
      width: 0;
      height: 0;
      border-left: 20px solid transparent;
      border-right: 20px solid transparent;
      border-bottom: 30px solid #e53935;
      z-index: 10;
    }

    #spin {
      margin-top: 20px;
      padding: 12px 24px;
      font-size: 18px;
      color: white;
      background-color: #1976d2;
      border: none;
      border-radius: 6px;
      cursor: pointer;
      transition: background-color 0.3s ease;
    }

    #spin:hover {
      background-color: #1565c0;
    }

    #result-box {
      width: 200px;
      min-height: 100px;
      background-color: white;
      border: 2px solid #333;
      border-radius: 8px;
      padding: 20px;
      font-size: 20px;
      color: #333;
      text-align: center;
      box-shadow: 0 4px 12px rgba(0,0,0,0.2);
    }
  </style>
</head>
<body>
  <div class="container">
    <div class="wheel-container">
      <div class="pointer"></div>
      <canvas id="wheelCanvas" class="wheel" width="350" height="350"></canvas>
      <button id="spin">🎲 SPIN</button>
    </div>
    <div id="result-box">🎁 Waiting to spin...</div>
  </div>

  <script>
    const canvas = document.getElementById("wheelCanvas");
    const ctx = canvas.getContext("2d");
    const resultBox = document.getElementById("result-box");

    const prizes = ["Nendoroid", "Figma", "Try Again", "Voucher", "Mystery Box", "Scale Figure"];
    const colors = ["#f44336", "#4caf50", "#ffeb3b", "#2196f3", "#ff9800", "#9c27b0"];
    const slices = prizes.length;
    const arc = Math.PI * 2 / slices;

    let currentAngle = 0;

    function drawWheel() {
      for (let i = 0; i < slices; i++) {
        ctx.beginPath();
        ctx.moveTo(175, 175);
        ctx.arc(175, 175, 160, i * arc, (i + 1) * arc);
        ctx.fillStyle = colors[i % colors.length];
        ctx.fill();
        ctx.save();
        ctx.translate(175, 175);
        ctx.rotate(i * arc + arc / 2);
        ctx.textAlign = "right";
        ctx.fillStyle = "#000";
        ctx.font = "16px sans-serif";
        ctx.fillText(prizes[i], 150, 5);
        ctx.restore();
      }
    }

    drawWheel();

    document.getElementById("spin").addEventListener("click", () => {
      const spinAngle = Math.random() * 360 + 1440; // 4+ spins
      canvas.style.transition = "transform 4s ease-out";
      canvas.style.transform = `rotate(${spinAngle + currentAngle}deg)`;

      setTimeout(() => {
        const finalAngle = (spinAngle + currentAngle) % 360;
        const index = Math.floor((360 - finalAngle + arc * 180 / Math.PI / 2) % 360 / (360 / slices)) % slices;
        const result = prizes[index];
        resultBox.innerHTML = "🎉 You got:<br><strong>" + result + "</strong>";
        currentAngle = (spinAngle + currentAngle) % 360;
      }, 4000);
    });
  </script>
</body>
</html>
"""

components.html(html_code, height=600)
