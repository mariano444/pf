from flask import Flask, request, jsonify

app = Flask(__name__)

# Simulamos una base de datos de usuarios con sus contraseñas y número de usos restantes.
usuarios = {
    "usuario1": {"password": "password1", "uso_restante": 10},
    "usuario2": {"password": "password2", "uso_restante": 5},
}

@app.route("/login", methods=["POST"])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")
    
    if username in usuarios and usuarios[username]["password"] == password:
        return jsonify({"message": "Autenticado", "uso_restante": usuarios[username]["uso_restante"]})
    else:
        return jsonify({"message": "Credenciales incorrectas"}), 401

@app.route("/verificar_uso", methods=["POST"])
def verificar_uso():
    data = request.json
    username = data.get("username")
    password = data.get("password")
    
    if username in usuarios and usuarios[username]["password"] == password:
        if usuarios[username]["uso_restante"] > 0:
            usuarios[username]["uso_restante"] -= 1
            return jsonify({"message": "Acceso permitido", "uso_restante": usuarios[username]["uso_restante"]})
        else:
            return jsonify({"message": "Límite de uso alcanzado"}), 403
    else:
        return jsonify({"message": "Credenciales incorrectas"}), 401

if __name__ == "__main__":
    app.run(debug=True)
