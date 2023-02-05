

def structure_function(x1, x2, x3, x4):
    '''
    This formula unfortunately is not very dynamic.
    
    However, once you edit for the specific structure 
    function you are working with, a great way to verify
    block diagrams are drawn correctly.
    '''
    return 1-(1-x1)*(1-x2*(1-(1-x3)*(1-x4)))
