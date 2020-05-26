/** @format */

/////////////////// HYPERPARAMETERS ///////////////////


let parameters = "false";

try {
    document.getElementById("epochs").defaultValue = "1";
    var len = document.getElementById("no_of_hidden_layers").value;
    document.getElementById('range-slider').defaultValue = 30;
    document.getElementById('range-result').innerHTML = '30%';
} catch (error) {
    console.log("Log1. Element Not Found")
}

function onPageLoad(page_name) {
    if (page_name == 'Home') {
        neuralNetwork();

    } else if (page_name == 'Preprocess') {
        histogramData();
    }
}

/////////////////// SLIDER /////////////////////

function updateSliderText() {
    var sliderValue = document.getElementById('range-slider').value;
    var percent = document.getElementById('range-result');
    percent.innerHTML = sliderValue + '%';
}
var len_nodes = 0;

function onTrain() {
    var layers = [];
    for (let i = 1; i <= len_nodes; i++) {
        var temp1 = document.getElementById("layer" + i + "_node").value;
        var temp2 = document.getElementById("layer" + i + "_select").value;
        layers.push({
            no_of_nodes: temp1,
            activation: temp2,
        });
    }
    console.log(layers);
    parameters = "true";
    axios
        .post("/", {
            learningRate: document.getElementById("learningRate").value,
            activations: document.getElementById("activations").value,
            regularizations: document.getElementById("regularizations").value,
            regularRate: document.getElementById("regularRate").value,
            problem: document.getElementById("problem").value,
            epochs: document.getElementById("epochs").value,
            optimizer: document.getElementById("optimizer").value,
            parameters: parameters,
            no_of_input_nodes: document.getElementById("input_nodes").value,
            no_of_output_nodes: document.getElementById("output_nodes").value,
            no_of_hidden_nodes: len,
            no_of_nodes_in_hidden: layers,
            batchSize: document.getElementById("batchSize").value,
            test_data_size: document.getElementById('range-slider').value
        })
        .then(function(response) {
            parameters = "false";
            // window.location.href = "/";
        })
        .catch(function(error) {
            parameters = "false";
            console.log(error);
        });
}

/////////////////// HYPERPARAMETERS : +/- LAYERS | NODES ///////////////////

function manipulateInpNodes(choice1, choice2) {
    var len = document.getElementById("no_of_hidden_layers");
    if (choice2 == 0) {
        var element = document.getElementById("input_nodes");
        var val = element.value;
        val = Number(val);
        var tag = document.getElementById("input_nodes_tag");
    } else {
        var element = document.getElementById("no_of_hidden");
        var val = element.value;
        val = Number(val);
        var tag = document.getElementById("hidden_tag");
    }

    if (choice1 === 0) {
        if (choice2 == 1) {
            var elmnt = document.getElementById("layer" + val);
            elmnt.remove();
            len.setAttribute("value", Number(val) - 1);
            len_nodes = val - 1;
        }
        if (val === 0) {
            val = 0;
        } else {
            val -= 1;
        }
        element.setAttribute("value", val);
        tag.innerHTML = val;
    } else if (choice1 === 1) {
        val += 1;
        element.setAttribute("value", val);
        tag.innerHTML = val;

        if (choice2 == 1) {
            var div_child = document.getElementById("add_layers");
            var p = document.createElement("div");
            p.className = "row";
            p.id = "layer" + val;
            var but1 = document.createElement("button");
            but1.innerHTML = "-";
            id = "layer" + val;
            but1.setAttribute("onclick", "manipulateHiddenNodes(0, id)");
            but1.id = "layer" + val;
            var but2 = document.createElement("button");
            but2.innerHTML = "+";
            but2.setAttribute("onclick", "manipulateHiddenNodes(1, id)");
            but2.id = "layer" + val;
            var text = document.createElement("b");
            text.innerHTML = "1";
            text.id = "layer" + val + "_tag";
            var hidden = document.createElement("input");
            hidden.setAttribute("type", "hidden");
            hidden.id = "layer" + val + "_node";
            hidden.value = 1;
            var span1 = document.createElement("span");
            span1.innerHTML = "&nbsp;";
            var span2 = document.createElement("span");
            span2.innerHTML = "&nbsp;";
            var span3 = document.createElement("span");
            span3.innerHTML = "&nbsp;";
            var test = document.createElement("span");
            test.innerHTML = "No. of nodes in layer " + val + " : ";
            var select = document.createElement("select");
            select.id = "layer" + val + "_select";
            var option0 = document.createElement("option");
            option0.innerHTML = "Choose Activation";
            option0.disabled = true;
            option0.selected = true;
            var option1 = document.createElement("option");
            option1.value = "sigmoid";
            option1.innerHTML = "Sigmoid";
            var option2 = document.createElement("option");
            option2.value = "tanh";
            option2.innerHTML = "Tanh";
            var option3 = document.createElement("option");
            option3.value = "relu";
            option3.innerHTML = "ReLU";
            var option4 = document.createElement("option");
            option4.value = "leaky_relu";
            option4.innerHTML = "Leaky ReLU";

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

            len.setAttribute("value", Number(val));
            len_nodes = val;
        }
    }
}

