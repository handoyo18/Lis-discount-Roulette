import streamlit as st
import streamlit.components.v1 as components

# Set page config
st.set_page_config(page_title="Roulette Wheel", layout="centered")

# Title
st.markdown("<h1 style='text-align: center;'>🎯 Spin the Wheel!</h1>", unsafe_allow_html=True)

# HTML + CSS + JS for the wheel
html_code = """
<!DOCTYPE html>
<html>

<head>
    <style>
        body {
            background-color: #add8e6;
            /* 🔹 Light blue background */
            text-align: center;
            font-family: 'Segoe UI', sans-serif;
        }

        .wheel-container {
            position: relative;
            margin: 20px auto;
            width: 300px;
            height: 300px;
        }

        .wheel {
            width: 300px;
            height: 300px;
            border-radius: 50%;
            border: 8px solid #ffffff;
            box-shadow: 0 0 20px rgba(0, 0, 0, 0.3);
        }

        .wheel:before {
            content: '';
            position: absolute;
            top: -25px;
            left: 50%;
            transform: translateX(-50%);
            width: 0;
            height: 0;
            border-left: 20px solid transparent;
            border-right: 20px solid transparent;
            border-bottom: 30px solid #e53935;
            /* 🔺 Pointer color */
        }

        #spin {
            margin-top: 20px;
            padding: 12px 24px;
            font-size: 18px;
            color: white;
            background-color: #1976d2;
            /* 🔵 Button color */
            border: none;
            border-radius: 6px;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }

        #spin:hover {
            background-color: #1565c0;
        }
    </style>
</head>

<body>

    <div class="wheel-container">
        <canvas id="wheelCanvas" class="wheel" width="300" height="300"></canvas>
    </div>
    <button id="spin">🎲 SPIN</button>

    <script>
        const canvas = document.getElementById("wheelCanvas");
        const ctx = canvas.getContext("2d");

        const prizes = ["Nendoroid", "Figma", "Try Again", "Voucher", "Mystery Box", "Scale Figure"];
        const colors = ["#f44336", "#4caf50", "#ffeb3b", "#2196f3", "#ff9800", "#9c27b0"];
        const slices = prizes.length;
        const arc = Math.PI * 2 / slices;

        function drawWheel() {
            for (let i = 0; i < slices; i++) {
                ctx.beginPath();
                ctx.moveTo(150, 150);
                ctx.arc(150, 150, 140, i * arc, (i + 1) * arc);
                ctx.fillStyle = colors[i % colors.length];
                ctx.fill();
                ctx.save();
                ctx.translate(150, 150);
                ctx.rotate(i * arc + arc / 2);
                ctx.textAlign = "right";
                ctx.fillStyle = "#000";
                ctx.font = "14px sans-serif";
                ctx.fillText(prizes[i], 130, 5);
                ctx.restore();
            }
        }

        drawWheel();

        document.getElementById("spin").addEventListener("click", () => {
            const spinAngle = Math.random() * 360 + 720; // Minimum 2 full spins
            canvas.style.transition = "transform 4s ease-out";
            canvas.style.transform = `rotate(${spinAngle}deg)`;

            setTimeout(() => {
                const normalized = (spinAngle % 360);
                const index = Math.floor((360 - normalized) / (360 / slices)) % slices;
                alert("🎉 You got: " + prizes[index]);
            }, 4000);
        });
    </script>
</body>

</html>
"""

# Render the wheel inside the app
components.html(html_code, height=480)
