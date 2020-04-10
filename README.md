# Pluto-SDR-FM-Rx
Software Defined Radio

# Purpose

Demodulate FM signal picked up through Dipole antenna

## Hardware 
1. [Rabbit ear telescopic antenna](https://www.amazon.com/Behind-Indoor-Replacement-Antenna-Extension/dp/B07KMF3SSG/ref=sr_1_8?dchild=1&keywords=rabbit+ear+antenna&qid=1586538911&sr=8-8):


<img src="https://i.pinimg.com/736x/68/62/d1/6862d1e6e541db3c6d2559778989b7e2.jpg" width="300" height="300">

2. [Analog devices PLUTO SDR](https://www.analog.com/en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/adalm-pluto.html):

![alt text][SDR]

[SDR]: https://www.analog.com/-/media/analog/en/evaluation-board-images/images/adalm-pluto-web.gif?la=en&h=270&thn=1&hash=AC178C96A25ABD5C1234C238DCC75145 "SDR used"

## Software 

1. [GNU Radio companion](https://wiki.gnuradio.org/index.php/Main_Page)

<img src="https://github.com/KiranKanchi/Pluto-SDR-FM-Rx/blob/master/Screen%20shots/GRC_Signal_flow.png?raw=true" width="1000" height="500">

<img src="https://github.com/KiranKanchi/Pluto-SDR-FM-Rx/blob/master/Screen%20shots/Station_2.png" width="1000" height="500">

## Details

FM Reception and demodulation is much like hello world of Radio electronics. :rocket:

My simple GRC project connects to pluto-sdr as signal source, perform a bunch of signal transformation such as filtering, decimating, scaling & eventually fed to audio sink to listen to the broadcast.
On successfully executing the .grc project, you should see two graphs of Power (dB) vs Frequency.
I have enabled two slider/variables. 

* Receiver gain
* Volume gain

you can tune into your local FM station by setting the Local oscillator of your SDR to FM channel frequency.

In my case following are valid FM stations *91.1e6, 91.9e6, 92.7e6, 93.5e6, 94.3e6, 98.3e6* in Hz labelled as *1, 2, 3, 4, 5, 6*.  





