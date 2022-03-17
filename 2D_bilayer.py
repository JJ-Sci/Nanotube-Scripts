from ase import Atoms
from ase.visualize import view
from nts.sheet_tools import hexagonal_cell_to_orthorhombic
from nts.nanotube_tools import *
from ase import io
import os
from ase.calculators.vasp import Vasp
from ase.io.vasp import read_vasp
from ase import build

CBN = ['C', 'hBN']
TMD = ['MoS2', 'MoSe2', 'MoTe2', 'WS2', 'WSe2', 'WTe2']
#phase = ['H', 'T']
phase = ['H']

for m in TMD:
  for i in phase:  
      sheet1 = hexagonal_cell_to_orthorhombic(read("{}_{}.json".format(m,i)))
      c1 = sheet1.get_cell()[0][0]
      c2 = sheet1.get_cell()[1][1]
      sheet1.set_cell([(c1, 0, 0), (0, c2, 0), (0, 0, 30)])
      sheet2 = hexagonal_cell_to_orthorhombic(read("{}_{}.json".format(m,i)))
      sheet2.set_cell([(c1, 0, 0), (0, c2, 0), (0, 0, 30)])

      sheet1.center(vacuum=None, axis=(2), about=(18.3))
      sheet1.center(vacuum=None, axis=(0, 1), about=None)
      sheet2.center(vacuum=None, axis=(2), about=(11.7))
      sheet2.center(vacuum=None, axis=(0, 1), about=None)
      multi = sheet1 + sheet2

      multi.write('BL_{}_{}.xyz'.format(m,i))
      io.write('dftb_BL_{}_{}.gen'.format(m,i), multi) 
      io.write('POSCAR_BL_{}_{}.vasp'.format(m,i), multi, 'vasp', direct=True, sort=True, symbol_count=None, vasp5=True, ignore_constraints=False, wrap=True) 


# for hBN or Graphene bilayers
for k in CBN:
    
    if k == [0];
        ene1 = hexagonal_cell_to_orthorhombic(read("hBN.json"))
        ene1.symbols[0] = 'C'
        ene1.symbols[1] = 'C'
        ene1.symbols[2] = 'C'
        ene1.symbols[3] = 'C'
        ene2 = ene1
    else:
        ene1 = hexagonal_cell_to_orthorhombic(read("hBN.json"))
        ene2 = hexagonal_cell_to_orthorhombic(read("hBN.json"))

    c1 = sheet1.get_cell()[0][0]
    c2 = sheet1.get_cell()[1][1]
    ene1.set_cell([(c1, 0, 0), (0, c2, 0), (0, 0, 20)])
    ene2.set_cell([(c1, 0, 0), (0, c2, 0), (0, 0, 20)])

    ene1.center(vacuum=None, axis=(2), about=(11.7))
    ene2.center(vacuum=None, axis=(2), about=(8.3))

    multi = ene1 + ene2

    multi.write('BL_{}_{}.xyz'.format(k))
    io.write('dftb_BL_{}.gen'.format(k), multi) 
    io.write('POSCAR_BL_{}'.format(k), multi, 'vasp', direct=True, sort=True, symbol_count=None, vasp5=True, ignore_constraints=False, wrap=True) 


 
