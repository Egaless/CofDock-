

"""

Test file. 

"""


from CofDock import *
from ProteinComplexGraphTools import * 


enzyme_path = "pdb1u08.pdb"

enzyme_name = "pdb1u08"

ligand_path = "Reactive_PLP.pdbqt"

ligand_name = "Reactive_PLP" 

RES = 'LYS' 

output_dir = ''

Size = 10


center_atom_number = -1


best_pocket_docking(enzyme_path,enzyme_name,ligand_path,ligand_name, RES, output_dir, Size,center_atom_number)