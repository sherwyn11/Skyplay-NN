from flask import *

from playground import app
from playground.neural_net.nn_model.model import Model
from playground.preprocessing import generic_preprocessing as gp
from playground.nocache import nocache
from playground.utils.feature_extract import get_features
from playground.utils.flask_utils import *

global posted
save_path = 'weka/uploads/'
posted = 0

###### routes ######

@app.route('/', methods=['GET', 'POST'])
@nocache
def home():
    if request.method == 'POST':
        if request.get_json() is not None:
            data = request.get_json()

            model = create_model(data)

            regularization_type = data['regularizations']
            regularization_rate = float(data['regularRate'])
            problem_type = data['problem']
            epochs = int(data['epochs'])
            print(problem_type)
            # batch_size=int(data['batchSize'])
            batch_size = 100
            X, Y = get_features()

            model.fit(X, Y, epochs, regularization_type, regularization_rate, batch_size)
            print(model.predict([[1, 0], [0, 1], [1, 1], [0, 0]], [[1], [1], [0], [0]], problem_type))

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

        return render_template(
            'home.html',
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
            'home.html', title='Home',
        )