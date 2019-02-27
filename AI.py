import Model
import time
import math
from random import randint
hero_nammes = []

class AI:

    def preprocess(self, world):
        print("____PREPROCESS____")
        obj = world.map.objective_zone
        obj_cen_x = 0
        obj_cen_y = 0
        for cell in obj:
            obj_cen_x = obj_cen_x + cell.row
            obj_cen_y = obj_cen_y + cell.column
        obj_cen_x = obj_cen_x / len(obj)
        obj_cen_y = obj_cen_y / len(obj)
        print("--> X Center =", obj_cen_x)
        print("--> Y Center =", obj_cen_y)

    def pick(self, world):
        print("____PICK____")

        hero_names = [hero_name for hero_name in Model.HeroName]
        #0:SENTRY    1:BLASTER   2:HEALER     3:GUARDIAN

        world.pick_hero(hero_names[1])

        '''if( len(hero_nammes) < 3 ):
            world.pick_hero(hero_names[1])
            hero_nammes.append(hero_names[0])
        else:
            world.pick_hero(hero_names[2])
            hero_nammes.append(hero_names[2])'''


    def move(self, world):
        print("_____MOVE_____")
        dirs = [direction for direction in Model.Direction]
        #0:UP    1:DOWN   2:LEFT     3:RIGHT
        obj = world.map.objective_zone
        #########################

        for hero in world.my_heroes:
            hero_current_cell= hero.current_cell
            #random_index = randint( 0 , len(obj) - 1 )
            move_sequence = []
            move_sequence = world.get_path_move_directions(start_cell= hero_current_cell, end_cell= attack_points[math.ceil(hero.id/2)])

            #print(hero.current_cell.is_in_vision)
            if ( len(move_sequence) != 0 and hero.current_cell.is_in_objective_zone == False ):
                world.move_hero(hero=hero, direction=move_sequence[0])

    def action(self, world):
        print("____ACTION_____")
        '''for hero in world.my_heroes:
            row_num = randint(0, world.map.row_num)
            col_num = randint(0, world.map.column_num)
            abilities = hero.abilities
            world.cast_ability(hero=hero, ability=abilities[randint(0, len(abilities) - 1)],
                               cell=world.map.get_cell(row_num, col_num))'''
        enemies_in_vision = []
        vision = []
        worldmap = world.map.cells
        ability_names = [ ability_name for ability_name in Model.AbilityName ]


        for hero in world.my_heroes:
            abilities = hero.abilities
            '''for row in worldmap:
                for cell in row:
                    #print("--- Current cell is" , cell )
                    if world.is_in_vision( start_cell= hero.current_cell , end_cell= cell ):
                        vision.append(cell)
            world.cast_ability( hero = hero, ability= abilities[0], cell = vision[randint(0,len(vision)-1)] )'''

            for Dhero in world.opp_heroes:
                if world.is_in_vision(start_cell=hero.current_cell,end_cell = Dhero.current_cell):
                    world.cast_ability( hero = hero, ability= abilities[0], cell = Dhero.current_cell )
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
