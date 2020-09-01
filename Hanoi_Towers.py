# Hanoi Towers
'''
Example of a recursion solution.
We have 3 columns, source, target, and auxiliary.
The source column has disks on it in different sizes, arranged from the
smallest to largest.
Disks can be set on each other only if the smaller disk is on the bigger disk. 
What are the moves that we need to do in order to pass all the disks from the source
to the target column?

In the functions below 'fr' is for 'from', 'to' is for the column that we move the disks to,
and 'spare' for the "mediator" column.
'''

def print_mv(fr, to):
    '''
    Prints instructions for moving the disks correctly
    
    Arguments:
        fr -  the name of the column to move the disks from 
        to -  the name of the column to move the disks to
    '''
    print(f'move from {fr} to {to}')

def hanoi_towers(n, source, target, auxiliary):
    '''
    This function solve the hanoi towers problem using recursion.
    base state - 1 disk, move from source to target.
    recursive step - if more than one disk, move the upper n-1 disks to auxiliary, than
        move the n-th disk to the target column, and than put back the n-1 disk on top of
        the n-th disk at the target column. 
        
    Arguments:
        n - Number of disks
        source - the name of the source column where all disks are at the beginning
        target - the name of the target column where all disks should be at the end
        auxiliary - the name of the auxiliary column
    '''
    if n == 1:
        print_mv(source, target)
    else:
       hanoi_towers(n-1, source, auxiliary, target)
       hanoi_towers(1, source, target, auxiliary)
       hanoi_towers(n-1, auxiliary, target, source)


if __name__ == "__main__":
    n = 5
    hanoi_towers(n, 'source', 'target', 'auxiliary')
    