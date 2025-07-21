from flask import Flask, render_template, redirect, flash, request
from forms import ContactForm

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Needed for flash and CSRF

@app.route('/', methods=['GET', 'POST'])
def contact():
    form = ContactForm()

    if form.validate_on_submit():
        flash("Form submitted successfully!", "success")
        return redirect('/')
    elif request.method == 'POST':
        flash("Please correct the errors below.", "danger")
        print("Form Errors:", form.errors)  # 🔍 Debug log

    return render_template('form.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