function manipulateOpNodes(choice) {
    var element = document.getElementById("output_nodes");
    var val = element.value;
    val = Number(val);
    var tag = document.getElementById("output_tag");
    if (choice === 0) {
        if (val === 1) {
            val = 1;
        } else {
            val -= 1;
        }
        element.setAttribute("value", val);
        tag.innerHTML = val;
    } else {
        val += 1;
        element.setAttribute("value", val);
        tag.innerHTML = val;
    }
}

function manipulateHiddenNodes(choice, id) {
    var element = document.getElementById(id + "_node");
    var val = element.value;
    val = Number(val);
    var tag = document.getElementById(id + "_tag");
    if (choice === 0) {
        if (val === 1) {
            val = 1;
        } else {
            val -= 1;
        }
        element.setAttribute("value", val);
        tag.innerHTML = val;
    } else {
        val += 1;
        element.setAttribute("value", val);
        tag.innerHTML = val;
    }
}

/////////////////// N-NETWORK ///////////////////

var width = 740,
    height = 440,
    nodeSize = 30;

function updateHoverCard(type, d, coordinates) {
    let hovercard = d3.select("#hovercard");
    if (type == null) {
        hovercard.style("display", "none");
        d3.select("#svg").on("click", null);
        return;
    }
    // d3.select("#svg").on("click", () => {
    //     hovercard.select(".value").style("display", "none");
    //     let input = hovercard.select("input");
    //     input.style("display", null);
    //     input.on("input", function() {
    //         if (this.value != null && this.value !== "") {
    //             if (type === "weight") {
    //                 d.weight = +this.value;
    //             } else {
    //                 d.bias = +this.value;
    //             }
    //             updateUI();
    //         }
    //     });
    //     input.on("keypress", () => {
    //         if (d3.event.keyCode === 13) {
    //             updateHoverCard(type, d, coordinates);
    //         }
    //     });
    //     input.node().focus();
    // });
    let value = type === "weight" ? d.weight : d.bias;
    let name = type === "weight" ? "Weight" : "Bias";

    let temp = document.getElementById("hovercard")
    temp.style.left = coordinates[0] + 20 + "px ";
    temp.style.top = coordinates[1] + 100 + "px";
    temp.style.display = "block";
    hovercard.select(".type").text(name);
    hovercard.select(".value").style("display", null).text(value.toPrecision(2));
    hovercard
        .select("input")
        .property("value", value.toPrecision(2))
        .style("display", "none");
}

