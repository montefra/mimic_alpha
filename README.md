mimic_alpha
===========

The function `colorAlpha_to_rgb` returns a list of RGB color that mimic 
a RGBA on a given background.
The code implements the algorithm from 
[this stackoverflow post](http://stackoverflow.com/questions/2049230/convert-rgba-color-to-rgb?rq=1y%)

The code has not been much tested. 
A by eye comparison between a pdf image with alpha channel and 
a few values for the input color/alpha on white background shows that this approach is 'good enough'.

Dependances:
  Numpy
  Matplotlib

Works with python 2.7 and 3.2 (and likely 3.3)

Licence:
  This a free sofware and come without any warranty.
  It can be freely used, modified and redistributed, 
  with the only requirement that the author (Francesco Montesano) 
  and the inspiration for the algorithm
  (http://stackoverflow.com/questions/2049230/convert-rgba-color-to-rgb?rq=1)
  are aknowledged.

version 0.21
author: "Francesco Montesano (franz.bergesund@gmail.com)"


example
-------

    import mimic_alpha as ma

    print(ma.colorAlpha_to_rgb('r', 0.5))
    >>> [array([ 1. ,  0.5,  0.5])]
    print(ma.colorAlpha_to_rgb(['r', 'g'], 0.5)) 
    >>> [array([ 1. ,  0.5,  0.5]), array([ 0.5 ,  0.75,  0.5 ])]
    print(ma.colorAlpha_to_rgb(['r', 'g'], [0.5, 0.3])) 
    >>> [array([ 1. ,  0.5,  0.5]), array([ 0.7 ,  0.85,  0.7 ])]
    print(ma.colorAlpha_to_rgb(['r', [1,0,0]], 0.5)) 
    >>> [array([ 1. ,  0.5,  0.5]), array([ 1. ,  0.5,  0.5])]
    print( ma.colorAlpha_to_rgb([[0,1,1], [1,0,0]], 0.5) ) 
    >>> [array([ 0.5,  1. ,  1. ]), array([ 1. ,  0.5,  0.5])]
    print(ma.colorAlpha_to_rgb(np.array([[0,1,1], [1,0,0]]), 0.5)) 
    >>> [array([ 0.5,  1. ,  1. ]), array([ 1. ,  0.5,  0.5])]
    print(ma.colorAlpha_to_rgb(np.array([[0,1,1], [1,0,0]]), 0.5, bg='0.5')) 
    >>> [array([ 0.25,  0.75,  0.75]), array([ 0.75,  0.25,  0.25])]
