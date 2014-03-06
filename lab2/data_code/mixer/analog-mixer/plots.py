from numpy import *
from matplotlib.pyplot import *

close('all')

x = load('lo-1MHz-1.npz')
x1 = x['arr_1']
X1 = fft.fftshift(fft.fft(x1))
X1f = fft.fft(x1)
X1f[20000:len(X1f)-20000] = 0
x1f = real(fft.ifft(X1f))
x = load('lo-1MHz-2.npz')
x2 = x['arr_1']
X2 = fft.fftshift(fft.fft(x2))

subplot(4,1,1)
X1z = X1[len(X1)/3:2*len(X1)/3]
w = linspace(-5,5,len(X1z))
plot(w,abs(X1z)/max(abs(X1z)),'b')
title('LO = 1MHz, df = +5%')
xlabel('f [MHz]')
ylabel('|X(f)| (normalized)')

subplot(4,1,2)
X2z = X2[len(X2)/3:2*len(X2)/3]
w = linspace(-5,5,len(X2z))
plot(w,abs(X2z)/max(abs(X2z)),'g')
title('LO = 1MHz, df = -5%')
xlabel('f [MHz]')
ylabel('|X(f)| (normalized)')

subplot(2,2,3)
n = range(0,1000)
n = array(n)/50.
plot(n,x1[0:1000])
title('Mixer Output')
xlabel('t [ms]')

subplot(2,2,4)
n = range(0,1000)
n = array(n)/50.
plot(n,x1f[0:1000])
title('Filtered Mixer Output')
xlabel('t [ms]')

show()