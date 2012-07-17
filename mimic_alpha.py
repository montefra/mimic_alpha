"""
The function 'colorAlpha_to_rgb' returns a RGB color that mimic a RGBA on a given background
The code implements the algorithm from: http://stackoverflow.com/questions/2049230/convert-rgba-color-to-rgb?rq=1

The code has not been tested. 
A by eye comparison between a pdf image with alpha channel and 
a few values for the input color/alpha on white background shows that this approach is 'good enough'.

Dependances:
  Numpy
  Matplotlib

Licence:
  This a free sofware and come without any warranty.
  It can be freely used, modified and redistributed, 
  with the only requirement that the author (Francesco Montesano) 
  and the inspiration for the algorithm (http://stackoverflow.com/questions/2049230/convert-rgba-color-to-rgb?rq=1)
  are aknowledged.
"""

from matplotlib.colors import colorConverter as cC
import numpy as np

__version__ = 0.10
__author__ = "Francesco Montesano (franz.bergesund@gmail.com)"

def _to_rgb(c):
  """
  Convert color *c* to a numpy array of *RGB* handling exeption
  Parameters
  ----------
  c: Matplotlib color
    same as *color* in *colorAlpha_to_rgb*
  output
  ------
  rgb: numpy array
    *RGB* array
  """

  c= cC.to_rgb(c)
  return np.array(c)

def is_number(s):
  """
  Check if *c* is a number (from http://stackoverflow.com/questions/354038/how-do-i-check-if-a-string-is-a-number-in-python)
  Parameters
  ----------
  c: variable
  output
  ------
  true if c is a number
  false otherwise
  """
  try:
    float(s) # for int, long and float
  except ValueError:
    return False
  return True


def colorAlpha_to_rgb(color, alpha, bg='w'):
  """
  Given a Matplotlib color and a value of alpha, it returns 
  a RGB color which mimic the RGBA colors on the given background

  Parameters
  ----------
  color: Matplotlib color (documentation from matplotlib.colors.colorConverter.to_rgb)
    Can be an *RGB* or *RGBA* sequence or a string in any of
    several forms:
    1) a letter from the set 'rgbcmykw'
    2) a hex color string, like '#00FFFF'
    3) a standard name, like 'aqua'
    4) a float, like '0.4', indicating gray on a 0-1 scale
    if *color* is *RGBA*, the *A* will simply be discarded.
  alpha: float [0,1]
    Value of alpha to mimic. 
  bg: Matplotlib color (optional, default='w')
    Color of the background. Can be of any type shown in *color*

  output
  ------
  rgb: *RGB* color 

  example
  -------

  import mimic_alpha.mimic_alpha as ma
  
  print( ma.colorAlpha_to_rgb('r', 0.5') )
  >>> [ 1.   0.5  0.5]



  """

  color = _to_rgb(color)  #convert the color
  bg = _to_rgb(bg)   #convert the background
  if( is_number(alpha) == False or alpha < 0 or alpha > 1):
    raise ValueError("'alpha' must be a float with value between 0 and 1, included") 

  rgb = (1.-alpha) * bg + alpha*color  #interpolate between background and color

  return rgb

