#!/usr/bin/env python
# -*- coding: utf-8 -*-
__Auther__ = 'M4x'

buf = [0x01, 0x16, 0x79, 0x44, 0x04, 0x64, 0x12, 0x5A, 0x01, 0x0C,
0x2F, 0x21, 0x72, 0x53, 0x60, 0x16, 0x02, 0x2A, 0x16, 0x24,
0x33, 0x62, 0x60, 0x7B ]
f = map(ord, "0x00CTF{")

key = ''.join([chr(x^y) for x,y in zip(f, buf)])

print key