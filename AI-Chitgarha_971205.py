import Model
import time
#import num
from random import randint
hero_nammes = []



class AI:



    #def vision():
    '''vision = [[[ 0 for i in range(31)] for j in range(31)] for k in range(31)]
    objective_vision = matrix = [[[ 0 for i in range(31)] for j in range(31)]''' #for k in range(31)]

    def preprocess(self, world):
        print("____PREPROCESS____")
        objective = world.map.objective_zone
        worldmap = world.map_cells
        print("Worldmap =",worldmap)
        print(world.heroes)
        #print(objective)
        print("TYPE= " , type(objective), len(objective))
        #print(type(vision))
        '''print("preprocess")
        for i in range(0,31):
            for j in range (0,31):
                for k in range(i+1,31):
                    for l in range(j+1,31):
                        print( world.is_in_vision(row,(k,l)))'''


    def pick(self, world):
        print("____PICK____")

        hero_names = [hero_name for hero_name in Model.HeroName] #Gets Hero Names
        #if ( world.my_heroes.count(""))

        if( len(hero_nammes) < 3 ):
            world.pick_hero(hero_names[0])
            hero_nammes.append(hero_names[0])
        else:
            world.pick_hero(hero_names[2])
            hero_nammes.append(hero_names[2])

        #0:SENTRY    1:BLASTER   2:HEALER     3:GUARDIAN
        #hero = hero_names[randint(0,len(hero_names)-1)]
        #if


        #s = str(world.my_heroes.id) + ' ' + str(world.my_heroes.name)
        #print(s)

    def move(self, world):
        print("_____MOVE_____")
        dirs = [direction for direction in Model.Direction]
        #0:UP    1:DOWN   2:LEFT     3:RIGHT

        for hero in world.my_heroes:
            #if ( )
            hero_current_cell= hero.current_cell
            obj = world.map.objective_zone
            random_index = randint( 0 , len(obj) - 1 )
            move_sequence = []
            print("01=", hero_current_cell)
            print("02=", obj[random_index])

            move_sequence = world.get_path_move_directions(start_cell= hero_current_cell, end_cell= obj[random_index])

            #print(hero.current_cell.is_in_vision)
            if ( len(move_sequence) != 0 and hero.current_cell.is_in_objective_zone==False ):
                world.move_hero(hero=hero, direction=move_sequence[0])

    def action(self, world):
        print("____ACTION_____")
        vision = []
        print("map cells= " , world.map_cells )
        for hero in world.my_heroes:
            for cell in world.map.cells:
                if world.is_in_vision( hero.current_cell , cell ):
                    vision.append(cell)
        print vision

        # for hero in world.my_heroes:
        #     # row_num = randint(0, world.map.row_num)
        #     # col_num = randint(0, world.map.column_num)
        #     # abilities = hero.abilities
        #
        #     world.cast_ability(hero=hero, ability=abilities[randint(0, len(abilities) - 1)],
        #
                        # cell=world.map.get_cell(row_num, col_num))

        '''for Dhero in world.opp_heroes:
            for Khero in world.my_heroes:
                if (Dhero.current_cell.row!=-1):
                    if Khero.name==Model.HeroName.SENTRY:
                        ch=world.get_ability_targets(ability_name=Model.AbilityName.SENTRY_RAY,start_cell=Khero.current_cell,target_cell=Dhero.current_cell)
                        print (ch,'\n\n\n')
                        if (len(ch)!=0):
                            world.cast_ability(hero=Khero,ability_name=Model.AbilityName.SENTRY_RAY,cell=Dhero.current_cell)'''
