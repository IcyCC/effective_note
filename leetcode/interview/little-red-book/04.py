N,T,M = [int(i) for i in input().split()]
monsters = [int(i) for i in input().split()]
if len(monsters) > T:
    print(-1)
else:
    total = sum(monsters)
    min_res =( (sum(monsters) - T) // M  ) + 1
    max_res = max(monsters)
    if (total-M)< T:
        print(-1)
    else:
        monsters.sort(reverse=True)
        has = False
        for h in range(min_res, max_res + 1):
            mp = M
            l = list()      
            t = T
            for hp in monsters:
                if hp < h:
                    l.append(hp)
                    break
                cost = hp // h
                if hp == 0:
                    break
                if(mp - cost) >= 0:
                    mp = mp - cost
                    t = t - cost
                    new_hp = hp - cost * h
                    if new_hp != 0:
                        l.append(new_hp)
                else:
                    t = t - mp
                    if hp-mp != 0:
                        l.append(hp-mp)
                    mp = 0
                    break
            if t <=0:
                break
            l.sort(reverse=True)
            leave = l[mp:]
            t = t - mp
            if sum(leave) <= t:
                print(h)
                has = True
                break
        if not has:
            print(-1)



