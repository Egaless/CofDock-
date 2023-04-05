from Pypocket import *

""" 

Docking A ligand on the best pocket knowing a RES where the cofactor is binded
using GPU Gnina

"""

def best_pocket_docking(enzyme_path,enzyme_name,ligand_path, RES, output_dir, Size,center_atom_number) : 
    
        box_size , MID, chain, RES_N = centered_Box(enzyme_path, enzyme_name, ligand_path, RES,center_atom_number ,output_dir, Size)
    
        command = ( "gnina -r "+ enzyme_path +" -l "+ligand_path + " --center_x "+
          str(MID[0])+" --center_y "+str(MID[1])+" --center_z "+str(MID[2])+  
           " --size_x "+str(box_size[0])+" --size_y "+str(box_size[1])+" --size_z "+str(box_size[2])+" --flexdist_ligand "+ligand_path+" --flexdist 0 -o "+output_dir+chain+"S.pdb")
        print(command)
        os.system(command)        
        return 
    
