from flask import Flask, render_template, send_from_directory
import random
import json

app = Flask("__name__")

def generate_id():
    with open('ids.json', 'r') as file:
        ids = json.load(file)
    symbols = 'abcdefghijklmnopqrstuvwxyz'
    id = '39'
    for x in range(4):
        rand = random.randint(0,1)
        if rand == 0:
            symb = random.choice(symbols)
        else:
            symb = random.choice(symbols).upper()
        id += symb
    if id in ids:
        return generate_id()
    else:
        ids.append(id)
        with open('ids.json', 'w') as file:
            json.dump(ids, file)
        return id
        

@app.route('/')
def main():
    return render_template('main.html')


@app.route('/gen/<count>')
def coun(count):
    count = int(count)
    allbuttons = ''
    for x in range(count):
        url = "https://clck.ru/" + generate_id()
        butt = f'<a href="{url}" target="_blank">\n<button id="button"> {url} </button>\n</a>\n <br> \n'
        allbuttons += butt
    return render_template('index.html', buttons=allbuttons)

@app.route("/css/<filename>")
def uploaded_css(filename):
    return send_from_directory("css", filename)
    

if __name__ == "__main__":
    app.run(debug=True)