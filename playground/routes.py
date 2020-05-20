from flask import *
import numpy as np
from playground import app
from playground.neural_net.nn_model.model import Model
from playground.preprocessing import generic_preprocessing as gp
from playground.nocache import nocache
from playground.utils.feature_extract import get_features
from playground.utils.flask_utils import *
from playground.visualization.visualize import *


global posted
model = Model()
save_path = 'weka/uploads/'
posted = 0

# --------------------- ROUTES ---------------------------


@nocache
@app.route('/', methods=['GET', 'POST'])
def home():
    global model
    if request.method == 'POST':
        if request.get_json() is not None:
            data = request.get_json()

            model = create_model(data)

            regularization_type = data['regularizations']
            regularization_rate = float(data['regularRate'])
            problem_type = data['problem']
            epochs = int(data['epochs'])
            batch_size = int(data['batchSize'])
            X, Y = get_features()

            model.fit(
                X, Y, epochs, regularization_type, regularization_rate, batch_size
            )
            print(
                model.predict(
                    [[1, 0], [0, 1], [1, 1], [0, 0]], [[1], [1], [0], [0]], problem_type
                )
            )
            return 'True'

        elif request.form['Submit'] == 'Upload':
            if upload(request.files['data']):
                flash(f'File uploaded successfully', 'success')
            else:
                flash(f'Upload Unsuccessful. Please try again', 'danger')

        elif request.form['Submit'] == 'preprocess':
            print('True')
            return 'True'

    else:
        if session.get('uploaded') is None and session.get('posted') is None:
            model = create_default_model()
            X, Y = get_features()
            model.fit(X, Y, 1500, '0', 0, 4)
            print(
                model.predict(
                    [[1, 0], [0, 1], [1, 1], [0, 0]],
                    [[1], [1], [0], [0]],
                    'classification',
                )
            )
    df = gp.read_dataset('playground/clean/clean.csv')
    description = gp.get_description(df)
    columns = gp.get_columns(df)
    dim1, dim2 = gp.get_dim(df)
    head = gp.get_head(df)

    return render_template(
        'home.html',
        title='Home',
        filename=session['fname'],
        posted=posted,
        no_of_rows=len(df),
        no_of_cols=len(columns),
        dim=str(dim1) + ' x ' + str(dim2),
        description=description.to_html(
            classes=['table-bordered', 'table-striped', 'table-hover', 'thead-light',]
        ),
        columns=columns,
        head=head.to_html(
            classes=[
                'table',
                'table-bordered',
                'table-striped',
                'table-hover',
                'thead-light',
            ]
        ),
    )


@nocache
@app.route('/data.json', methods=['GET'])
def data():

    global model
    no_of_layers = len(model.parameters) // 2
    data = {'nodes': [], 'weights': []}
    SUB = str.maketrans('0123456789', '₀₁₂₃₄₅₆₇₈₉')
    SUP = str.maketrans('0123456789', '⁰¹²³⁴⁵⁶⁷⁸⁹')
    lst = get_columns()

    for i in range(len(lst) - 1):
        data['nodes'].append({'label': lst[i], 'layer': 1})

    for i in range(1, no_of_layers + 1):

        for j in range(1, model.layers[i].units + 1):
            data['nodes'].append(
                {
                    'label': 'a' + str(j).translate(SUB) + str(i).translate(SUP),
                    'layer': i + 1,
                }
            )

        a = model.parameters['W' + str(i)].T.tolist()

        [data['weights'].append(x) for param in a for x in param]

    return json.dumps(data)


@app.route('/test.png')
@nocache
def test():
    return send_file('static/img/test.png', mimetype='image/png', as_attachment=True)


@app.route('/reset', methods=['GET', 'POST'])
def reset():
    session.clear()
    default_data()
    session['posted'] = 0
    return redirect('/')