function neuralNetwork() {

    console.log("nn")
    let linkWidthScale = d3.scale
        .linear()
        .domain([0, 5])
        .range([1, 10])
        .clamp(true);

    var color = d3.scale.category20();

    var svg = d3
        .select(".network")
        .append("svg")
        .attr("id", "svg")
        .attr("width", width)
        .attr("height", height);

    d3.json("data.json", function(error, graph) {
        var nodes = graph.nodes;
        var weights = graph.weights;
        var biases = graph.biases;

        // get network size
        var netsize = {};
        var _num = 0;
        nodes.forEach(function(d) {
            if (d.layer in netsize) {
                netsize[d.layer] += 1;
            } else {
                netsize[d.layer] = 1;
            }
            d["lidx"] = netsize[d.layer];
            d["bias"] = biases[_num++];
        });

        // calc distances between nodes
        var largestLayerSize = Math.max.apply(
            null,
            Object.keys(netsize).map(function(i) {
                return netsize[i];
            })
        );

        var xdist = width / Object.keys(netsize).length,
            ydist = height / largestLayerSize;

        nodes.map(function(d) {
            d["x"] = (d.layer - 0.5) * xdist;
            d["y"] = (d.lidx - 0.5) * ydist;
        });
        console.log(nodes);

        var links = [];
        var num = 0;
        nodes
            .map(function(d, i) {
                for (var n in nodes) {
                    if (d.layer + 1 == nodes[n].layer) {
                        links.push({
                            source: parseInt(i),
                            target: parseInt(n),
                            weight: weights[num++],
                        });
                    }
                }
            })
            .filter(function(d) {
                return typeof d !== "undefined";
            });

        var link = svg
            .selectAll(".link")
            .data(links)
            .enter()
            .append("line")
            .attr("class", "link")
            .attr("x1", function(d) {
                return nodes[d.source].x;
            })
            .attr("y1", function(d) {
                return nodes[d.source].y;
            })
            .attr("x2", function(d) {
                return nodes[d.target].x;
            })
            .attr("y2", function(d) {
                return nodes[d.target].y;
            })
            .style("stroke-width", function(d) {
                return linkWidthScale(Math.abs(d.weight));
            })
            .style("stroke-dasharray", "5, 2")
            .on("mouseenter", function(d) {
                updateHoverCard("weight", d, d3.mouse(this));
            })
            .on("mouseleave", function(d) {
                updateHoverCard(null);
            });

        // draw nodes
        var node = svg
            .selectAll(".node")
            .data(nodes)
            .enter()
            .append("g")
            .attr("transform", function(d) {
                return "translate(" + d.x + "," + d.y + ")";
            });

        var circle = node
            .append("circle")
            .attr("class", "node")
            .attr("r", nodeSize)
            .style("fill", function(d) {
                return color(d.layer);
            }).on("mouseenter", function(d) {
                updateHoverCard("bias", d, d3.mouse(circle.node()));
            })
            .on("mouseleave", function(d) {
                updateHoverCard(null);
            });

        node
            .append("text")
            .attr("dx", "-.35em")
            .attr("dy", ".35em")
            .text(function(d) {
                return d.label;
            });
    });
}


/////////////////// HISTOGRAM /////////////////////


function histogramData() {

    console.log("histogram")

    var margin = {
            top: 20,
            right: 30,
            bottom: 30,
            left: 40
        },
        width = 600 - margin.left - margin.right,
        height = 400 - margin.top - margin.bottom;

    // append the svg object to the body of the page
    var svg = d3.select("#my_dataviz")
        .append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
        .append("g")
        .attr("transform",
            "translate(" + margin.left + "," + margin.top + ")");


    // A formatter for counts.
    var formatCount = d3.format(",.0f");

    // get the data
    d3.csv("/col.csv", function(data) {

        var yAxis

        // A function that builds the graph for a specific value of bin
        function update(nBin) {

            // X axis: scale and draw:
            var x = d3.scaleLinear()
                .domain([d3.min(data, function(d) {
                    return +d.price
                }), d3.max(data, function(d) {
                    return +d.price
                })]) // can use this instead of 1000 to have the max of data: d3.max(data, function(d) { return +d.price })
                .range([0, width]);

            var xAxis = svg.append("g")
                .attr("transform", "translate(0," + height + ")")
                .call(d3.axisBottom(x));


            // set the parameters for the histogram
            var histogram = d3.histogram()
                .value(function(d) {
                    return d.price;
                }) // I need to give the vector of value
                .domain(x.domain()) // then the domain of the graphic
                .thresholds(x.ticks(nBin)); // then the numbers of bins

            // And apply this function to data to get the bins
            var bins = histogram(data);

            // Y axis: initialization
            var y = d3.scaleLinear()
                .range([height, 0]);

            yAxis = svg.append("g")

            // Y axis: update now that we know the domain
            y.domain([0, d3.max(bins, function(d) {
                return d.length;
            })]); // d3.hist has to be called before the Y axis obviously

            yAxis
                .enter()
                .merge(yAxis)
                .transition()
                .duration(1000)
                .call(d3.axisLeft(y));



            // Join the rect with the bins data
            var u = svg.selectAll(".bar")
                .data(bins)

            ///////////// Method 1 : Color Works
            //Append a defs (for definition) element to your SVG
            var defs = svg.append("defs");

            //Append a linearGradient element to the defs and give it a unique id
            var linearGradient = defs.append("linearGradient");

            //Horizontal gradient
            linearGradient
                .attr("x1", "100%")
                .attr("y1", "100%")
                .attr("x2", "0%")
                .attr("y2", "0%")
                .attr("id", "linear-gradient");

            //Set the color for the start (0%)
            linearGradient.append("stop")
                .attr("offset", "0%")
                .attr("stop-color", "#ffa474"); //light blue

            //Set the color for the end (100%)
            linearGradient.append("stop")
                .attr("offset", "100%")
                .attr("stop-color", "#8b0000"); //dark blue

            ///////////// Method 2 : X
            color = d3.scaleSequential()
                .domain([0, d3.max(data, d => d.price)])
                .interpolator(d3.interpolateBlues)

            ///////////// Method 3 : Works

            var color = "steelblue";
            var color2 = "purple"
            var yMax = d3.max(data, function(d) {
                return d.price
            });
            var yMin = d3.min(data, function(d) {
                return d.price
            });
            var colorScale = d3.scaleLinear()
                .domain([0, yMax])
                .range([d3.rgb(color).brighter(), d3.rgb(color)]);



            // Manage the existing bars and eventually the new ones:
            u
                .enter()
                .append("rect") // Add a new rect for each new elements
                .merge(u) // get the already existing elements as well
                .transition() // and apply changes to all of them
                .duration(1000)
                .attr("x", 1)
                .attr("transform", function(d) {
                    return "translate(" + x(d.x0) + "," + y(d.length) + ")";
                })
                .attr("width", function(d) {
                    return x(d.x1) - x(d.x0) - 1;
                })
                .attr("height", function(d) {
                    return height - y(d.length);
                })
                .style("fill", function(d) {
                    return colorScale(d.length)
                })


            u.enter()
                .append("text")
                .merge(u)
                .transition()
                .duration(1000)
                .attr("dy", ".6em")
                .attr("y", function(d) {
                    return (y(d.length) - 13);
                })
                .attr("x", function(d) {
                    return (x(d.x1) - (x(d.x1) - x(d.x0)) / 2)
                })
                .attr("text-anchor", "middle")
                .attr("class", "font-weight-light")
                .text(function(d) {
                    return formatCount(d.length);
                })

            // If less bar in the new histogram, I delete the ones not in use anymore
            u
                .exit()
                .remove()

        }
        // Initialize with 20 bins
        update(20)
            // Listen to the button -> update if user change it
        d3.select("#nBin").on("input", function() {
            d3.selectAll('text').remove()
            d3.selectAll('rect').remove()
            yAxis.remove()
            update(+this.value);
        });

    });
}

