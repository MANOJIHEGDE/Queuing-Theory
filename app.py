from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        method = request.form['method']
        if method == 'Method 1':
            return render_template('method1.html')
        elif method == 'Method 2':
            return render_template('method2.html')
    return render_template('index.html')

@app.route('/method1', methods=['POST'])
def method1():
    lambda_val = float(request.form['lambda'])
    mu_val = float(request.form['mu'])
    
    Lq = round(((lambda_val**2) / (mu_val * (mu_val - lambda_val))),3)
    Ls = round((Lq + (lambda_val / mu_val)),3)
    wq = round((Lq / lambda_val),2)
    ws =round((wq + (1 / mu_val)),2)

    return render_template('result.html', Lq=Lq, Ls=Ls, wq=wq, ws=ws)

@app.route('/method2', methods=['POST'])
def method2():
    lambda_val = float(request.form['lambda'])
    mu_val = float(request.form['mu'])
    c = int(request.form['c'])

    M = (lambda_val / mu_val)
    N =(lambda_val * mu_val)
    values = range(c)
    po = round(((sum([(M ** n) / factorial(n) for n in values]) + ((M ** c) / (factorial(c))* ((c * mu_val) / (c * mu_val - lambda_val)))) ** -1),3)

    Lq = round((((N * (M ** c)) / (factorial(c - 1) * ((c * mu_val - lambda_val) ** 2))) * po),3)
    Ls = round((Lq + (lambda_val / mu_val)),3)
    wq =round((( Lq / lambda_val)),3)
    ws =round((wq + (1 / mu_val)),3)
    z= round((((mu_val * (M ** c)) / (factorial(c - 1) * ((c * mu_val - lambda_val)))) * po),3)

    return render_template('result2.html',C=c,z=z,p=po, Lq=Lq, Ls=Ls, wq=wq, ws=ws)

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

if __name__ == '__main__':
    app.run(debug=True)
