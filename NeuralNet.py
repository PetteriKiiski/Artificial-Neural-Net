#A working AI neural net with biases, nodes, and trainable weights, so that I can make it do fun things
#But for starters, I am going to make it return its inverse nodes
#ex1. input:1011, output:0100
#ex2. input:0101, output:1010
#ex3. input:1101, output:1101

#Basic Node
#Might get rid of this, though I may add function
class Node:
    def __init__(self, bias):
        self.bias = bias

#Class which contains a layer of nodes, and weights
class Layer:
    def __init__(self, layer = 0):
        self.connectingLayer = layer
        self.nodes = []
        self.weights = []
    def add_node(self, node, weight):
        self.nodes.append(node)
        for x in self.weights:
            x.append(weight)

#Creating four Layer instances, connected to eachother
OutLayer = Layer()
Layer2 = Layer(OutLayer)
Layer1 = Layer(Layer2)
InLayer = Layer(Layer1)

#Adding nodes
for x in range(4):
    InLayer.add_node(Node(0.5) , 0)
for x in range(16):
    Layer1.add_node(Node(0.5) , 0)
for x in range(16):
    Layer2.add_node(Node(0.5), 0)
for x in range(4):
    OutLayer.add_node(Node(0.5), 0)
