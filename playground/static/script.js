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

function manipulateInpNodes(choice1, choice2){

    if(choice2 == 0){
        var element = document.getElementById('input_nodes');
        var val = element.value;
        val = Number(val)
        var tag = document.getElementById('input_nodes_tag');
    }else{
        var element = document.getElementById('no_of_hidden');
        var val = element.value;
        val = Number(val)
        var tag = document.getElementById('hidden_tag');
    }

    if(choice1 === 0){
        if(val === 0){
            val = 0;
        }else{
            val -= 1;
        }
        element.setAttribute('value', val);
        tag.innerHTML = val;
    }else if(choice1 === 1){
        val += 1;
        element.setAttribute('value', val);
        tag.innerHTML = val;
    }  
}