from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

# A list of tuples, each containing the name of the fruit and its price
fruits = [
        ('Apple', 0.99),
        ('Banana', 0.59),
        ('Cherry', 2.99),
        ('Date', 1.99),
        ('Elderberry', 1.49)
    ]
@app.route("/")
def home():
    return render_template("index.html")

@app.route('/shop')
def shop():
    return render_template('shop.html', fruits=fruits)

@app.route('/end',methods=['POST'])
def end():
    total_price =0
    for fruit, price in fruits:
        quantity = request.form.get(fruit, type=int, default=0)
        print(quantity)
        total_price += price*quantity
    return render_template('end.html',total_price=total_price)

if __name__ == "__main__":
    app.run()