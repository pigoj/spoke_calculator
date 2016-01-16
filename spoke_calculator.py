#!/usr/bin/python2
# Spoke calculator for bicycle wheels written in python 2.7,
# Author: Kim Nojdberg,
# License: GPLv3.

import sys, argparse, math

__version__ = 'v0.0.1'
parser = argparse.ArgumentParser()
parser.add_argument('--version', action='version', version='%(prog)s {version}'.format(version=__version__))
parser.add_argument('-e', '--erd', help='Effective rim diameter, mm', type=float,)
parser.add_argument('-r', '--shr', help='Radius of spoke hole circle, mm', type=float,)
parser.add_argument('-s', '--spokes', help='Number of spokes', type=float,)
parser.add_argument('-c', '--crossings', help='Number of crossings', type=float,)
parser.add_argument('-d', '--hubtoflange', help='Distance from center of hub to flange center, mm', type=float,)
parser.add_argument('-x', '--holeradius', help='Radius of spoke holes, mm', type=float,)
args = parser.parse_args()

# Variables:
# 
# erd           = ERD (effective rim diameter)
# erdhalf       = ERD devided by 2
# shr           = Radius of spoke hole circle
# spokes        = Number of spokes
# crossings     = Number of times a spoke crosses another spoke (0 means radial)
# hubtoflange   = Distance from center of hub to flange center
# holerad       = Radius of spoke hole
# angle         = Angle at meeting point of erdhalf and shr
# radians       = Above-mentioned angle expressed in radians (for math.cos function)
# length        = Calculated spoke length

erd = args.erd
erdhalf = erd/2
shr = args.shr
spokes = args.spokes
crossings = args.crossings
hubtoflange = args.hubtoflange
holerad = args.holeradius
angle = 360 * ( crossings / (spokes/2) )
radians = angle * (math.pi/180)

def give_spoke_length(erdhalf, shr, spokes, crossings, hubtoflange, holerad, radians):
    length = round( math.sqrt ( (hubtoflange**2) + (shr**2) + (erdhalf**2) \
            - (2*shr*erdhalf * math.cos(radians)) - holerad ))
    return length


length = give_spoke_length (erdhalf, shr, spokes, crossings, hubtoflange, holerad, radians)

print'\nSpoke length:', length,'mm\n'

