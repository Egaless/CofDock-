'''

Sadly, we did not manage to program efficient covalent docking program for our study case.
But, here they are three different working covalent docking functions. 

If you have any ideas the better the functions, we will be glad as students to have your advises. 

'''

from PyPocket import * 

"""

Docking Covalently the cofactor, Using ADFR : https://ccsb.scripps.edu/adfr/tutorial-covalent/
Most efficient. 

"""

def ADFR_covalent_docking(enzyme_path,enzyme_name,ligand_path, RES, output_dir, Size,ADFR_PATH,C_cov,center_atom_number) : 
    box_size , MID, chain, RES_N = centered_Box(enzyme_path, enzyme_name, ligand_path, RES, center_atom_number, output_dir, Size)
    
    print("the chain is : "+chain+" the "+RES+" id is : "+str(RES_N)
              +" write the atom number covalently bounded")
    
    
    os.system(ADFR_PATH+"prepare_receptor -r "+enzyme_path+" -o "+output_dir+enzyme_name+".pdbqt")
    enzyme_prepared = output_dir+enzyme_name+".pdbqt"
    
    
    num_str = input("Enter the list of numbers, separated by spaces: ")
    A_num = [int(x) for x in num_str.split()]
              

    """
    Generate the target file containing the affinity maps.
    
    """

    command_1 = ADFR_PATH+"agfr -r "+enzyme_prepared+" -b user "+str(MID[0])+" "+str(MID[1])+" "+str(MID[2])+" "+str(box_size[0])+" "+str(box_size[1])+" "+str(box_size[2])+" -c "+str(A_num[0])+" "+str(A_num[1])+" -t "+str(A_num[2])+" -x "+chain+":"+RES+str(RES_N)+" -o "+enzyme_name+"_cov_cmdline"
    print(command_1)
    os.system(command_1)
    
    """
    
    Perform the docking : 
    
    """
    
    command_2 = ADFR_PATH+"adfr -l "+ligand_path+" -t "+enzyme_name+"_cov_cmdline.trg --jobName covalent -C "+str(C_cov[0])+" "+str(C_cov[1])+" "+str(C_cov[2])+" --nbRuns 8 --maxEvals 100000 -O --seed 1"
    print(command_2)
    os.system(command_2)
    
    
    return 
    
    
    
"""
Covalent Docking : 
using meeko  : https://github.com/forlilab/Meeko (interface for AutoDockTools)
Work only if the binding atom is Carbone 

"""

def meeeko_covalent(enzyme_path, enzyme_name, ligand_name ,  ligand_RES_path, output_dir,indices, side_chain,  RES) : 

    binded_lys = get_Residue( enzyme_path, enzyme_name, RES)
   
    N_lys = binded_lys["residue_label"].tolist()[0]
   
    command = ' mk_prepare_ligand.py\
    -i '+ligand_RES_path+'\
    --receptor '+enzyme_path+'\
    --rec_residue ":LYS:'+str(N_lys)+'"\
    --tether_smarts "'+side_chain+'"\
    --tether_smarts_indices '+str(indices[0])+' '+str(indices[1])+'\
    -o '+output_dir+"covalent_docked_"+ligand_name+'_'+enzyme_name+'_'+RES+str(N_lys)+'.pdbqt '
    
    os.system (command ) 

    return
 
 
 
 """

Covalent Docking, using
using AutoDock Vina Covalent : https://autodock.scripps.edu/resources/covalent-docking/ 
(tutorial cf readme, when you dowload the package)
Do not work, to many probems with AutoDock Covalent Library :( 

"""

