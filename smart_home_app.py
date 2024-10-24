
from flask import Flask, jsonify, render_template_string

app = Flask(__name__)

HTML_TEMPLATE = '''<!DOCTYPE html>
<html>
<head>
    <title>Smart Home Dashboard</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; }
        h1 { color: #333; }
        .device { margin: 10px 0; }
    </style>
</head>
<body>
    <h1>Smart Home Dashboard</h1>
    <div id="device-list"></div>
    <script>
        fetch('/api/devices')
            .then(response => response.json())
            .then(data => {
                const deviceList = document.getElementById('device-list');
                data.forEach(device => {
                    const div = document.createElement('div');
                    div.className = 'device';
                    div.textContent = `${device.name}: ${device.status}`;
                    deviceList.appendChild(div);
                });
            });
    </script>
</body>
</html>'''

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE)

@app.route('/api/devices', methods=['GET'])
def get_devices():
    devices = [{'name': 'Smart Light', 'status': 'off'}, {'name': 'Thermostat', 'status': 'on'}]
    return jsonify(devices)

if __name__ == '__main__':
    app.run(debug=True)
