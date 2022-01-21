#программа численного интегрирования площади под кривой.

import math


def integrate(f, a, b, *, n_iter=10**6):
  h = (b-a)/n_iter # step
  s = 0 # square
  x = a
  while (x <= (b-h)):
    s = s+f(x)
    x += h

  return float(h*s)
        # точность 10*-8

# или можно так: 
#  def integrate(f, a, b, n_iter=1000):
#        pass
#        #точность 10*-8

# а и b - диапазон интегрирования

if __name__ == '__main__':
  I = integrate(math.cos,3,7)
  print(I)
  assert integrate(math.cos,3,7) == 0.5158631028464435, "Ответ неверный"
  pass
