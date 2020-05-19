from flask import session
from playground.preprocessing import generic_preprocessing as gp

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