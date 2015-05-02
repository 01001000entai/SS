from getData import *
from math import *
import matplotlib.pyplot as plt

def d2p(x):
	if x < 90:
		x = x;
	elif x < 180:
		x = 180 - x;
	elif x < 270:
		x = x - 180;
	else:
		x = 360 - x;
	return x/180*pi

data = getData('data_2.csv');
l = len(data);
x = range(l);
y1 = [i['power'] for i in data];
y2 = [ (i['WS30']*cos(d2p(i['DIRECTION30']))+i['WS31']*cos(d2p(i['DIRECTION31']))+ \
	 i['WS32']*cos(d2p(i['DIRECTION32']))+i['WS10']*cos(d2p(i['DIR10']))+ \
	 i['WS10S']*cos(d2p(i['DIR10S'])))**3 for i in data];
print y1;
print y2;

plt.figure(figsize=(16,8));
plt.plot(y2, y1, 'o');
#plt.plot(x, y1, 'r', linewidth=2);
#plt.plot(x, y2, 'b', linewidth=2);
plt.legend()

plt.show() 