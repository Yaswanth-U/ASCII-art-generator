from flask import Flask, render_template_string, request

app = Flask(__name__)

ASCII_MAP= {
    # new styles coming soon
    'A':[" █████╗  ",
         "██╔══██╗ ",
         "███████║ ",
         "██╔══██║ ",
         "██║  ██║ ",
         "╚═╝  ╚═╝ "
        ],
    'B':["██████╗  ",
         "██╔══██╗ ",
         "██████╔╝ ",
         "██╔══██╗ ",
         "██████╔╝ ",
         "╚═════╝  "
        ],
    'C':[" ██████╗ ",
         "██╔════╝ ",
         "██║      ",
         "██║      ",
         "╚██████╗ ",
         " ╚═════╝ "
        ],
    'D':["██████╗  ",
         "██╔══██╗ ",
         "██║  ██║ ",
         "██║  ██║ ",
         "██████╔╝ ",
         "╚═════╝  "
         ],
    'E':["███████╗ ",
         "██╔════╝ ",
         "█████╗   ",
         "██╔══╝   ",
         "███████╗ ",
         "╚══════╝ "
        ],
    'F':["███████╗ ",
         "██╔════╝ ",
         "█████╗   ",
         "██╔══╝   ",
         "██║      ",
         "╚═╝      "
        ],
    'G':[" ██████╗  ",
         "██╔════╝  ",
         "██║  ███╗ ",
         "██║   ██║ ",
         "╚██████╔╝ ",
         " ╚═════╝  "
          ],
    'H':["██╗  ██╗ "
        ,"██║  ██║ "
        ,"███████║ "
        ,"██╔══██║ "
        ,"██║  ██║ "
        ,"╚═╝  ╚═╝ "
        ],
    'I':["██╗ "
        ,"██║ "
        ,"██║ "
        ,"██║ "
        ,"██║ "
        ,"╚═╝ "
        ],
    'J':[
     "     ██╗ ",
     "     ██║ ",
     "     ██║ ",
     "██   ██║ ",
     "╚█████╔╝ ",
     " ╚════╝  "
        ],
    'K':[
     "██╗  ██╗ "
    ,"██║ ██╔╝ "
    ,"█████╔╝  "
    ,"██╔═██╗  "
    ,"██║  ██╗ "
    ,"╚═╝  ╚═╝ "
     ],     
    'L':[
     "██╗      "
    ,"██║      "
    ,"██║      "
    ,"██║      "
    ,"███████╗ "
    ,"╚══════╝ "
        ],
    'M':[
     "███╗   ███╗ "
    ,"████╗ ████║ "
    ,"██╔████╔██║ "
    ,"██║╚██╔╝██║ "
    ,"██║ ╚═╝ ██║ "
    ,"╚═╝     ╚═╝ "
        ],
    'N':["███╗   ██╗ "
        ,"████╗  ██║ "
        ,"██╔██╗ ██║ "
        ,"██║╚██╗██║ "
        ,"██║ ╚████║ "
        ,"╚═╝  ╚═══╝ "
          ],
    'O':[" ██████╗  "
        ,"██╔═══██╗ "
        ,"██║   ██║ "
        ,"██║   ██║ "
        ,"╚██████╔╝ "
        ," ╚═════╝  "
         ],
    'P':[ "██████╗  "
         ,"██╔══██╗ "
         ,"██████╔╝ "
         ,"██╔═══╝  "
         ,"██║      "
         ,"╚═╝      "
    ],
    'Q':[" ██████╗  "
        ,"██╔═══██╗ "
        ,"██║   ██║ "
        ,"██║▄▄ ██║ "
        ,"╚██████╔╝ "
        ," ╚══▀▀═╝  "
         ],
    'R':["██████╗  "
        ,"██╔══██╗ "
        ,"██████╔╝ "
        ,"██╔══██╗ "
        ,"██║  ██║ "
        ,"╚═╝  ╚═╝ "
        ],
    'S':["███████╗ "
        ,"██╔════╝ "
        ,"███████╗ "
        ,"╚════██║ "
        ,"███████║ "
        ,"╚══════╝ "
        ],
    'T':["████████╗ "
        ,"╚══██╔══╝ "  
        ,"   ██║    "
        ,"   ██║    "
        ,"   ██║    "
        ,"   ╚═╝    "
         ],
    'U':["██╗   ██╗ "
        ,"██║   ██║ "
        ,"██║   ██║ "
        ,"██║   ██║ "
        ,"╚██████╔╝ "
        ," ╚═════╝  "
         ],
    'V':["██╗   ██╗ "
        ,"██║   ██║ " 
        ,"██║   ██║ "
        ,"╚██╗ ██╔╝ "
        ," ╚████╔╝  "
        ,"  ╚═══╝   "
         ],
    'W':["██╗    ██╗ " 
        ,"██║    ██║ "
        ,"██║ █╗ ██║ " 
        ,"██║███╗██║ "
        ,"╚███╔███╔╝ "
        ," ╚══╝╚══╝  "
           ],
    'X':["██╗  ██╗ "
        ,"╚██╗██╔╝ "
        ," ╚███╔╝  "
        ," ██╔██╗  "
        ,"██╔╝ ██╗ "
        ,"╚═╝  ╚═╝ "
        ],
    'Y':["██╗   ██╗ "
        ,"╚██╗ ██╔╝ "
        ," ╚████╔╝  " 
        ,"  ╚██╔╝   "
        ,"   ██║    "
        ,"   ╚═╝    "
         ],
    'Z':["███████╗ "
        ,"╚══███╔╝ "
        ,"  ███╔╝  " 
        ," ███╔╝   " 
        ,"███████╗ "
        ,"╚══════╝ "
        ],
    '?':[
      "██████╗  "
     ,"╚════██╗ "
     ,"  ▄███╔╝ "
     ,"  ▀▀══╝  "
     ,"  ██╗    "
     ,"  ╚═╝    "  
    ]
}


