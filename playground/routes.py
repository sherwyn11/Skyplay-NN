from flask import *
import numpy as np
import os
import random

from playground import app
from playground.neural_net.nn_model.model import Model
from playground.preprocessing import generic_preprocessing as gp
from playground.nocache import nocache
from playground.utils.feature_extract import get_features
from playground.utils.flask_utils import *
from playground.visualization import visualize as vis


global posted
model = Model()
save_path = 'playground/uploads/'
posted = 0

####################### ROUTES #######################


@nocache
@app.route('/', methods=['GET', 'POST'])
def home():

    global model
    if request.method == 'POST':
        if request.get_json() is not None:
            session['posted'] = 1
            
            if(os.path.exists('playground/static/img/test.png')):
                os.remove('playground/static/img/test.png')

            data = request.get_json()
            model = create_model(data)

            regularization_type = data['regularizations']
            regularization_rate = float(data['regularRate'])
            problem_type = data['problem']
            epochs = int(data['epochs'])
            batch_size = int(data['batchSize'])
            X, Y, ss, le = get_features(problem_type)

            model.fit(
                X, Y, epochs, regularization_type, regularization_rate, batch_size
            )
            idx = random.randint(0, len(X) - 1)
            print(
                model.predict(
                    ss.transform([X[idx]]), [le.transform(Y[idx])], problem_type
                )
            )
            return 'True'

        elif request.form['Submit'] == 'Upload':
            if upload(request.files['data']):
                flash(f'File uploaded successfully', 'success')
            else:
                flash(f'Upload Unsuccessful. Please try again', 'danger')

        elif request.form['Submit'] == 'preprocess':
            return redirect('/preprocess')

    else:
        if session.get('uploaded') is None and session.get('posted') is None:
            if(os.path.exists('playground/static/img/test.png')):
                os.remove('playground/static/img/test.png')
            model = create_default_model()
            problem_type = 'classification'

            X, Y, ss, le = get_features(problem_type)
            model.fit(X, Y, 1500, '0', 0, 4)

            print(
                model.predict(
                    ss.transform([[1, 1], [0, 1], [1, 0], [0, 0]]),
                    np.array(le.transform([0, 1, 1, 0])).reshape(-1, 1),
                    problem_type,
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


@app.route('/preprocess', methods=['GET', 'POST'])
@nocache
def preprocess():

    if request.method == 'POST':

        if request.form['Submit'] == 'Delete':
            try:
                df = gp.read_dataset('playground/clean/clean.csv')
                df = gp.delete_column(df, request.form.getlist('check_cols'))
                df.to_csv('playground/clean/clean.csv', mode='w', index=False)
                flash(f'Column(s) deleted Successfully', 'success')
            except:
                flash(f'Error! Upload Dataset', 'danger')

        elif request.form['Submit'] == 'Clean':
            try:
                df = gp.read_dataset('playground/clean/clean.csv')
                print(request.form['how'])
                if request.form['how'] is not 'any':
                    df = gp.treat_missing_numeric(
                        df, request.form.getlist('check_cols'), how=request.form['how']
                    )
                elif request.form['howNos'] is not None:
                    df = gp.treat_missing_numeric(
                        df,
                        request.form.getlist('check_cols'),
                        how=float(request.form['howNos']),
                    )

                df.to_csv('playground/clean/clean.csv', mode='w', index=False)
                flash(f'Column(s) cleant Successfully', 'success')
            except:
                flash(f'Error! Upload Dataset', 'danger')

        elif request.form['Submit'] == 'Visualize':
            global posted
            df = gp.read_dataset('playground/clean/clean.csv')

            x_col = request.form['x_col']

            if vis.hist_plot(df, x_col):
                posted = 1

    df = gp.read_dataset('playground/clean/clean.csv')
    description = gp.get_description(df)
    columns = gp.get_columns(df)
    print(columns)
    dim1, dim2 = gp.get_dim(df)
    head = gp.get_head(df)

    return render_template(
        'preprocess.html',
        active='preprocess',
        title='Preprocess',
        filename=session['fname'],
        posted=posted,
        no_of_rows=len(df),
        no_of_cols=len(columns),
        dim=str(dim1) + ' x ' + str(dim2),
        description=description.to_html(
            classes=[
                'table-bordered',
                'table-striped',
                'table-hover',
                'thead-light',
            ]
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


@app.route('/visualize', methods=['GET', 'POST'])
@nocache
def visualize():

    if request.method == 'POST':
        x_col = request.form['x_col']
        y_col = request.form['y_col']

        df = vis.xy_plot(x_col, y_col)
        heights = np.array(df[x_col]).tolist()
        weights = np.array(df[y_col]).tolist()

        newlist = []
        for h, w in zip(heights, weights):
            newlist.append({'x': h, 'y': w})
        ugly_blob = str(newlist).replace("'", '')
        print(newlist)
        columns = vis.get_columns()
        print(x_col)
        return render_template(
            'visualize.html',
            cols=columns,
            src='img/pairplot.png',
            xy_src='img/fig.png',
            posted=1,
            data=ugly_blob,
            active='visualize',
            x_col_name=str(x_col),
            y_col_name=str(y_col),
            title='Visualize',
        )

    else:
        vis.pair_plot()
        columns = vis.get_columns()
        return render_template(
            'visualize.html',
            cols=columns,
            src='img/pairplot.png',
            posted=0,
            active='visualize',
            title='Visualize',
        )


@nocache
@app.route("/data.json", methods=["GET"])
def data():

    global model
    no_of_layers = len(model.parameters) // 2
    data = {"nodes": [], "weights": [], "biases": []}
    SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
    SUP = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")
    lst = vis.get_columns()

    for i in range(len(lst) - 1):
        data["nodes"].append({"label": lst[i], "layer": 1})
        data["biases"].append(int(0))

    for i in range(1, no_of_layers + 1):

        for j in range(1, model.layers[i].units + 1):
            data["nodes"].append(
                {
                    "label": "a" + str(j).translate(SUB) + str(i).translate(SUP),
                    "layer": i + 1,
                }
            )

        a = model.parameters["W" + str(i)].T.tolist()
        b = model.parameters["b" + str(i)].T.tolist()

        [data["weights"].append(x) for param in a for x in param]
        [data["biases"].append(x) for param in b for x in param]

    return json.dumps(data)


@app.route('/test.png')
@nocache
def test():
    return send_file('static/img/test.png', mimetype='image/png', as_attachment=True)


@app.route('/reset', methods=['GET', 'POST'])
def reset():
    session.clear()
    default_data()
    session['posted'] = None
    session['uploaded'] = None
    return redirect('/')

@app.route('/col.csv')
@nocache
def col():
    return send_file('visualization/col.csv', mimetype='text/csv', as_attachment=True)


# @app.route('/pairplot.png')
# @nocache
# def pairplot():
#     return send_file(
#         'static/img/pairplot.png', mimetype='image/png', as_attachment=True
#     )

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')