import math

records = """
2 0 No
0 2 No
4 2 Yes
2 4 Yes
""".split('\n')[1:-1]
newRecord = ""
training_order = "1 2 3 4 1"
recordID = False
# output_0, output_1 = "0", "1"
output_0, output_1 = "No", "Yes"
activation_func_name = "threshold" # "threshold", "linear", "ReLU", "sigmoid", "tanh"
weights = [0.3, 0.3, 0.3]
learning_rate = 0.6
record_type = int

if recordID:
    records = [record.split()[1:] for record in records]
    newRecord = newRecord.split()
else:
    records = [record.split() for record in records]
    newRecord = newRecord.split()
records_attr = [list(map(record_type, record[:-1])) for record in records]
records_target = [(0 if record[-1]==output_0 else 1 if record[-1]==output_1 else -1) for record in records]
if -1 in records_target:
    raise Exception("wrong target attribute")
newRecord = list(map(record_type, newRecord))
attrCount = len(records_attr[0])
# check
newRecordFlag = 1
if (len(newRecord) != attrCount):
    print(f"new record has wrong no. of attributes! expected {attrCount} got {len(newRecord)}")
    newRecordFlag = 0
training_order = list(map(lambda x: int(x)-1, training_order.split()))
print(training_order)
# check
if (len(weights) != attrCount + 1):
    raise Exception(f"no. of weights incorrect! expected {attrCount + 1} got {len(weights)}")

def evaluate(record):
    return sum([rec_attr*weight for rec_attr, weight in zip(record, weights[:-1])]) + weights[-1]
    # calculates net

def write(x):
    pass
def writeEq(x, newline=False):
    pass

def writeColumnStart():
    pass
def writeColumnNext():
    pass
def writeColumnEnd():
    pass

activation_func = {
    "threshold": lambda net: 1 if net>=0 else 0,
    "linear": lambda net: net,
    "ReLU": lambda net: 0 if net<0 else net,
    "sigmoid": lambda net: 1/(1+math.exp(-net)),
    "tanh": lambda net: math.tanh(net)
}[activation_func_name]


formula_net = "".join([f"w_{i+1}x_{i+1}+" for i in range(attrCount)])+"b"
def formula_weight(i):
    return  f"w_{i}&\\leftarrow w_{i}+\\alpha(d-y)x_{i}"
formula_bias = f"b&\leftarrow b+\\alpha(d-y)"

print(weights)
for iteration, record_id in enumerate(training_order):
    net = evaluate(records_attr[record_id])
    y = activation_func(net)
    prevWeights = weights
    weights = [weight + 
        learning_rate*(records_target[record_id] - y)*x
        for weight, x in zip(weights, records_attr[record_id] + [1])]
    
    print("#"*2+f" **Iteration {iteration + 1}**\n")
    print("net", net)
    print("y", y)
    print("weights", weights)

if newRecordFlag:
    print("newRecord", evaluate(newRecord))
    y = evaluate(newRecord)
    net = activation_func(y)
    