def generate_ascii(text):
    rows = ["", "", "", "", "", ""]

    for char in text.upper():
        pattern = ASCII_MAP.get(char, ASCII_MAP['?'])

        for i in range(6):
            rows[i] += pattern[i] + "  "

    return "\n".join(rows)


HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Text to ASCII Art Generator</title>

    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            background: #000000;
            color: #00ff88;
            font-family: Consolas, monospace;
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 30px;
        }

        .container {
            width: 100%;
            max-width: 1000px;
            background: #0a0a0a;
            border: 1px solid #222;
            border-radius: 24px;
            padding: 40px;
            box-shadow: 0 0 30px rgba(0,255,120,0.15);
        }

        h1 {
            text-align: center;
            font-size: 42px;
            margin-bottom: 10px;
        }

        .subtitle {
            text-align: center;
            color: #777;
            margin-bottom: 35px;
        }

        textarea {
            width: 100%;
            height: 140px;
            background: #000;
            color: #00ff88;
            border: 1px solid #00ff88;
            border-radius: 18px;
            padding: 18px;
            font-size: 18px;
            resize: none;
            outline: none;
            margin-bottom: 20px;
        }

        .buttons {
            display: flex;
            gap: 15px;
            margin-bottom: 30px;
        }

        button {
            border: none;
            border-radius: 16px;
            padding: 14px 24px;
            font-size: 16px;
            font-weight: bold;
            cursor: pointer;
            transition: 0.2s ease;
        }

        .generate-btn {
            background: #00ff88;
            color: #000;
        }

        .generate-btn:hover {
            transform: scale(1.05);
        }

        .copy-btn {
            background: #222;
            color: white;
        }

        .output {
            background: #000;
            border: 1px solid #333;
            border-radius: 18px;
            padding: 24px;
            min-height: 260px;
            overflow-x: auto;
        }

        pre {
            white-space: pre-wrap;
            line-height: 1.5;
            font-size: 14px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Text to ASCII Art Generator</h1>

        <p class="subtitle">
            made with ❤️ By Yaswanth Uppalapu, 18 year old hack cluber from India.
        </p>

        <form method="POST">
            <textarea
                name="text"
                placeholder="Type text here and click 'Generate'..."
            >{{ text }}</textarea>

            <div class="buttons">
                <button class="generate-btn" type="submit">
                    Generate!
                </button>

                <button class="copy-btn" type="button" onclick="copyOutput()">
                    Copy Output
                </button>
            </div>
        </form>

        <div class="output">
            <pre id="ascii-output">{{ output }}</pre>
        </div>
    </div>

    <script>
        function copyOutput() {
            const text = document.getElementById('ascii-output').innerText;
            navigator.clipboard.writeText(text)
                .then(() => alert('ASCII art copied!'));
        }
    </script>
</body>
</html>
"""


@app.route('/', methods=['GET', 'POST'])
def home():
    text = 'HELLO'
    output = generate_ascii(text)

    if request.method == 'POST':
        text = request.form.get('text', '')
        output = generate_ascii(text)

    return render_template_string(
        HTML_TEMPLATE,
        text=text,
        output=output
    )


if __name__ == '__main__':
    app.run(debug=True)
