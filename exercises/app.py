from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home_page():
    sports = ["baseball", "football", "basketball"]
    return render_template(
        "index.html",
        sports = sports,
        likes_same_sport = True)


    

if __name__ == '__main__':
   app.run(debug = True)