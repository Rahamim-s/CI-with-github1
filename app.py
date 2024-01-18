from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/api/hello")
def hello():
    return jsonify({"hello": "world"})

@app.route("/api/hello/<name>")
def hello_name(name):
    return jsonify({"hello": name})

@app.route("/api/whoami")
def whoami():
    return jsonify(
        name=request.remote_addr,
        ip=request.remote_addr,
        useragent=request.user_agent.string
    )

@app.route("/api/whoami/<name>")
def whoami_name(name):
    return jsonify(
        name=name,
        ip=request.remote_addr,
        useragent=request.user_agent.string
    )

# Ajoutez les routes pour les webhooks
@app.route("/testing", methods=['POST'])
def testing():
    payload = request.json
    ref = payload.get('ref', '')

    if ref == 'refs/heads/staging':
        # Ajoutez votre logique de test ici
        return 'Testing endpoint received payload.'

    return 'Invalid reference for testing.'

@app.route("/deployment", methods=['POST'])
def deployment():
    payload = request.json
    ref = payload.get('ref', '')

    if ref == 'refs/heads/main':
        # Ajoutez votre logique de déploiement ici
        return 'Deployment endpoint received payload.'

    return 'Invalid reference for deployment.'

if __name__ == '__main__':
    app.run(debug=True)
