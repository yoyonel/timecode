About
-----

Python Module for manipulating SMPTE timecode. Supports 23.98, 24, 25, 29.97,
30, 50, 59.94, 60 frame rates and milliseconds (1000 fps).

The math behind the drop frame calculation is based on the
[blog post of David Heidelberger](http://www.davidheidelberger.com/blog/?p=29).

Simple math operations like, addition, subtraction, multiplication or division
with an integer value or with a timecode is possible. Math operations between
timecodes with different frame rates are supported. So:

  from pytimecode import PyTimeCode

  tc1 = PyTimeCode('29.97', '00:00:00:00')
  tc2 = PyTimeCode('24', '00:00:00:10')
  tc3 = tc1 + tc2
  assert tc3.framerate == '29.97'
  assert tc3.frames == 12
  assert tc3 == '00:00:00:11'

Creating a PyTimeCode instance with a start timecode of '00:00:00:00' will
result a timecode object where the total number of frames is 1. So:

  tc4 = PyTimeCode('24', '00:00:00:00')
  assert tc4.frames == 1

Use the ``frame_number`` attribute if you want to get a 0 based frame number:

  assert tc4.frame_number == 0

Frame rates 29.97 and 59.94 are always drop frame, and all the others are non
drop frame.

The SMPTE standard limits the timecode with 24 hours. Even though, PyTimeCode
instance will show the current timecode inline with the SMPTE standard, it will
keep counting the total frames without clipping it.

Copyright 2014 Joshua Banton and PyTimeCode developers.
