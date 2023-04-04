import os
import pandas as pd
from biopandas.pdb import PandasPdb

"""
UTILITY FONCTIONS :

1) get_boxes : Get Boxes predicted by P2Rank.
2) get_residues : Find the best residue where a ligand may bind to the protein
3) centered_Box : Find the best box to Dock, near a the Target Residue. 

"""






"""

Get Boxes predicted by P2Rank. (https://github.com/rdk/p2rank ) 

"""

# Return Boxes at
def get_boxes(enzyme_path : str, enzyme_name : str) :  # enzyme_name : The name of the local file, without /home/.... and .pdb
    command = "/home/guillaume/p2rank/prank.sh predict -f " + enzyme_path
    os.system(command)
   
    Path = "/home/guillaume/p2rank/distro/test_output/"+"predict_"+enzyme_name+'/'
    Param = open( Path + "params.txt" , "r")
    Boxes = pd.read_csv( Path + enzyme_name + ".pdb_predictions.csv")
    Residues = pd.read_csv( Path + enzyme_name + ".pdb_residues.csv")
    Residues.rename(columns=lambda x: x.strip(), inplace=True)
    Boxes.rename(columns=lambda x: x.strip(), inplace=True)
    # enlever les espaces dans toutes les colonnes
   
    for df in (Residues, Boxes) :
        for col in df.columns:
            if df[col].dtype == object:
                df[col] = df[col].str.strip()
    return Boxes, Residues , Param




"""
Find the best residue where a ligand may bind to the protein
using P2rank : https://github.com/rdk/p2rank 

"""

def get_Residue( enzyme_path, enzyme_name, RES) :
   
    Boxes, Residues , Param = get_boxes(enzyme_path, enzyme_name)
   
    lys = Residues[ Residues['residue_name'] == RES ]
    binded_lys = lys[ lys["probability"] ==  lys["probability"].max()  ]
   
    print(lys)
   
    return binded_lys




"""



"""

def dist( A, B ):
    return pow( pow(A[0]-B[0],2) + pow(A[1]-B[1],2)  + pow(A[2]-B[2],2) ,1/2)

def centered_Box(enzyme_path,enzyme_name,ligand_path, RES, center_atom_number, output_dir, Size) : 
    Boxes, Residues , Param = get_boxes(enzyme_path, enzyme_name)
   
    lys = Residues[ Residues['residue_name'] == RES ]
    binded_lys = lys[ lys["probability"] ==  lys["probability"].max()  ]
    
    
    #Find the pocket with the best RES
    pocket_N = binded_lys["pocket"].tolist()[0]
    RES_N = binded_lys['residue_label'].tolist()[0]
    pocket = Residues[ Residues[ 'pocket'] == pocket_N]
    Res_List = pocket['residue_label'].tolist()   
    #Find the coordinates of the residues
    Frame = PandasPdb().read_pdb(enzyme_path)
    E = Frame.df["ATOM"]
    chain = binded_lys["chain"].tolist()[0]
    E = E[ E['chain_id'] == chain]
    E = E.loc[ E['residue_number'].isin(Res_List)  ]
    
    X = E['x_coord'].tolist()
    Y = E['y_coord'].tolist()
    Z = E['z_coord'].tolist()
    print(len(X),len(Y),len(Z))        
    Res = E.loc[ E['residue_number'] == RES_N ]
        
    X_RES = Res['x_coord'].tolist()[center_atom_number]
    Y_RES = Res['y_coord'].tolist()[center_atom_number]
    Z_RES = Res['z_coord'].tolist()[center_atom_number]
    print(Res['x_coord'].tolist())   
    N = len(X)
    k = 0 
    while k != N : 
        if dist( [X[k],Y[k],Z[k]] , [X_RES, Y_RES, Z_RES]) > Size : 
            X.pop(k)
            Y.pop(k)
            Z.pop(k)
            N+=-1
        else :
            k+=1
    
    min_X , max_X = min(X) , max(X)
    min_Y , max_Y = min(Y) , max(Y)
    min_Z , max_Z = min(Z) , max(Z)
    
        
    MID = [ (min_X + max_X)/2, (min_Y + max_Y)/2, (min_Z + max_Z)/2]
    box_size = [ max_X - min_X , max_Y - min_Y , max_Z - min_Z ] 
    return box_size ,  MID , chain, RES_N
