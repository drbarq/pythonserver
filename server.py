from flask import Flask, render_template, request, redirect
import csv

# export FLASK_APP=server
# export FLASK_DEBUG=1
# flask run --port 5050


app = Flask(__name__)
print(__name__)


@app.route('/')
def my_home():
    return render_template("index.html")


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(f"{page_name}.html")


def write_to_file(data):
    with open('database.txt', mode="a") as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email},{subject},{message}')


def write_to_csv(data):
    with open('database2.csv', mode="a", newline='',) as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow({email, subject, message})


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    # error = None
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            # write_to_file(data)
            write_to_csv(data)
            return redirect('thankyou')
        except Exception as e:
            return f'something went wrong {e}'
    else:
        "something went wrong"
        # error = True
    # return "form submitted"




# @app.route('/index')
# def my_index():
#     return render_template("index.html")


# @app.route('/about')
# def about():
#     return render_template("about.html")


# @app.route('/components')
# def components():
#     return render_template("components.html")


# @app.route('/contact')
# def contact():
#     return render_template("contact.html")


# @app.route("/thankyou")
# def thankyou():
#     return render_template("thankyou.html")


# @app.route("/work")
# def work():
#     return render_template("work.html")


# @app.route("/works")
# def works():
#     return render_template("works.html")


# # @app.route("/<username>")
# # def hello_world2(username=None):
# #     return render_template('index.html', name=username)

# # @app.add_url_rule('/favicon.ico',
# #                  redirect_to=url_for('static', filename='Flask-icon.png'))

# # @app.route('/favicon.ico')
# #     return send_from_directory(os.path.join(app.root_path, 'static'), "
# # Flask-icon.png", mimetype='image/vnd.microsoft.icon')

# # if __name__ == '__main__':
# #     app.run(debug=True, port=5050)  # Change the port number here