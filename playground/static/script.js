/** @format */

let parameters = 'false';
document.getElementById('epochs').defaultValue = "1";

function onTrain() {
    parameters = 'true';
    axios.post('/', {
        learningRate: document.getElementById('learningRate').value,
        activations: document.getElementById('activations').value,
        regularizations: document.getElementById('regularizations').value,
        regularRate: document.getElementById('regularRate').value,
        problem: document.getElementById('problem').value,
        epochs: document.getElementById('epochs').value,
        optimizer: document.getElementById('optimizer').value,
        parameters: parameters,
    })
    .then(function(response) {
        parameters = 'false';
    })
    .catch(function(error) {
        parameters = 'false';
        console.log(error);
    });
}