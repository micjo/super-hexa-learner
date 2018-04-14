#!/usr/bin/env python

import pyscreenshot

im = pyscreenshot.grab()
im.save('example.png')
im.show()

