from flask import Flask, render_template
app = Flask(__name__)
likes_same_sport = True
@app.route('/')
def home_page():
    if likes_same_sport == True:
        return "Hello"
    else:
        return render_template("index.html")


    

if __name__ == '__main__':
   app.run(debug = True)