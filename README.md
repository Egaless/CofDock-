# Enzyme-Ligand Docking

This repository contains a program for docking a ligand on an enzyme with a bound cofactor, as well as utility functions for preparing the enzyme and ligand files for docking, finding the best binding pocket, and creating a reaction graph of the complex. The program uses the GPU-accelerated docking software Gnina for docking, P2Rank for finding the best binding pocket, AutoDock Tools for preparing the enzyme and ligand files, BagPype and PyTorch Geometric for creating the reaction graph.


## OS

- **Only work on `Linux`** 


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
 
 - Docked liagnd File : 
 
 
 
## PyPocket : 

## Requirements : 

- `biopandas`
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

### `to_pdbqt_ligand(output_dir: str, ligand_name: str, ligand_path: str) -> str`

Prepare ligand.pdb file for docking by converting it to pdbqt format with AutoDock Tools.

Arguments:

- `output_dir` (str): Directory to save the output pdbqt file.
- `ligand_name` (str): Name of the ligand file.
- `ligand_path` (str): Path to the ligand pdb file.

Returns:

The path to the prepared pdbqt file.

### `to_complex(receptor_file: str, docked_ligand_file: str, output_file: str) -> None`

Combine receptor and ligand files into a complex pdb file.

Arguments:

- `receptor_file` (str): Path to the receptor pdb file.
- `docked_ligand_file` (str): Path to the docked ligand pdb file.
- `output_file` (str): Path to the output complex pdb file.
