from flask import Flask, render_template_string, request

app = Flask(__name__)

# Función matemática core (Pytest compatible)
def celsius_a_fahrenheit(celsius: float) -> float:
    return (celsius * 9/5) + 32

# URL del "Modelo" de imagen (Optimus Prime / Autobot)
ROBOT_MODEL_URL = "https://w7.pngwing.com/pngs/381/660/png-transparent-optimus-prime-transformers-bumblebee-autobot-decepticon-optimus-prime-fictional-character-action-figure-transformers.png"

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AUTOBOT - Matrix Calculator</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&family=Rajdhani:wght@500;700&display=swap" rel="stylesheet">
    
    <style>
        :root {
            --cyber-blue: #00f0ff;
            --cyber-red: #ff0055;
            --matrix-dark: #0a0c10;
        }

        body {
            background-color: var(--matrix-dark);
            background-image: radial-gradient(circle at 50% 50%, rgba(0, 240, 255, 0.1) 0%, transparent 80%);
            height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            font-family: 'Rajdhani', sans-serif;
            color: white;
            margin: 0;
            overflow: hidden;
        }

        .transformer-panel {
            background: rgba(16, 20, 28, 0.9);
            border: 2px solid #1a2333;
            border-radius: 15px;
            padding: 2.5rem;
            max-width: 500px;
            width: 90%;
            backdrop-filter: blur(15px);
            box-shadow: 0 0 50px rgba(0, 240, 255, 0.2);
            text-align: center;
            position: relative;
        }

        /* Contenedor del "Modelo" de imagen */
        .model-container {
            width: 180px;
            height: 180px;
            margin: 0 auto 1.5rem;
            background: radial-gradient(circle, rgba(0,240,255,0.2) 0%, transparent 70%);
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            border: 1px solid rgba(0, 240, 255, 0.3);
        }

        .model-image {
            max-width: 140px;
            max-height: 140px;
            filter: drop-shadow(0 0 10px var(--cyber-blue));
        }

        h1 {
            font-family: 'Orbitron', sans-serif;
            font-size: 1.5rem;
            letter-spacing: 3px;
            color: var(--cyber-blue);
            margin-bottom: 1rem;
        }

        .cyber-input {
            background: #000 !important;
            border: 1px solid var(--cyber-blue) !important;
            color: white !important;
            font-family: 'Orbitron', sans-serif;
            text-align: center;
        }

        .btn-cyber {
            background: transparent;
            border: 2px solid var(--cyber-red);
            color: white;
            font-family: 'Orbitron', sans-serif;
            width: 100%;
            margin-top: 1rem;
            transition: 0.3s;
        }

        .btn-cyber:hover {
            background: var(--cyber-red);
            box-shadow: 0 0 20px var(--cyber-red);
        }

        .result-hud {
            margin-top: 1.5rem;
            padding: 10px;
            border-left: 4px solid var(--cyber-blue);
            background: rgba(0, 240, 255, 0.05);
            text-align: left;
        }
    </style>
</head>
<body>

    <div class="transformer-panel">
        <div class="model-container">
            <img src="{{ robot_img }}" class="model-image" alt="Core Model">
        </div>
        
        <h1>MATRIX CALCULATOR</h1>
        
        <form method="POST">
            <input type="number" step="any" name="celsius" class="form-control cyber-input" placeholder="INGRESE CELSIUS" required value="{{ celsius_enviado }}">
            <button type="submit" class="btn btn-cyber">PROCESAR VECTOR 🔄</button>
        </form>

        {% if resultado is not none %}
            <div class="result-hud">
                <small style="color: var(--cyber-blue)">TELEMETRÍA:</small><br>
                {{ celsius_enviado }}°C ➔ <strong>{{ resultado }}°F</strong>
            </div>
        {% endif %}
    </div>

</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def home():
    resultado = None
    celsius_enviado = ""
    if request.method == 'POST':
        try:
            celsius_enviado = request.form.get('celsius', '').strip()
            if celsius_enviado:
                resultado = celsius_a_fahrenheit(float(celsius_enviado))
        except ValueError:
            resultado = "ERR_VECTOR"
            
    return render_template_string(HTML_TEMPLATE, 
                                 resultado=resultado, 
                                 celsius_enviado=celsius_enviado,
                                 robot_img=ROBOT_MODEL_URL)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)

He echado un vistazo a tu código y he preparado esta presentación técnica para mostrarte cómo integrar correctamente la imagen del robot y mejorar la estructura. ¡Espero que te sea de gran ayuda!