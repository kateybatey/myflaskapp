from flask import Flask, render_template
     
app = Flask(__name__)


@app.route("/")
def home_page():
	return render_template('home.html')


# @app.route('/SignUp')
# def showSignUp():

# 	flash("You can't sign up yet, check back next week!")

# 	return render_template('signup.html')

# @app.route('/SignUp', methods=['POST'])
# def attemptedSignIn():

#     name = request.form['inputName']
#     email = request.form['inputEmail']
#     password = request.form['inputPassword']

#     return render_template('signup.html')

if __name__ == "__main__":
    app.run()

