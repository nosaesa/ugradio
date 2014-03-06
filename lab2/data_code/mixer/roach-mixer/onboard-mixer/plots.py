from numpy import *
from matplotlib.pyplot import *

close('all')

x = load('roach-lo-10MHz-1-numeric.npz')
x1 = x['arr_1']
X1 = fft.fftshift(fft.fft(x1))
x = load('roach-lo-10MHz-2-numeric.npz')
x2 = x['arr_1']
X2 = fft.fftshift(fft.fft(x2))
x = load('onboard-lo-1-numeric.npz')
xcos = x['arr_2']
xsin = x['arr_3']
xr = xcos + 1j*xsin
XR = fft.fftshift(fft.fft(xr))
XCOS = fft.fftshift(fft.fft(xcos))
XSIN = fft.fftshift(fft.fft(xsin))

subplot(3,1,1)
X1z = X1[len(X1)/3:2*len(X1)/3]
X2z = X2[len(X2)/3:2*len(X2)/3]
w = linspace(-3.33,3.33,len(X1z))
plot(w,abs(X1z)/max(abs(X1z)),'b',label='df = +5%')
plot(w,abs(X2z)/max(abs(X2z)),'g',label='df = -5%')
title('DSB Mixer Output, LO = 10MHz')
xlabel('f [MHz]')
ylabel('|X(f)| (normalized)')
legend()

subplot(3,1,2)
XRz = XR[len(XR)/3:2*len(XR)/3]
w = linspace(-3.33,3.33,len(XRz))
plot(w,abs(XRz)/max(abs(XRz)))
title('Reconstructed SSB Mixer Output')
xlabel('f [MHz]')
ylabel('|X(f)| (normalized)')

subplot(3,1,3)
XCz = XCOS[len(XCOS)/3:2*len(XCOS)/3]
XSz = XSIN[len(XSIN)/3:2*len(XSIN)/3]
w = linspace(-3.33,3.33,len(XCz))
plot(w,abs(XCz)/max(abs(XCz)),'g',label='I')
plot(w,abs(XSz)/max(abs(XSz)),'r',label='Q')
title('SSB Mixer I/Q Outputs')
xlabel('f [MHz]')
ylabel('|X(f)| (normalized)')
legend()

show()