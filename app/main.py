from flask import Flask, render_template, request

app = Flask(__name__)

morse_code_dict = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    1: '.----',
    2: '..---',
    3: '...--',
    4: '....-',
    5: '.....',
    6: '-....',
    7: '--...',
    8: '---..',
    9: '----.',
    0: '-----',
}


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/convert")
def convert_text():
    user_input = request.args.get("text", "").upper()
    morse_output = ""
    for char in user_input:
        if char == " ":
            morse_output += " "
        elif char in morse_code_dict:
            morse_output += morse_code_dict[char] + " "
    return morse_output


if __name__ == "__main__":
    app.run(debug=True)