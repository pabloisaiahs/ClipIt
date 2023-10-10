from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    # Get the username from the submitted form
    username = request.form.get('username')

    # Mock data for now
    restaurant_coupons = [
        {"platform": "AMEX", "details": "10% off any meal"},
        {"platform": "Chase", "details": "Free appetizer with main course"}
    ]
    grocery_coupons = [
        {"platform": "Target Circle", "details": "5% off fresh produce"},
        {"platform": "Chase", "details": "3% cashback on all groceries"}
    ]
    return render_template('dashboard.html', restaurant_coupons=restaurant_coupons, grocery_coupons=grocery_coupons, user_name=username)

@app.route('/settings')
def settings():
    return render_template('settings.html')

@app.route('/link-accounts')
def link_accounts():
    return render_template('link_accounts.html')

if __name__ == '__main__':
    app.run(debug=True)