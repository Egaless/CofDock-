import os 



"""

to_pdbqt() prepare enzyme.pdb or ligand.pdb for docking (transforming in pdbqt, optimised for docking) 
Need to dowload AutoDock Tools 

"""

def to_pdbqt_enzyme(enzyme_path,output_dir,enzyme_name) : 
    os.system("prepare_receptor -r "+enzyme_path+" -o "+output_dir+enzyme_name+".pdbqt")
    enzyme_prepared = output_dir+enzyme_name+".pdbqt"
    return enzyme_prepared 

def to_pdbqt_ligand(output_dir,ligand_name,ligand_path) :
    os.system("mk_prepare_ligand.py -i "+ ligand_path + "  -o " +output_dir+ligand_name+ ".pdbqt" )
    ligand_prepared = output_dir+ligand_name+".pdbqt"
    return  ligand_prepared


"""

Transform ligand.pdb + protein.pdb in a complex.pdb : Usefull for interactions analyses. 

"""

def to_complex(receptor_file,docked_ligand_file,output_file) : 
    import os 
    command =''' awk '/ENDMDL/{exit} {print}' '''+docked_ligand_file+''' > out.pdb && cat '''+receptor_file+''' out.pdb | grep "^ATOM" > '''+output_file+''' && echo "END" >> complexe.pdb '''
    os.system(command)
    return 


"""

Change the name of a residue in a pdb file

"""


def Cofactor_Tag(i, o,path) :
    command =" sed -i 's/{i}/{o}/g' {path} " 
    os.system(command)
    return 

    