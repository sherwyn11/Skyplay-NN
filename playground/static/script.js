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
        console.log(div_child);
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

        if(choice2 == 1){
            var div_child = document.getElementById('add_layers');
            var row = document.createElement('div');
            row.className = 'row';
            var but1 = document.createElement('button');
            but1.innerHTML = '-';
            var but2 = document.createElement('button');
            but2.innerHTML = '+';
            var text = document.createElement('b');
            text.innerHTML = '0';
            var span1 = document.createElement('span');
            span1.innerHTML = '&nbsp;';
            var span2 = document.createElement('span');
            span2.innerHTML = '&nbsp;';
            var test = document.createElement('b');
            test.innerHTML = 'Layer ' + (val + 1)
            var br = document.createElement('br');
            var p = document.createElement('p');
    
    
            row.appendChild(p);
            p.appendChild(test);
            p.appendChild(but1);
            p.appendChild(span1);
            p.appendChild(text);
            p.appendChild(span2);
            p.appendChild(but2);
            div_child.appendChild(p);
            div_child.appendChild(br);
        }

    }  
}