class MysteriousLabrynth:
    def __init__(self):
        #self.n, self.m, self.obstacles, self.teleports = n,m, obstacles, teleports
        return
    
    def mysteriousLabrynth(self, n, m, obstacles, teleports):
        obstacle_set = {(a,b) for a,b in obstacles}
        teleportDict = {(a,b):(c,d) for a,b,c,d in teleports}
        #n is rows
        #m is columns
        #Start
        r,c = 0,0
        visited = set()
        visited.add((r,c)) 
        count = 1 #no. or coordinates (accounts for infinite loop– i.e. inf)
    
        while True:
            #Right
            nr = r
            nc = c+1
            
            #Check bounds
            if (nr, nc) in obstacle_set or nc>=m:
                return -1
                
            #UPDATE COUNT and placement
            count +=1
            r, c = nr, nc
            
            #check exit
            if (r,c) == (n-1, m-1):
                return count
            
            #check teleport
            if (r,c) in teleportDict.keys():
                (r,c) = teleportDict[r,c]
                count += 1
    
                if (r,c) == (n-1, m-1):
                    return count
            #Visitations
            if (r,c) in visited:
                return -2
            visited.add((r,c))
            #nr, nc = r , c