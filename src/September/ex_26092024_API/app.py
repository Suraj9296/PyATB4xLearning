from flask import Flask
app=Flask(__name__)

@app.route('/')
def hello():
    return '{"name" : "pramod"}'
if __name__=='__main__':
    app.run(debug=True)
