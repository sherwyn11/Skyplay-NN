from flask import *
from playground.neural_net.nn_model.model import Model
from playground.preprocessing import generic_preprocessing as gp
from playground import app
from playground.nocache import nocache
from playground.utils.feature_extract import get_features

from playground.utils.flask_utils import *

global posted
save_path = 'weka/uploads/'
posted = 0




@app.route('/test', methods=['GET', 'POST'])
def test():

    model = Model()
    model.add(2, 'sigmoid')
    model.add(4, 'sigmoid')
    model.add(1, 'sigmoid')
    model.compile('Adam', 0.01)
    model.fit([[0, 0], [0, 1], [1, 0], [1, 1]], [[0], [1], [1], [0]], 6000, 0, 0)
    print(model.predict([[0, 0], [0, 1], [1, 1], [1, 0]], [[0], [1], [0], [1]]))
    print(model.predict([[1, 0], [0, 1], [1, 1], [0, 0]], [[1], [1], [0], [0]]))

    return render_template('test.html')

@app.route('/', methods=['GET', 'POST'])
@nocache
def home():
    if request.method == 'POST':
        if request.get_json() is not None:
            print(request.get_json()["learningRate"])        
        elif request.form['Submit'] == 'Upload':
            if(upload(request.files['data'])):
                flash(f'File uploaded successfully', 'success')
            else:
                flash(f'Upload Unsuccessful. Please try again', 'danger')

        elif request.form['Submit'] == 'preprocess':
            print('True')
            return 'True'

    if session.get('uploaded') is not None:

        df = gp.read_dataset('playground/clean/clean.csv')
        description = gp.get_description(df)
        columns = gp.get_columns(df)
        dim1, dim2 = gp.get_dim(df)
        head = gp.get_head(df)
        X, Y = get_features()
        print(X, Y)

        return render_template(
            'home.html',
            active='preprocess',
            title='Home',
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
    else:
        return render_template(
            'home.html', active='preprocess', title='Preprocess',
        )
