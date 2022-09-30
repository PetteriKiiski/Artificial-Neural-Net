#A working AI neural net with biases, nodes, and trainable weights, so that I can make it do fun things
#But for starters, I am going to make it return its inverse nodes
#ex1. input:1011, output:0100
#ex2. input:0101, output:1010
#ex3. input:1101, output:1101

#Class which contains a layer of nodes, and weights
class Layer:
    def __init__(self, layer = 0):
        self.connectingLayer = layer
        #This list just contains bias values
        self.nodes = []
        self.weights = []
        #Each connecting node has its own wait(:P) list
        if self.connectingLayer != 0:
            for x in self.connectingLayer.nodes:
                self.weights.append([])
    def add_node(self, node, weight):
        self.nodes.append(node)
        for x in self.weights:
            x.append(weight)

#Run the neural net
def run_net(inputVals, inputLayer):
    #Key thing here:
    #int(sum(values) >= bias)
    output = []
    #Each next layer will
    for x in inputLayer.connectingLayer.nodes:
        output.append(0)
    for x in range(len(output)):
        for y in range(len(inputVals)):
            output[x] += inputVals[y] * inputLayer.weights[x][y]
    for x in range(len(output)):
        if inputLayer.connectingLayer.connectingLayer != 0:
            output[x] = int(output[x] >= inputLayer.connectingLayer.nodes[x])
        else:
            return output
    return run_net(output, inputLayer.connectingLayer)
#Creating four Layer instances, connected to eachother
#Also adding nodes
OutLayer = Layer()
for x in range(4):
    OutLayer.add_node(0.5, 1)

Layer2 = Layer(OutLayer)
for x in range(16):
    Layer2.add_node(0.5, 0.75)

Layer1 = Layer(Layer2)
for x in range(16):
    Layer1.add_node(0.5, 0.25)

InLayer = Layer(Layer1)
for x in range(4):
    InLayer.add_node(0.5, 0.25)

print (run_net([1, 0, 1, 1], InLayer))
