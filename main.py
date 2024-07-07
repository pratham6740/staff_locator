from flask import Flask, request, render_template
from chatbot import Chat
from ttabstract import Ttabstract

app = Flask(__name__)

professors = ["Dr. Akhtar Rasool", "Dr. Manish Pandey", "Dr. Jay Trilok Choudhary", "Dr. Deepak Singh Tomar",
              "Dr. Nilay Khare", "Dr. Dhirendra Pratap Singh", "Dr. Mitul Kumar Ahirwar", "Dr. Rajesh Wadhwani",
              "Dr. Pragati Agrawal", "Dr. Minu Chawla", "Dr. Saiyam Shukla", "Dr. Vaibhav Soni", "Dr. Vijay Bhaskar",
              "Dr. Shweta Jain"]


@app.route('/', methods=['GET', 'POST'])
def home():
    bot_response = ""
    user_input = ""

    if request.method == 'POST':
        user_input = request.form['message']
        chat = Chat()

        if user_input.lower() in ['thanks', 'thank you']:
            bot_response = "You are welcome..."
        elif chat.greet(user_input.lower()):
            bot_response = chat.greet(user_input.lower())
        else:
            find_prof_name = chat.response(user_input.lower())
            if find_prof_name not in professors:
                bot_response = find_prof_name
            else:
                tt = Ttabstract(find_prof_name)
                bot_response = tt.getdetails()

    return render_template('index.html', bot_response=bot_response, user_input=user_input)


if __name__ == '__main__':
    app.run(debug=True)
