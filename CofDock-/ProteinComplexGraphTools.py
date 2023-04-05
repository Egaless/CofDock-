"""

Transform a complex (ligand + protein).pdb in a graph 
(using BagPype : https://github.com/yalirakilab/BagPype and Pytorc_Geometric) 

"""

def PDB_to_GRAPH(complex_file,complex_name) :
    
    #Create a Graph Folder :
    
    import bagpype
    myprot = bagpype.molecules.Protein()

    parser = bagpype.parsing.PDBParser(complex_file)
    parser.parse(myprot, strip = {'res_name': ['HOH']})
    ggenerator = bagpype.construction.Graph_constructor()
    ggenerator.construct_graph(myprot)
    
    import os 
    os.system("mv atoms.csv "+complex_name+"_atoms.csv")
    os.system("mv bonds.csv "+complex_name+"_bonds.csv" )
    

    return 



"""

Transform a complex (ligand + protein).pdb in a graph then, create a "Reaction graph" 
that is to say : the 'center_elements' and the neighborhood. 
Here, they are 2 center elements max (you can easily modify the program !) 

"""



def Reaction_GRAPH(complex_file, center_elements, complex_name, chain) : 
    PDB_to_GRAPH(complex_file,complex_name)
    import pandas as pd
    
    A = pd.read_csv(complex_name+"_bonds.csv" )
    A = A[ A['atom1_chain'] == chain]
    c_1 = A[ 'atom1_res_name'] == center_elements[0] 
    c_3 = A[ 'atom1_res_name'] == center_elements[1] 
    B = A.loc[ c_1 | c_3]
    
    #Nodes : 
    atom1_id = B["atom1_id"].tolist()
    atom2_id = B[ "atom2_id"].tolist()
    atom_id = atom1_id + atom2_id 
    atom1_name = B[ "atom1_name"].tolist()
    atom2_name = B[ "atom2_name"].tolist()
    atom_name = atom1_name + atom2_name 
    atom1_res_name = B[ "atom1_res_name"].tolist()
    atom2_res_name = B[ "atom2_res_name"].tolist()
    atom_res_name = atom1_res_name + atom2_res_name
    #Edges : 
    bond_type = B["bond_type"].tolist()
    bond_weight = B["bond_weight"].tolist()
    bond_distance = B["bond_distance"].tolist()
    
    #BOND = [ [atom1_id[k], atom2_id[k], bond_type[k] ,  bond_weight[k] , bond_distance[k] ] for k in range(n)  ]
    s =set()
    
    import networkx as nx
    G = nx.Graph()
  
    #CREATE NODES  : 
        
    for i in range(len(atom_name)) :
        
        if not( atom_id[i] in s) :
            G.add_node(atom_id[i], atom_name = atom_name[i], res_name = atom_res_name[i])
            print(int(atom_id[i]), s )
            s.add(int(atom_id[i]))
            
    #CREATE EDGES : 
    for i in range(len(atom1_name)) :
        
        G.add_edge( atom1_id[i], atom2_id[i], bond_type = bond_type[i] , bond_weight = bond_weight[i],
                  bond_distance = bond_distance[i] )
        
        
    import matplotlib.pyplot as plt
    # Dessinez le graph
    nx.draw(G, with_labels=True)
    '''
    node_labels = nx.get_node_attributes(G, 'atom_res_name')
    edge_labels = nx.get_edge_attributes(G, 'bond_type')
 
    nx.draw_networkx_edge_labels(G, nx.spring_layout(G), edge_labels=edge_labels)
    nx.draw_networkx_labels(G,  nx.spring_layout(G),  labels=node_labels)
    '''
    plt.show()
    
    from torch_geometric.utils import from_networkx
    
    Pytorch_Graph =  from_networkx(G)
        
    return G , Pytorch_Graph
