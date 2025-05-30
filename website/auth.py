from flask import Blueprint , render_template,request,flash # type: ignore

auth=Blueprint('auth',__name__)
@auth.route('/sign-up',methods=['POST','GET'])
def sign_up():
    if request.method=='POST':
        email=request.form.get('email')
        password_1=request.form.get('password')
        password_2=request.form.get('password_2')
        firstname=request.form.get('firstname')
        if len(email)<4:
            flash('Email must be more than 4 characters.',category='error')
        elif len(firstname)<3:
            flash('Firstname must be more than 3 characters.',category='error')
        elif password_1!=password_2:
            flash('Passwords don\'t match.',category='error')
        elif len(password_1)<7:
            flash('Pssword must be at least 8 characters',category='error')
        else:
            flash(f'{firstname}s account created successfuly!',category='success')
    return render_template("signup.html")
@auth.route('/login' ,methods=['POST','GET'])
def login():
    return render_template("login.html")
@auth.route('/logout' )
def logout():
    return render_template("logout.html")
