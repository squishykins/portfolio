from flask import Flask, render_template


# Create an instance of Flask
app = Flask(__name__)

# flash route to render template
@app.route("/")
def index():

    # Return the template with the data
    return render_template("index.html")

# Make it run
if __name__ == "__main__":
    app.run(debug=True)