/////////////////// SLIDER /////////////////////

document.getElementById('range-slider').defaultValue = 30;
document.getElementById('range-result').innerHTML = '30%';

function updateSliderText() {
    var sliderValue = document.getElementById('range-slider').value;
    var percent = document.getElementById('range-result');
    percent.innerHTML = sliderValue + '%';
}

/////////////////// TEST /////////////////////

var input_nodes_for_test = Number(document.getElementById('no_of_inp_nodes').value);
var output_nodes_for_test = Number(document.getElementById('no_of_op_nodes').value);
var col1 = document.getElementById('addTestDataInputs');
var col2 = document.getElementById('addTestDataOutputs');

for (let i = 1; i <= input_nodes_for_test; i++) {
    var div = document.createElement('div');
    div.className = 'container';
    div.style = 'margin-top: 10px;';
    var temp1 = document.createElement('b');
    temp1.innerHTML = 'Input' + i;
    var span1 = document.createElement("span");
    span1.innerHTML = "&nbsp;";
    var temp2 = document.createElement('input');
    temp2.type = 'text';
    temp2.id = 'Input' + i;
    var temp3 = document.createElement('br');
    div.appendChild(temp1);
    div.appendChild(span1);
    div.appendChild(temp2);
    div.appendChild(temp3);
    col1.appendChild(div);
}

for (let i = 1; i <= output_nodes_for_test; i++) {
    var div = document.createElement('div');
    div.className = 'container';
    div.style = 'margin-top: 10px;';
    var temp1 = document.createElement('b');
    temp1.innerHTML = 'Output' + i;
    var span1 = document.createElement("span");
    span1.innerHTML = "&nbsp;&nbsp;&nbsp;";
    var temp2 = document.createElement('b');
    temp2.id = 'Output' + i;
    var temp3 = document.createElement('br');
    div.appendChild(temp1);
    div.appendChild(span1);
    div.appendChild(temp2);
    div.appendChild(temp3);
    col2.appendChild(div);
}

function getPredictedResults() {
    inps = [];
    for (let i = 1; i <= input_nodes_for_test; i++) {
        var doc = document.getElementById('Input' + i).value;
        inps.push(Number(doc));
    }
    axios.post('/predict', {
            test_inputs: inps,
        })
        .then(function(response) {
            var data = response.data.output;
            var len = response.data.output.length;

            for (let i = 1; i <= len; i++) {
                document.getElementById('Output' + i).innerHTML = data[i - 1];
            }
        })
        .catch(function(error) {
            console.log(error);
        })
}