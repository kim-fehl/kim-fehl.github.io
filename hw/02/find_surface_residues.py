import pymol
from pymol import cmd, stored
import random

# https://pymolwiki.org/index.php/FindSurfaceResidues
def findSurfaceResidues(objSel="(all)", cutoff=2.5, doShow=False, verbose=False):
    tmpObj="__tmp"
    cmd.create( tmpObj, objSel + " and polymer");
    if verbose!=False:
        print("WARNING: I'm setting dot_solvent.  You may not care for this.")
    cmd.set("dot_solvent");
    cmd.get_area(selection=tmpObj, load_b=1)
    cmd.remove( tmpObj + " and b < " + str(cutoff) )

    stored.tmp_dict = {}
    cmd.iterate(tmpObj, "stored.tmp_dict[(chain,resv)]=1")
    exposed = stored.tmp_dict.keys()
    exposed.sort()

    randstr = str(random.randint(0,10000))
    selName = "exposed_atm_" + randstr
    if verbose!=False:
        print("Exposed residues are selected in: " + selName)
    cmd.select(selName, objSel + " in " + tmpObj ) 
    selNameRes = "exposed_res_" + randstr
    cmd.select(selNameRes, "byres " + selName )

    if doShow!=False:
        cmd.show_as("spheres", objSel + " and poly")
        cmd.color("white", objSel)
        cmd.color("red", selName)
    cmd.delete(tmpObj)
    return exposed


cmd.extend("findSurfaceResidues", findSurfaceResidues)