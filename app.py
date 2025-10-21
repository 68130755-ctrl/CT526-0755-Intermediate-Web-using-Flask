from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
  return render_template('index.html')
    

@app.route('/tech')
def tech():
    return render_template('tech.html')

@app.route('/myid')
def myid():
    return "รหัสนักศึกษา: 0755"

@app.route('/draw/<int:num>')
def draw(num):
    output = ""
    for i in range(num):
        output += "mmmm<br>"
    return f"<h3>การแสดงผล {num} แถว</h3><p>{output}</p>"

@app.route('/sum/<xx>/<yy>')
def sum_number(xx,yy):
    try :
        num_x = int(xx)
        num_y = int(yy)
        zz = num_x + num_y
        return f"The result of sum between {num_x} and {num_y} is {zz}"
    except ValueError:
        return "You are using miss data type for operation"
 
@app.route('/concat/<xx>/<yy>')
def concatenate_strings(xx, yy):
    xxyy = str(xx) + str(yy)
    return f"The result of concatenate between {xx} and {yy} is {xxyy}" 
 
if __name__ == '__main__':
   app.run(host='0.0.0.0', port=5000,debug=True)
