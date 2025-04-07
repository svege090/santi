from flask import Flask, render_template, request

app = Flask(__name__)

perfumes = {
    "sweet-pea-bliss": {
        "name": "Sweet Pea Bliss",
        "description": "A delicate floral fragrance with notes of fresh rose petals and morning dew."
    },
    "citrus-spark": {
        "name": "Citrus Spark",
        "description": "A zesty, energizing scent infused with lemon, grapefruit, and bergamot."
    },
    "mystic-applaud": {
        "name": "Mystic Applaud",
        "description": "An exotic blend of oud, spice, and deep musk for a mysterious allure."
    },
    "vanilla-noir": {
        "name": "Vanilla Noir",
        "description": "A warm, sweet scent with vanilla bean, amber, and a touch of caramel."
    }
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/shop')
def shop():
    return render_template('shop.html', perfumes=perfumes)

@app.route('/perfume/<perfume_id>')
def perfume_detail(perfume_id):
    perfume = perfumes.get(perfume_id)
    if not perfume:
        return "<h2>Perfume not found.</h2>", 404
    return render_template('perfume_detail.html', perfume=perfume)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        message = request.form['message']
        return render_template('result.html', name=name, message=message)
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)