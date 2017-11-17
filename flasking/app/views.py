from app import app
from flask import render_template,flash,redirect
from forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Amrinder'}
    posts = [
        {
            'author': {'nickname': 'John'},
            'body': 'Beautiful day in Portland'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'Avengers was so cool'
        },
        {
            'author': {'nickname': 'Rahil'},
            'body': 'Coded whole day'
        },
        {
            'author': {'nickname': 'Nishank'},
            'body': 'Ran all day'
        }

    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login', methods=['get','post'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="%s", remember_me="%s"' % ((form.openid.data),str(form.remember_me.data)))
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form,
                           providers=app.config['OPENID_PROVIDERS'])
