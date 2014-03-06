from numpy import *
from matplotlib.pyplot import *

close('all')
n = arange(0,50)
x = np.load('signal-1.npz')

x1 = x['arr_1']
X1 = fft.fftshift(fft.fft(x1))
w = linspace(-.5,.5,len(X1))
x1 = x1[0:50]
subplot(3,2,1)
stem(n,x1,'b')
title('vsig = 0.1vsmpl')
xlabel('t [us]')
ylabel('Volts')
subplot(3,2,2)
plot(w,abs(X1)/max(abs(X1)),'g')
title('Power Spectrum of vsig = 0.1vsmpl')
xlabel('f [MHz]')
ylabel('|X(f)| (normalized)')

x = np.load('signal-5.npz')
x5 = x['arr_1']
X5 = fft.fftshift(fft.fft(x5))
x5 = x5[0:50]
subplot(3,2,3)
stem(n,x5,'b')
title('vsig = 0.5vsmpl')
xlabel('t [us]')
ylabel('Volts')
subplot(3,2,4)
plot(w,abs(X5)/max(abs(X5)),'g')
title('Power Spectrum of vsig = 0.5vsmpl')
xlabel('f [MHz]')
ylabel('|X(f)| (normalized)')

x = np.load('signal-9.npz')
x9 = x['arr_1']
X9 = fft.fftshift(fft.fft(x9))
x9 = x9[0:50]
subplot(3,2,5)
stem(n,x9,'b')
title('vsig = 0.9vsmpl')
xlabel('t [us]')
ylabel('Volts')
subplot(3,2,6)
plot(w,abs(X9)/max(abs(X9)),'g')
title('Power Spectrum of vsig = 0.9vsmpl')
xlabel('f [MHz]')
ylabel('|X(f)| (normalized)')

show()