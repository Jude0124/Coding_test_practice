def solution(N,stages):
        pos = []

        for i in range(1,N+1):
            stack =0
            entire = len(stages)
            for k in stages:
                if i<k:
                    stack += 1
                elif i>k:
                    entire -=1
            if entire == 0:
                pos.append(0)
            else:    
                pos.append((1-(stack/entire)))
        prop = {k+1:v for k,v in enumerate(pos)}
        
        return sorted(prop , key= lambda x : prop[x] ,reverse = True)