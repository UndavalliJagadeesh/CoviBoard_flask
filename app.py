from flask import Flask, render_template, abort

app = Flask(__name__)

@app.route('/')
folder = os.path.join('static', 'images')
app.config['UPLOAD_FOLDER'] = folder

def index():
    pic1 = os.path.join(app.config['UPLOAD_FOLDER'], 'ap.jpg')
    return render_template('index.html')

@app.route('/vstatus')
def vstatus():
    return render_template('vstatus.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/updates')
def updates():
    from urllib.request import urlopen
    import json
    url = "https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/latest/owid-covid-latest.json"
    response = urlopen(url)
    data_json = json.loads(response.read())
    ind = data_json["IND"]
    world = data_json["OWID_WRL"]
    return render_template('updates.html', 
                    ind_total_cases = int(ind['total_cases']), 
                    ind_new_cases=int(ind['new_cases']),
                    ind_total_deaths = int(ind['total_deaths']),
                    ind_vaccinated = int(ind['total_vaccinations']),
                    ind_update = ind['last_updated_date'],
                    wrd_total_cases = int(world['total_cases']), 
                    wrd_new_cases=int(world['new_cases']),
                    wrd_total_deaths = int(world['total_deaths']),
                    wrd_vaccinated = int(world['total_vaccinations']),
                    wrd_update = world['last_updated_date'])

@app.route('/<string:code>')
def redirect_to_page(code):
    return abort(404)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run()
