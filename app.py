from flask import Flask, render_template, request

app = Flask(__name__)

# Function to determine user's segment
def determine_segment(income, education, location, religiosity):
    if income < 10000:
        return "Rural Poor"
    elif income < 30000:
        return "Urban Middle Class"
    else:
        return "Elite"

# Route for the homepage
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Get form data
        try:
            income = int(request.form["income"])
            education = int(request.form["education"])
            location = request.form["location"].lower()
            religiosity = request.form["religiosity"].lower()

            # Validate inputs
            if location not in ["urban", "rural"]:
                return render_template("index.html", error="Location must be 'urban' or 'rural'.")
            if religiosity not in ["high", "moderate", "low"]:
                return render_template("index.html", error="Religiosity must be 'high', 'moderate', or 'low'.")

            # Determine segment
            segment = determine_segment(income, education, location, religiosity)
            return render_template("index.html", segment=segment)
        except ValueError:
            return render_template("index.html", error="Please enter valid numbers for income and education.")

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)