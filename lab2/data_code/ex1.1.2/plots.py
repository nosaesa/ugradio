from numpy import *
from matplotlib.pyplot import *

close('all')
n = arange(0,10)
x = load('sig-3MHz-samp-500Hz.npz')

x1 = x['arr_1']
x1 = x1[0:10]
subplot(2,1,1)
plot(n,x1,'b')
title('vsig = 6000vsmpl')
xlabel('t [us]')
ylabel('Volts')
subplot(2,1,2)
n = arange(0,117600)
n = n/6000000.
sig = cos(2*pi*3000000*n)
plot(sig)

show()