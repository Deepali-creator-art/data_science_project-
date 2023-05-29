from flask import Flask, request, jsonify,render_template
app = Flask(__name__)
@app.route('/')
def firstpage():
    return render_template('app.html')
if __name__ == "__main__":
    print("Starting Python Flask Server ")
    app.run(debug=True,port=5001)