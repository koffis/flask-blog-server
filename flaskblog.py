from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm
from forms import LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '3273357638792F423F4528482B4D6251'

posts = [
    {
        'author': 'Yaroslav Kravchenko',
        'title': 'Post number 1',
        'content': 'First post content',
        'date_posted': "May 16, 2020"
    },
    {
        'author': 'Oleh Kononenko',
        'title': 'Post number 2',
        'content': 'Second post content',
        'date_posted': "May 17, 2020"
    }

]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash("Account created for {}!".format(form.username.data), "success")
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)
