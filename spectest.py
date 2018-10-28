import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pyaudio
import struct
import wave
 
 
SAVE = 0.0
TITLE = ''
FPS = 25.0
 
nFFT = 512
BUF_SIZE = 4 * nFFT
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
 
 
def animate(i, line, stream, wf, MAX_y):
 
  # Read n*nFFT frames from stream, n > 0
  N = max(stream.get_read_available() / nFFT, 1) * nFFT
  data = stream.read(N)
  if SAVE:
    wf.writeframes(data)
 
  # Unpack data, LRLRLR...
  y = np.array(struct.unpack("%dh" % (N * CHANNELS), data)) / MAX_y
  y_L = y[::2]
  y_R = y[1::2]
 
  Y_L = np.fft.fft(y_L, nFFT)
  Y_R = np.fft.fft(y_R, nFFT)
 
  # Sewing FFT of two channels together, DC part uses right channel's
  Y = abs(np.hstack((Y_L[-nFFT/2:-1], Y_R[:nFFT/2])))
 
  line.set_ydata(Y)
  return line,
 
 
def init(line):
 
  # This data is a clear frame for animation
  line.set_ydata(np.zeros(nFFT - 1))
  return line,
 
 
def main():
  
  fig = plt.figure()
  f = Figure(figsize=(5,4), dpi=100)
  # Frequency range
  x_f = 1.0 * np.arange(-nFFT / 2 + 1, nFFT / 2) / nFFT * RATE
  ax = f.add_subplot(111, title=TITLE, xlim=(x_f[0], x_f[-1]),
                       ylim=(0, 2 * np.pi * nFFT**2 / RATE))
  ax.set_yscale('symlog', linthreshy=nFFT**0.5)
 
  line, = ax.plot(x_f, np.zeros(nFFT - 1))
 
  
 
  p = pyaudio.PyAudio()
  # Used for normalizing signal. If use paFloat32, then it's already -1..1.
  # Because of saving wave, paInt16 will be easier.
  MAX_y = 2.0**(p.get_sample_size(FORMAT) * 8 - 1)
 
  frames = None
  wf = None
 
  stream = p.open(format=FORMAT,
                  channels=CHANNELS,
                  rate=RATE,
                  input=True,
                  frames_per_buffer=BUF_SIZE)
 
  ani = animation.FuncAnimation(fig, animate, frames,
      init_func=lambda: init(line), fargs=(line, stream, wf, MAX_y),
      interval=1000.0/FPS, blit=True)
 
  

  dataPlot = FigureCanvasTkAgg(f, master=top)
  dataPlot.show()
  dataPlot.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
 
  stream.stop_stream()
  stream.close()
  p.terminate()
 
  if SAVE:
    wf.close()
 
 
if __name__ == '__main__':
  main()
