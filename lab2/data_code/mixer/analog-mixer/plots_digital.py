from numpy import *
from matplotlib.pyplot import *

close('all')

x = load('roach-lo-10MHz-1-numeric.npz')
x1 = x['arr_1']
X1 = fft.fftshift(fft.fft(x1))
x = load('roach-lo-10MHz-2-numeric.npz')
x2 = x['arr_1']
X2 = fft.fftshift(fft.fft(x2))

subplot(4,1,1)
X1z = X1[len(X1)/3:2*len(X1)/3]
w = linspace(-5,5,len(X1z))
plot(w,abs(X1z)/max(abs(X1z)),'b')
title('LO = 10MHz, df = +5%')
xlabel('f [MHz]')
ylabel('|X(f)| (normalized)')

subplot(4,1,2)
X2z = X2[len(X2)/3:2*len(X2)/3]
w = linspace(-5,5,len(X2z))
plot(w,abs(X2z)/max(abs(X2z)),'g')
title('LO = 10MHz, df = -5%')
xlabel('f [MHz]')
ylabel('|X(f)| (normalized)')

subplot(4,1,3)
title('Mixer Output')
xlabel('t [ms]')

subplot(4,1,4)
title('Filtered Mixer Output')
xlabel('t [ms]')

show()