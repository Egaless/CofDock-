# Enzyme-Ligand Docking and Graph reprensation 

This repository contains a program for docking a ligand on an enzyme with a bound cofactor, as well as utility functions for preparing the enzyme and ligand files for docking, finding the best binding pocket, and creating a reaction graph of the complex. The program uses the GPU-accelerated docking software Gnina for docking, P2Rank for finding the best binding pocket, AutoDock Tools for preparing the enzyme and ligand files, BagPype and PyTorch Geometric for creating the reaction graph.


## OS

- **Only works on `Linux`** 


## CofDock 

## Requirements 

- `Gnina` : https://github.com/gnina/gnina. **Follow carefully the installation process**. GPU only available for Nvidia
- `PyPockets` (cf it requirements, indicated hereinbelow)

## `best_pocket_docking(enzyme_path: str, enzyme_name: str, ligand_path: str, RES: str, output_dir: str, Size: float, center_atom_number: int) -> None`
Dock a ligand on the best pocket knowing a residue where the cofactor is bound using GPU Gnina.

Arguments:

- `enzyme_path` (str): Path to the enzyme file.
- `enzyme_name` (str): Name of the enzyme file.
- `ligand_path` (str): Path to the ligand file.
- `RES` (str): Residue to bind the ligand.
- `output_dir` (str): Output directory.
- `Size` (float): Box size.
- `center_atom_number` (int): Number of the atom to center the box around.

 Return:
 
 - Docked ligand file.sdf 
 
 
 
## PyPocket : 

## Requirements : 

- `biopandas` : python mudle to read pdb files as frames
- `P2rank` : https://github.com/rdk/p2rank 


## Functions : 


### `get_boxes(enzyme_path: str, enzyme_name: str) -> Tuple[pandas.DataFrame, pandas.DataFrame, pandas.DataFrame]`

Get boxes predicted by P2Rank.

Arguments:

- `enzyme_path` (str): Path to the enzyme file.
- `enzyme_name` (str): Name of the enzyme file.

Returns:

A tuple containing three pandas DataFrames:

- `Boxes`: Boxes predicted by P2Rank.
- `Residues`: Residues "ligandability".
- `Param`: Parameters used for the prediction.

### `get_residue(enzyme_path: str, enzyme_name: str, RES: str) -> pandas.DataFrame`

Find the best residue where a ligand may bind to the protein using P2Rank.

Arguments:

- `enzyme_path` (str): Path to the enzyme file.
- `enzyme_name` (str): Name of the enzyme file.
- `RES` (str): Residue to bind the ligand.

Returns:

A pandas DataFrame containing the residue predicted to bind to the ligand.

### `centered_box(enzyme_path: str, enzyme_name: str, ligand_path: str, RES: str, center_atom_number: int, output_dir: str, size: float) -> Tuple[List[float], List[float], str, int]`

Find the best box to dock, near the target residue.

Arguments:

- `enzyme_path` (str): Path to the enzyme file.
- `enzyme_name` (str): Name of the enzyme file.
- `ligand_path` (str): Path to the ligand file.
- `RES` (str): Residue to bind the ligand.
- `center_atom_number` (int): Number of the atom to center the box around.
- `output_dir` (str): Output directory.
- `size` (float): Box size.

Returns:

A tuple containing four elements:

- `box_size` (List[float]): Box size.
- `MID` (List[float]): Center of the box.
- `chain` (str): Chain of the enzyme.
- `RES_N` (int): Residue number of the target residue.
 
 
 
 
 ## Protein Complex Graph Tools
 
 ## Requirements
 
  -`Bagpype` : https://github.com/yalirakilab/BagPype
  - `networkx` : python module
  - `pytorch-geometrics` : https://pytorch-geometric.readthedocs.io/en/latest/install/installation.html 

### `PDB_to_GRAPH(complex_file: str, complex_name: str) -> None`

Transform a complex PDB file to a graph.

Arguments:

- `complex_file` (str): The path to the complex file in PDB format.
- `complex_name` (str): The name of the complex.

Returns: 

- `BagPype Files` csv with all the interactions between atoms of the complex. for further informations, go see BagPype Github, linked hereinabove.

### `Reaction_GRAPH(complex_file: str, center_elements: List[str], complex_name: str, chain: str) -> Tuple[networkx.Graph, torch_geometric.data.Data]`

Create a reaction graph from a complex PDB file. The reaction graph consists of the center elements and their neighboring atoms interactions (covalent, intermolecular)

Arguments:

- `complex_file` (str): The path to the complex file in PDB format.
- `center_elements` (List[str]): A list of the center elements (residues) for the reaction graph.
- `complex_name` (str): The name of the complex.
- `chain` (str): The chain ID of the protein.

Returns:

A tuple containing:

- `graph` (networkx.Graph): The reaction graph.
- `pytorch_graph` (torch_geometric.data.Data): The PyTorch Geometric representation of the graph.



## PdbTools 
 
 ## Requirements
 
 - `ADT` ( ADT : AutoDockTools is part of MGLtools : https://autodocksuite.scripps.edu/adt/)
 

## Utility Functions

### `to_pdbqt_enzyme(enzyme_path: str, output_dir: str, enzyme_name: str) -> str`

Prepare enzyme.pdb file for docking by converting it to pdbqt format with AutoDock Tools.

Arguments:

- `enzyme_path` (str): Path to the enzyme pdb file.
- `output_dir` (str): Directory to save the output pdbqt file.
- `enzyme_name` (str): Name of the enzyme file.

Returns:

The path to the prepared pdbqt file.
- prepared to dock `receptor.pdbqt`

### `to_pdbqt_ligand(output_dir: str, ligand_name: str, ligand_path: str) -> str`

Prepare ligand.pdb file for docking by converting it to pdbqt format with AutoDock Tools.

Arguments:

- `output_dir` (str): Directory to save the output pdbqt file.
- `ligand_name` (str): Name of the ligand file.
- `ligand_path` (str): Path to the ligand pdb file.

Returns:

- path to the prepared file
- prepared to dock `ligand.pdbqt`

### `to_complex(receptor_file: str, docked_ligand_file: str, output_file: str) -> None`

Combine receptor.pdb and ligand.pdb files into a complex.pdb file. **Very usefull function to use in any case, good to have** 

Arguments:

- `receptor_file` (str): Path to the receptor pdb file.
- `docked_ligand_file` (str): Path to the docked ligand pdb file.
- `output_file` (str): Path to the output complex pdb file.

Returns :

- `complex.pdb` file


## Covalent Docking 
 ## Working in progress ! 
 We have still issues with those program, wich use : ADFR, AutoDock and Meeko to perform the covalent Docking. All the code is share, function are working but not give perfect result. 

# Tips : 
Use CofDock for covalent docking. Dock the indermediate product to the reactive residue, you will hve a strong interactions bewteen them in the interactions graph. Go see the toturial.
