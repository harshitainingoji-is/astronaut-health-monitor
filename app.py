from flask import Flask, render_template
import random
from flask import Flask, render_template, jsonify
from monitor_data import get_astronaut_data

app = Flask(__name__)

@app.route("/")
def home():

    # Simulated astronaut health readings
    heart_rate = random.randint(60, 110)
    oxygen_level = random.randint(90, 100)
    body_temperature = round(random.uniform(36.0, 38.0), 1)
    blood_pressure = f"{random.randint(110, 130)}/{random.randint(70, 85)}"

    # Health status
    if heart_rate > 100 or oxygen_level < 95 or body_temperature > 37.5:
        health_status = "WARNING"
    else:
        health_status = "NORMAL"

    return render_template(
        "index.html",
        heart_rate=heart_rate,
        oxygen_level=oxygen_level,
        body_temperature=body_temperature,
        blood_pressure=blood_pressure,
        health_status=health_status
    )

if __name__ == "__main__":
    app.run(debug=True)