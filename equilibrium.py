import time
import random
import copy

earth = ["O"]*100





    

def born(born_rate):
    born_rand = random.randint(0,99)/100
    return born_rand < born_rate

def die(dying_rate):
    dying_rand = random.randint(0,99)/100
    return dying_rand < dying_rate
    

def time_shift( planet, born_rate, dying_rate ):
    if planet != []:
        planet_temporary = []
        for creature_pos in range(len(planet)):
            if not die(dying_rate):
                planet_temporary += [ copy.deepcopy(planet[creature_pos]) ,]
        planet = copy.deepcopy(planet_temporary)
    
    if born( born_rate ):
        planet += ["O"]
    return planet




def show(planet,pop_stat):
    print("\n"*100)
    for i in planet:
        print(i)
    print("\n",len(planet),"creatures alives")
    print("\n last 10 mean :",sum(pop_stat)/len(pop_stat))
    






population_stat = [0]
while 1:
    earth = time_shift( planet=earth, born_rate=1, dying_rate=0.1 )

    population_stat += [ len(earth) ,]
    if len(population_stat) > 10:
        del population_stat[0]
    
    show(earth,population_stat)
    time.sleep(0.25)
