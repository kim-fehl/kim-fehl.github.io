import numpy as np

def npy2cube(grid, start, step, cube_f):
    '''
    PARAMETERS:
        grid : numpy array
            3-dimentional array, containing grid data
        start : tuple
            format: (x, y, z), coordinates of cube start point
        step: tuple
            format: (x, y, z), step size on 3 axes 
        cube_f: string
             name of output .cube file
    
    RETURNS:
        void    
    '''
    
    cube_string = ""
    bohr_to_angs = 0.529177210859 #const
    start = map(lambda x: x/bohr_to_angs, start)
    step = map(lambda x: x/bohr_to_angs, step)

    with open(cube_f, "w") as cube_file:
        ###HEADER###
        cube_file.write(" CPMD CUBE FILE.\nOUTER LOOP: X, MIDDLE LOOP: Y, INNER LOOP: Z\n")
        cube_file.write("    1 %f %f %f\n" %(start[0], start[1], start[2]))
        cube_file.write("  %i    %f   0.000000     0.000000\n" %(grid.shape[0], step[0]))
        cube_file.write("  %i    0.000000    %f    0.000000\n" %(grid.shape[1], step[1]))
        cube_file.write("  %i    0.000000    0.000000    %f\n" %(grid.shape[2], step[2]))
        cube_file.write("    1    0.000000    %f %f %f\n" %(start[0], start[1], start[2]))

        ###DATA###
        i = 0
        for x in range(grid.shape[0]):
            for y in range(grid.shape[1]):
                for z in range(grid.shape[2]):
                    if i < 5:
                        cube_file.write("%f " %(float(grid[x, y, z])))
                        i += 1
                    elif i == 5:
                        cube_file.write("%f\n" %(float(grid[x, y, z])))
                        i = 0
    return 0    
    
    
if __name__ == "__main__":
    import argparese
    parser = argparse.ArgumentParser(description = "Convert .npy to .cube file")
    parser.add_argument("-npy", help = "Input .npy filename")
    parser.add_argument("-cube", help = "Output .cube filename")
    parser.add_argument("-start", type = float, nargs = 3, help = "Coordinates of cube start point")
    parser.add_argument("-step", type = float, nargs = 3, help = "Step between nodes in grid on each axe, Angstremes")
    args = parser.parse_args()
    grid = np.load(args.npy)
    npy2grid(grid, args.start, args.step, args.cube)
