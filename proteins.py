#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun May  6 21:27:27 2018

@author: Tom
"""
# HO HO HO!

import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate


# Input a pdb file, e.g. '1mp6.pdb', output a list of lines containing atom information.
def atom_list(file):
    atoms=[]
    for line in open(file):
        list=line.split()
        id = list[0]
        if id == 'ATOM':
            atoms.append(list)
    return atoms

# Input a list of atom information, output list of float coordinates of CA atoms.
def carbon_list(atoms):
    carbons=[]        
    for atom in atoms:
        type = atom[2]
        if type == 'CA':
            carbons.append([float(atom[6]),float(atom[7]),float(atom[8])])
    return carbons

# Input a list of atom information, output [x, y , z] coordinates of CA atoms.
def carbon_coords(atoms):
    x = []
    y = []
    z = []
    for atom in atoms:
        type = atom[2]
        if type == 'CA':
            x.append(float(atom[6]))
            y.append(float(atom[7]))
            z.append(float(atom[8]))
    return [x, y, z]

# Input pdb file, output [x, y ,z] coordinates of CA atoms.
def pdb2coords(file):
    atoms = atom_list(file)
    [x,y,z] = carbon_coords(atoms)
    return [x, y, z]

# Input pdb file, produces plot of protein backbone.
def plot_backbone(file):
    mpl.rcParams['legend.fontsize'] = 10
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    [x,y,z]=pdb2coords(file)
    ax.plot(x, y, z, label='Protein Backbone')
    ax.legend()
    plt.show()

# plot smoothed backbone --- DOESN'T WORK!!!
def smooth_backbone(file):
    [x,y,z]=pdb2coords(file)
    tck, u = interpolate.splprep([x,y,z], s=2)
    u_fine = np.linspace(0,1,200)
    [x_int, y_int, z_int] = interpolate.splev(u_fine, tck)
    mpl.rcParams['legend.fontsize'] = 10
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.plot(x_int, y_int, z_int, label='Protein Backbone')
    ax.legend()
    plt.show()



    
