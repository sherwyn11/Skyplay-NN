/** @format */

let parameters = 'false';
document.getElementById('epochs').defaultValue = "1";
var len = document.getElementById('no_of_hidden_layers').value;
var len_nodes = 0;

function onTrain() {

    var layers = [];
    for(i = 1; i <= len_nodes; i++){
        var temp1 =  document.getElementById('layer'+ i +'_node').value;
        var temp2 =  document.getElementById('layer'+ i +'_select').value;
        layers.push({
            no_of_nodes: temp1,
            activation: temp2
        });
    }
    console.log(layers)
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
        no_of_input_nodes: document.getElementById('input_nodes').value,
        no_of_output_nodes: document.getElementById('output_nodes').value,
        no_of_hidden_nodes: len,
        no_of_nodes_in_hidden: layers,
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

    var len = document.getElementById('no_of_hidden_layers');
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

        if(choice2 == 1){
            var elmnt = document.getElementById('layer' + (val));
            elmnt.remove();
            len.setAttribute('value', Number(val) - 1);
            len_nodes = val - 1;
        }
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
            var p = document.createElement('div');
            p.className = 'row';
            p.id = 'layer' + val
            var but1 = document.createElement('button');
            but1.innerHTML = '-';
            id = 'layer' + val;
            but1.setAttribute('onclick', 'manipulateHiddenNodes(0, id)');
            but1.id = 'layer' + val;
            var but2 = document.createElement('button');
            but2.innerHTML = '+';
            but2.setAttribute('onclick', 'manipulateHiddenNodes(1, id)');
            but2.id = 'layer' + val;
            var text = document.createElement('b');
            text.innerHTML = '1';
            text.id = 'layer' + val + '_tag';
            var hidden = document.createElement('input');
            hidden.setAttribute('type', 'hidden');
            hidden.id = 'layer' + val + '_node';
            hidden.value = 1;
            var span1 = document.createElement('span');
            span1.innerHTML = '&nbsp;';
            var span2 = document.createElement('span');
            span2.innerHTML = '&nbsp;';
            var span3 = document.createElement('span');
            span3.innerHTML = '&nbsp;';
            var test = document.createElement('span');
            test.innerHTML = 'No. of nodes in layer ' + val + ' : ';
            var select = document.createElement('select');
            select.id = 'layer' + val + '_select';
            var option0 = document.createElement('option');
            option0.innerHTML = 'Choose Activation';
            option0.disabled = true;
            option0.selected = true;
            var option1 = document.createElement('option');
            option1.value = 'sigmoid';
            option1.innerHTML = 'Sigmoid';
            var option2 = document.createElement('option');
            option2.value = 'tanh';
            option2.innerHTML = 'Tanh';
            var option3 = document.createElement('option');
            option3.value = 'relu';
            option3.innerHTML = 'ReLU';
            var option4 = document.createElement('option');
            option4.value = 'leaky_relu';
            option4.innerHTML = 'Leaky ReLU';
    
            p.appendChild(test);
            p.appendChild(span1);
            p.appendChild(but1);
            p.appendChild(span2);
            p.appendChild(hidden);
            p.appendChild(text);
            p.appendChild(span3);
            p.appendChild(but2);
            select.appendChild(option0);
            select.appendChild(option1);
            select.appendChild(option2);
            select.appendChild(option3);
            select.appendChild(option4);
            p.appendChild(select);
            div_child.appendChild(p);

            len.setAttribute('value', Number(val));
            len_nodes = val;
        }
    }
}

function manipulateOpNodes(choice){
    var element = document.getElementById('output_nodes');
    var val = element.value;
    val = Number(val)
    var tag = document.getElementById('output_tag');
    if(choice === 0){
        if(val === 1){
            val = 1;
        }else{
            val -= 1;
        }
        element.setAttribute('value', val);
        tag.innerHTML = val;
    }else{
        val += 1;
        element.setAttribute('value', val);
        tag.innerHTML = val;
    }
}

function manipulateHiddenNodes(choice, id){
    var element = document.getElementById(id+'_node');
    var val = element.value;
    val = Number(val)
    var tag = document.getElementById(id+'_tag');
    if(choice === 0){
        if(val === 1){
            val = 1;
        }else{
            val -= 1;
        }
        element.setAttribute('value', val);
        tag.innerHTML = val;
    }else{
        val += 1;
        element.setAttribute('value', val);
        tag.innerHTML = val;
    }
}