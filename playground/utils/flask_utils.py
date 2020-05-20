from flask import session
from playground.preprocessing import generic_preprocessing as gp
from playground.neural_net.nn_model.model import Model

exts = ['csv', 'json', 'yaml']


def upload(data):

    ext = data.filename.split('.')[1]
    if ext in exts:
        session['ext'] = ext
        session['fname'] = data.filename
        data.save('playground/uploads/' + data.filename)
        df = gp.read_dataset('playground/uploads/' + data.filename)
        df.to_csv('playground/clean/clean.csv', index=False)
        session['uploaded'] = True
        return True
    else:
        return False

def create_model(data):

    learning_rate = float(data['learningRate'])
    activation = data['activations']
    optimizer = data['optimizer']
    no_of_input_nodes = int(data['no_of_input_nodes'])
    no_of_output_nodes = int(data['no_of_output_nodes'])
    no_of_hidden_nodes = int(data['no_of_hidden_nodes'])

    model = Model()

    model.add(no_of_input_nodes, None)
    for node in data['no_of_nodes_in_hidden']:
        model.add(int(node['no_of_nodes']), node['activation'])
    model.add(no_of_output_nodes, activation)
    model.compile(optimizer, learning_rate)

    return model


    
