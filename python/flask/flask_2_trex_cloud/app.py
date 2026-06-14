from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/services')
def services():
    cloud_services=["Виртуальные серверы","Облачное хранилище","Kubernetes"]
    return render_template('services.html',services=cloud_services)

if __name__ == '__main__':
    app.run(debug=True)
