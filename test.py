from getData import *
import pybrain as pb
from pybrain.tools.shortcuts import buildNetwork
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer

trainData = getData('data_2.csv');
testData = getData('data_1_2.csv');

#training
fnn = buildNetwork(24, 30, 8, 1, bias=True);
ds = SupervisedDataSet(24, 1);
for i in trainData:
	ds.addSample([i[j] for j in Name[1:]], i[Name[0]]);
trainer = BackpropTrainer(fnn, ds);
print "Begin....";
trainer.trainEpochs(epochs=100);
print "Ing...";
out = SupervisedDataSet(24, 1);
for i in testData:
	out.addSample([i[j] for j in Name[1:]], [0]);

res = fnn.activateOnDataset(out);

for i, o in out:
	print i, "->", o;
print res  