from math import floor,ceil
from collections import Counter

def fun(ABn,ls):
    hero_power = ABn[0]
    hero_health =  ABn[1]
    n= ABn[2]
    ind=0
    last_index= n-1
    for val in ls:
        i,j=val
        monster_power = i
        monster_health = j
        # while(monster_health>0 and hero_health>0):
        #     monster_health = monster_health - hero_power
        #     hero_health = hero_health - monster_power
        no_of_fight_by_monster = ceil(monster_health/hero_power)
        no_fight_by_hero = ceil(hero_health/monster_power)
        mx_no_of_fight=min(no_fight_by_hero,no_of_fight_by_monster)

        monster_health = monster_health - hero_power*mx_no_of_fight
        hero_health = hero_health - monster_power*mx_no_of_fight
        # print(hero_health,monster_health)
        if(ind==last_index and hero_health<=0):
            if(monster_health<=0):
                print('yes')
                return
            if(monster_health>0):
                print('no')
                return
            
        if(ind!=last_index and hero_health<=0):
            print('no')
            return
        ind+=1
    print('yes')


T = int(input())
for i in range(T):
    abn = list( map (int, input().split()) )
    a = list( map (int, input().split()) )
    b = list (map (int, input().split()) )
    fun(abn,sorted(list(zip(a,b))))
