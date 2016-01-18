#!/usr/bin/python2
# Spoke calculator for bicycle wheels written in python 2.7,
# Author: Kim Nojdberg,
# License: GPLv3.

import sys, argparse, math

__version__ = 'v0.0.2'
parser = argparse.ArgumentParser()
parser.add_argument('--version', action='version', version='%(prog)s {version}'.format(version=__version__))
parser.add_argument('-e', '--erd', help='Effective rim diameter, mm', type=float,)
parser.add_argument('-r', '--shr', help='Radius of spoke hole circle, mm', type=float,)
parser.add_argument('-s', '--spokes', help='Number of spokes', type=float,)
parser.add_argument('-c', '--crossings', help='Number of crossings', type=float,)
parser.add_argument('-d', '--hubtoleftflange', help='Distance from center of hub to left flange center, mm', type=float,)
parser.add_argument('-f', '--hubtorightflange', help='Distance from center of hub to right flange center, mm', type=float,)
parser.add_argument('-x', '--holeradius', help='Radius of spoke holes, mm', type=float,)
args = parser.parse_args()

# Variables:
# 
# args.erd              = ERD (effective rim diameter)
# args.shr              = Radius of spoke hole circle
# args.spokes           = Number of spokes
# args.crossings        = Number of times a spoke crosses another spoke (0 means radial)
# args.hubtoleftflange  = Distance from center of hub to left flange center
# args.hubtorightflange = Distance from center of hub to right flange center
# args.holeradius       = Radius of spoke hole
# angle                 = Angle at meeting point of erdhalf and shr
# radians               = Above-mentioned angle expressed in radians (for math.cos function)
# leftlength            = Calculated spoke length for the left side of the wheel
# rightlength           = Calculated spoke length for the right side of the wheel

def give_spoke_length(erd, shr, spokes, crossings, hubtoflange, holeradius):
    angle = 360 * ( crossings / (spokes/2) )
    radians = angle * (math.pi/180)
    length = round( math.sqrt ( (hubtoflange**2) + (shr**2) + ((erd/2)**2) \
            - (2*shr*(erd/2) * math.cos(radians)) - holeradius ))
    return length

if type(args.hubtorightflange) == float:
    rightlength = give_spoke_length (args.erd, args.shr, args.spokes, args.crossings, args.hubtorightflange, args.holeradius)
else:
    rightlength = leftlength

leftlength = give_spoke_length (args.erd, args.shr, args.spokes, args.crossings, args.hubtoleftflange, args.holeradius)

print'Left side spoke length:', leftlength,'mm'
print'Right side spoke length:', rightlength, 'mm\n'
