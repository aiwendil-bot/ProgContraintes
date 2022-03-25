def parser(nomfic):

    res = {}
    with open(nomfic, "r") as file:
        
        contenufic = file.readlines()
        
        for i in range(1, int(contenufic[1].split()[0]) + 1):
            res[i] = []
       
       
        for i in range(2,len(contenufic)):
            sommet_succ = contenufic[i].split()
            res[int(sommet_succ[0])].append(int(sommet_succ[1]))
            
        return(res)