def covalent_docking_v2(enzyme_path, enzyme_name, ligand_name, ligand_path, output_dir, indices, side_chain, chain,  RES, AutoDock_Cov_Path, MGLTOOLS_ROOT) : 
    binded_lys = get_Residue( enzyme_path, enzyme_name, RES)
    N_lys = binded_lys["residue_label"].tolist()[0]
    print(N_lys)
    
    '''
    
    1. Generate the alignment
    --------------------------
    
    '''
    
    c_1 = '  python  '+AutoDock_Cov_Path+'/adcovalent/prepareCovalent.py --ligand '+ligand_path+' \
                  --ligindices '+str(indices[0])+','+str(indices[1])+'\
                  --ligsmart "'+side_chain+'"\
                  --receptor '+enzyme_path+'\
                  --residue '+chain+':'+RES+str(N_lys)+'\
                  --outputfile ligcovalent'+ligand_name+RES+str(N_lys)+'.pdb '
    print(c_1)
    os.system(c_1)
    
    
    '''
    
    2. Generate PDBQT files
    --------------------------
    
    '''
    
    
    
    c_2 = MGLTOOLS_ROOT+'/bin/pythonsh '+MGLTOOLS_ROOT+'/MGLToolsPckgs/AutoDockTools/Utilities24/prepare_receptor4.py -r '+enzyme_path+' -A hydrogens'
    print(c_2)
    os.system(c_2)
    
    
    c_3 =  MGLTOOLS_ROOT+'/bin/pythonsh '+MGLTOOLS_ROOT+'/MGLToolsPckgs/AutoDockTools/Utilities24/prepare_receptor4.py -r ligcovalent'+ligand_name+RES+str(N_lys)+'.pdb '
    print(c_3)
    os.system(c_3)
    
    
    '''
    
    3. Generate flexible/rigid PDBQT files
    ---------------------------------------
    
    '''
    
    c_4= MGLTOOLS_ROOT+'/bin/pythonsh '+MGLTOOLS_ROOT+'/MGLToolsPckgs/AutoDockTools/Utilities24/prepare_flexreceptor4.py -r '+enzyme_name+'.pdbqt -s '+enzyme_name+':'+chain+':'+RES+str(N_lys)
    print(c_4)
    os.system(c_4)
    
    c_5= MGLTOOLS_ROOT+'/bin/pythonsh '+MGLTOOLS_ROOT+'/MGLToolsPckgs/AutoDockTools/Utilities24/prepare_flexreceptor4.py -r '+ligand_name+RES+str(N_lys)+'.pdbqt -s '+ligand_name+RES+str(N_lys)+':'+chain+':'+RES+str(N_lys)
    print(c_5)
    os.system(c_5)
    



    '''
    
    4. Generate GPF and DPF files
    ------------------------------
    
    '''
    '''
    
    c_6 = MGLTOOLS_ROOT+'/bin/pythonsh '+MGLTOOLS_ROOT+'/MGLToolsPckgs/AutoDockTools/Utilities24/prepare_gpf4.py -r 3upo_protein_rigid.pdbqt\
                -x '+ligand_name+RES+str(N_lys)+'.pdbqt\
                -l '+ligand_name+RES+str(N_lys)+'.pdbqt\
                -y -I 20\
                -o '+enzyme_name+'.gpf'
    '''
    
    os.system("touch empty")
    print("touch_empty")
    

    c_7 = MGLTOOLS_ROOT+"/bin/pythonsh "+MGLTOOLS_ROOT+"/MGLToolsPckgs/AutoDockTools/Utilities24/prepare_dpf4.py -r 3upo_protein_rigid.pdbqt\
                -x "+ligand_name+RES+str(N_lys)+".pdbqt\
                -l "+ligand_name+RES+str(N_lys)+".pdbqt\
                -o "+ligand_name+enzyme_name+RES+str(N_lys)+".dpf\
                -p move='empty' "
    print(c_7)
    os.system(c_7)         
   
    
    """

    5. Run AutoGrid and AutoDock
    ------------------------------
    
    """    
    
    '''
    c_8 = " autogrid4 -p 3upo_priotein.gpf -l 3upo_priotein.glg"
    print(c_8)
    os.command(c_8)
    complete if you want to use autogrid
    '''
    
    c_9 = "autodock4 -p "+ligand_name+enzyme_name+RES+str(N_lys)+".dpf -l  "+ligand_name+enzyme_name+RES+str(N_lys)+".dlg"
    print(c_9)
    os.system(c_9)
    
    c_10 =  "grep '^DOCKED' "+ligand_name+enzyme_name+RES+str(N_lys)+".dlg | cut -c9- > "+ligand_name+enzyme_name+RES+str(N_lys)+".pdbqt"
    print(c_10)
    os.system(c_10)
    return 
    
    
   

