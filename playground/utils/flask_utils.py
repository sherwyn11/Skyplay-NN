from flask import session
from playground.preprocessing import generic_preprocessing as gp
from playground.neural_net.nn_model.model import Model

exts = ['csv', 'json', 'yaml']

def default_data():
    session['ext'] = 'csv'
    session['fname'] = 'XOR'
    df = gp.read_dataset('playground/uploads/XOR.csv')
    df.to_csv('playground/clean/clean.csv', index=False)

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
    
    model = Model()

    model.add(2, activation)
    model.add(4, activation)
    model.add(1, activation)
    model.compile(optimizer, learning_rate)

    return model

def create_default_model():
    
    learning_rate = 0.1
    activation = 'sigmoid'
    optimizer = 'Adam'
    model = Model()
    model.add(2, activation)
    model.add(4, activation)
    model.add(1, activation)
    model.compile(optimizer, learning_rate)

    return model
    
