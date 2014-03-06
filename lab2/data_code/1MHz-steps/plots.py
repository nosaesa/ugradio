from numpy import *
from matplotlib.pyplot import *

close('all')
n = arange(0,50)
x = np.load('signal-1.npz')

x1 = x['arr_1']
X1 = fft.fftshift(fft.fft(x1))
w = linspace(-.5,.5,len(X1))
x1 = x1[0:50]
subplot(6,3,1)
plot(n,x1,'b')
title('vsig = 0.1vsmpl')
xlabel('t [us]')
ylabel('Volts')
subplot(6,3,4)
plot(w,abs(X1)/max(abs(X1)),'g')
xlabel('f [MHz]')
ylabel('|X(f)| (normalized)')

x = np.load('signal-2.npz')
x2 = x['arr_1']
X2 = fft.fftshift(fft.fft(x2))
x2 = x2[0:50]
subplot(6,3,2)
plot(n,x2,'b')
title('vsig = 0.2vsmpl')
xlabel('t [us]')
ylabel('Volts')
subplot(6,3,5)
plot(w,abs(X2)/max(abs(X2)),'g')
xlabel('f [MHz]')
ylabel('|X(f)| (normalized)')

x = np.load('signal-3.npz')
x3 = x['arr_1']
X3 = fft.fftshift(fft.fft(x3))
x3 = x3[0:50]
subplot(6,3,3)
plot(n,x3,'b')
title('vsig = 0.3vsmpl')
xlabel('t [us]')
ylabel('Volts')
subplot(6,3,6)
plot(w,abs(X3)/max(abs(X3)),'g')
xlabel('f [MHz]')
ylabel('|X(f)| (normalized)')

x = np.load('signal-4.npz')
x4 = x['arr_1']
X4 = fft.fftshift(fft.fft(x4))
x4 = x4[0:50]
subplot(6,3,7)
plot(n,x4,'b')
title('vsig = 0.4vsmpl')
xlabel('t [us]')
ylabel('Volts')
subplot(6,3,10)
plot(w,abs(X4)/max(abs(X4)),'g')
xlabel('f [MHz]')
ylabel('|X(f)| (normalized)')

x = np.load('signal-5.npz')
x5 = x['arr_1']
X5 = fft.fftshift(fft.fft(x5))
x5 = x5[0:50]
subplot(6,3,8)
plot(n,x5,'b')
title('vsig = 0.5vsmpl')
xlabel('t [us]')
ylabel('Volts')
subplot(6,3,11)
plot(w,abs(X5)/max(abs(X5)),'g')
xlabel('f [MHz]')
ylabel('|X(f)| (normalized)')

x = np.load('signal-6.npz')
x6 = x['arr_1']
X6 = fft.fftshift(fft.fft(x6))
x6 = x6[0:50]
subplot(6,3,9)
plot(n,x6,'b')
title('vsig = 0.6vsmpl')
xlabel('t [us]')
ylabel('Volts')
subplot(6,3,12)
plot(w,abs(X6)/max(abs(X6)),'g')
xlabel('f [MHz]')
ylabel('|X(f)| (normalized)')

x = np.load('signal-7.npz')
x7 = x['arr_1']
X7 = fft.fftshift(fft.fft(x7))
x7 = x7[0:50]
subplot(6,3,13)
plot(n,x7,'b')
title('vsig = 0.7vsmpl')
xlabel('t [us]')
ylabel('Volts')
subplot(6,3,16)
plot(w,abs(X7)/max(abs(X7)),'g')
xlabel('f [MHz]')
ylabel('|X(f)| (normalized)')

x = np.load('signal-8.npz')
x8 = x['arr_1']
X8 = fft.fftshift(fft.fft(x8))
x8 = x8[0:50]
subplot(6,3,14)
plot(n,x8,'b')
title('vsig = 0.8vsmpl')
xlabel('t [us]')
ylabel('Volts')
subplot(6,3,17)
plot(w,abs(X8)/max(abs(X8)),'g')
xlabel('f [MHz]')
ylabel('|X(f)| (normalized)')

x = np.load('signal-9.npz')
x9 = x['arr_1']
X9 = fft.fftshift(fft.fft(x9))
x9 = x9[0:50]
subplot(6,3,15)
plot(n,x9,'b')
title('vsig = 0.9vsmpl')
xlabel('t [us]')
ylabel('Volts')
subplot(6,3,18)
plot(w,abs(X9)/max(abs(X9)),'g')
xlabel('f [MHz]')
ylabel('|X(f)| (normalized)')

show()