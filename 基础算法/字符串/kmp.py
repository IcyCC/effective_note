
def get_next(s2):
    if len(s2) == 1: 
        return [-1]
    next_arr = [0 for i in s2]
    next_arr[0] = -1
    i = 2
    cn = 0
    while  i <len(next_arr):
        if(s2[i - 1] == s2[cn]):
            cn = cn + 1
            s2[i]  = cn
            i = i + 1
        elif cn > 0:
            cn = next_arr[cn]
        else:
            next_arr[i] = 0
            i = i + 1
    return next_arr
        

def get_match(s1, s2):
    if ( (not s1) or (not s2)):
        return -1
    next_arr = get_next(s2)
    s1_idx = 0
    s2_idx = 0
    while s1_idx < len(s1) and s2_idx < len(s2):
        if s1[s1_idx ] == s2[s2_idx] :
            s1_idx = s1_idx + 1
            s2_idx = s2_idx + 1
        elif next_arr[s2_idx] == -1:
            s1_idx = s1_idx + 1
        else:
            s2_idx = next_arr[s2_idx]
    
    return s1_idx - s2_idx if s2_idx == len(s2) else -1



    
