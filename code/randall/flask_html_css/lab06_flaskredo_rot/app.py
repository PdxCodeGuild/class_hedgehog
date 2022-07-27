from flask import Flask, render_template, request

app = Flask(__name__)

#home page at localhost:5000/
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def result():
#user input from a string to encrypt and encrypt as an integer
    encrypt = request.form['word'] #input
    rotation = request.form.get('rotation', type=int) #int Enter rotation
    secret_key=rotation
    encrypt = encrypt.lower()
    
#two dictionaries,letter and  number keys
    alphabet1 = {
        'a' : '1', 
        'b' : '2', 
        'c' : '3', 
        'd' : '4', 
        'e' : '5', 
        'f' : '6', 
        'g' : '7', 
        'h' : '8', 
        'i' : '9', 
        'j' : '10', 
        'k' : '11', 
        'l' : '12', 
        'm' : '13', 
        'n' : '14', 
        'o' : '15', 
        'p' : '16', 
        'q' : '17', 
        'r' : '18', 
        's' : '19', 
        't' : '20', 
        'u' : '21', 
        'v' : '22', 
        'w' : '23', 
        'x' : '24', 
        'y' : '25', 
        'z' : '26',
        ' ' : '27',
        '.' : '28',
        ',' : '29'
    }

    alphabet2 = {
        '1' : 'a', 
        '2' : 'b', 
        '3' : 'c', 
        '4' : 'd', 
        '5' : 'e', 
        '6' : 'f', 
        '7' : 'g', 
        '8' : 'h', 
        '9' : 'i', 
        '10' : 'j', 
        '11' : 'k', 
        '12' : 'l', 
        '13' : 'm', 
        '14' : 'n', 
        '15' : 'o', 
        '16' : 'p', 
        '17' : 'q', 
        '18' : 'r', 
        '19' : 's', 
        '20' : 't', 
        '21' : 'u', 
        '22' : 'v', 
        '23' : 'w', 
        '24' : 'x', 
        '25' : 'y', 
        '26' : 'z',
        '27' : ' ',
        '28' : ',',
        '29' : '.' 
    }
# list for results
    code = []

    for char in encrypt:
        w = int((alphabet1[char])) # Converts to integer
        x = w + rotation # Adds rotation 
        if x > 26: # makes alphabet wrap around
            x = rotation - (26 - w)
        y = str(x) # converts to string
        z = (alphabet2[y]) # converts to letter
        code.append(z) # adds to list
    encoded_message =''.join(code) # joins list to string
    
#return the encoded message

    return render_template('result.html', encoded_message=encoded_message, secret_key=secret_key)

app.run(debug=True)
