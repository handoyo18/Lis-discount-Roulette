import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Roulette Wheel", layout="wide")

# Force entire background to light blue
st.markdown(
    """
    <style>
        body, .stApp {
            background-color: #add8e6 !important;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Page Title
st.markdown("<h1 style='text-align: center;'>🎯 Spin the Wheel!</h1>", unsafe_allow_html=True)

# Roulette Wheel HTML + JS
html_code = """
<!DOCTYPE html>
<html>
<head>
  <style>
    html, body {
      margin: 0;
      padding: 0;
      height: 100%;
      font-family: 'Segoe UI', sans-serif;
    }

    .container {
      display: flex;
      justify-content: center;
      align-items: center;
      gap: 40px;
    }

    .wheel-box {
      position: relative;
      width: 350px;
      height: 350px;
    }

    .pointer {
      position: absolute;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -172px); /* Move inside the wheel */
      width: 0;
      height: 0;
      border-left: 20px solid transparent;
      border-right: 20px solid transparent;
      border-bottom: 30px solid #e53935;
      z-index: 10;
    }

    .wheel {
      width: 100%;
      height: 100%;
      border-radius: 50%;
      border: 8px solid #fff;
      box-shadow: 0 0 20px rgba(0,0,0,0.3);
      transform-origin: center center;
    }

    .button-container {
      text-align: center;
      margin-top: 20px;
    }

    #spin {
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
      width: 220px;
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
    <div>
      <div class="wheel-box">
        <div class="pointer"></div>
        <canvas id="wheelCanvas" class="wheel" width="350" height="350"></canvas>
      </div>
      <div class="button-container">
        <button id="spin">🎲 SPIN</button>
      </div>
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
    let currentRotation = 0;

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
      const spinAngle = Math.random() * 360 + 1440; // spin multiple full turns
      currentRotation += spinAngle;

      canvas.style.transition = "transform 4s ease-out";
      canvas.style.transform = `rotate(${currentRotation}deg)`;

      setTimeout(() => {
        const normalized = currentRotation % 360;
        const index = Math.floor(normalized / (360 / slices));
        const result = prizes[(slices - index) % slices];
        resultBox.innerHTML = "🎉 You got:<br><strong>" + result + "</strong>";
      }, 4000);
    });
  </script>
</body>
</html>
"""

components.html(html_code, height=650)
