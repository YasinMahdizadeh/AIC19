import Model
import time
import queue
from random import randint
chk=0
class AI:

    #def vision():


    def BFS(src,dest):
        mcells=world.map.cells
        result=[]
        visited=[]
        for i in range(31):
            visited.append([])
            for j in range(31):
                visited[i].append(False)

        path=[]
        for i in range(31):
            path.append([])
            for j in range(31):
                path[i].append(1005)

        saf = queue.Queue(maxsize=1000)
        saf.put(src[0],src[1])
        path[src[0],src[1]]=0
        while(saf.empty==False):
            x=saf.get()
            visited[x[0]][x[1]]=True
            if x[0]==dest[0] and x[1]==dest[1]:
                result.append([x[0],x[1]])
                while path[x[0]][x[1]]!=0:
                    if x[0]-1>=0 :
                        if path[x[0]-1][x[1]]+1== path[x[0]][x[1]]:
                            result.append([x[0]-1,x[1]])
                            x=[x[0]-1,x[1]]
                    elif x[1]-1>=0 :
                        if path[x[0]][x[1]-1]+1== path[x[0]][x[1]]:
                            result.append([x[0],x[1]-1])
                            x=[x[0],x[1]-1]
                    elif x[0] + 1 <31 :
                        if path[x[0]+1][x[1]]+1== path[x[0]][x[1]]:
                            result.append([x[0]+1,x[1]])
                            x=[x[0]+1,x[1]]

                    elif x[1] + 1 <31 :
                        if path[x[0]][x[1]+1]+1== path[x[0]][x[1]]:
                            result.append([x[0],x[1]+1])
                            x=[x[0],x[1]+1]

            else:
                if x[0]-1>=0 :
                    if mcells[x[0]-1][x[1]].is_wall==False and visited[x[0]-1][x[1]]==False:
                        path[x[0]-1][x[1]]=path[x[0]][x[1]]+1
                        saf.put([x[0]-1,x[1]])
                if x[1]-1>=0 :
                    if mcells[x[0]][x[1]-1].is_wall==False and visited[x[0]][x[1]-1]==False:
                        path[x[0]][x[1]-1]=path[x[0]][x[1]]+1
                        saf.put([x[0],x[1]-1])
                if x[0] + 1 <31 :
                    if mcells[x[0]+1][x[1]].is_wall==False and visited[x[0]+1][x[1]]==False:
                        path[x[0]+1][x[1]]=path[x[0]][x[1]]+1
                        saf.put([x[0]+1,x[1]])

                if x[1] + 1 <31 :
                    if mcells[x[0]][x[1]+1].is_wall==False and visited[x[0]][x[1]+1]==False:
                        path[x[0]][x[1]+1]=path[x[0]][x[1]]+1
                        saf.put([x[0],x[1]+1])
        if len(result)==0: return False
        else: return result


    def preprocess(self, world):
        print("preprocess")

        # mycells = world.map.cells
        # for i in range(31):
        #     for j in range(31):
        #         if mycells[i][j].wall


    def pick(self, world):
        print("pick")
        global chk
        hero_names = [hero_name for hero_name in Model.HeroName] #Gets Hero Names
        #0:SENTRY    1:BLASTER   2:HEALER     3:GUARDIAN
        if chk==0:
            world.pick_hero(hero_names[0])
        elif chk==1:
            world.pick_hero(hero_names[0])
        elif chk==2:
            world.pick_hero(hero_names[1])
        elif chk==3:
            world.pick_hero(hero_names[2])
        chk+=1





    def move(self, world):
        global result
        print("move")
        #masir=[]
        visited=[]
        for i in range(31):
            visited.append([])
            for j in range(31):
                visited[i].append(False)

        path=[]
        for i in range(31):
            path.append([])
            for j in range(31):
                path[i].append(1005)

        saf = queue.Queue(maxsize=1000)
        chhero=2
                sentryId1=''
                sentryId2=''
                blasterId=''
                healerId=''
                for chhero in world.my_heroes:
                    if chhero.name==Model.HeroName.BLASTER:
                        blasterId=chhero.id
                    elif chhero.name==Model.HeroName.HEALER:
                        healerId=chhero.id
                    elif chhero.name==Model.HeroName.SENTRY and sentryId1=='':
                        sentryId1=chhero.id
                    else:
                        sentryId2=chhero.id


                mcells = world.map.cells
                dirs = [direction for direction in Model.Direction]
                #0:UP    1:DOWN   2:LEFT     3:RIGHT

                for hero in world.my_heroes:
                    if hero.id == blasterId:
                        i = hero.current_cell.row
                        j = hero.current_cell.column
                        path[i][j]=0
                        saf.put([i,j])
                        while(saf.empty==False):
                            x=saf.get()
                            visited[x[0]][x[1]]=True
                            if mcells[x[0],x[1]].is_in_objective_zone==True:
                                result.append([x[0],x[1]])
                                while path[x[0]][x[1]]!=0:
                                    if x[0]-1>=0 :
                                        if path[x[0]-1][x[1]]+1== path[x[0]][x[1]]:
                                            result.append([x[0]-1,x[1]])
                                            x=[x[0]-1,x[1]]
                                    elif x[1]-1>=0 :
                                        if path[x[0]][x[1]-1]+1== path[x[0]][x[1]]:
                                            result.append([x[0],x[1]-1])
                                            x=[x[0],x[1]-1]
                                    elif x[0] + 1 <31 :
                                        if path[x[0]+1][x[1]]+1== path[x[0]][x[1]]:
                                            result.append([x[0]+1,x[1]])
                                            x=[x[0]+1,x[1]]

                                    elif x[1] + 1 <31 :
                                        if path[x[0]][x[1]+1]+1== path[x[0]][x[1]]:
                                            result.append([x[0],x[1]+1])
                                            x=[x[0],x[1]+1]

                            else:
                                if x[0]-1>=0 :
                                    if mcells[x[0]-1][x[1]].is_wall==False and visited[x[0]-1][x[1]]==False:
                                        path[x[0]-1][x[1]]=path[x[0]][x[1]]+1
                                        saf.put([x[0]-1,x[1]])
                                if x[1]-1>=0 :
                                    if mcells[x[0]][x[1]-1].is_wall==False and visited[x[0]][x[1]-1]==False:
                                        path[x[0]][x[1]-1]=path[x[0]][x[1]]+1
                                        saf.put([x[0],x[1]-1])
                                if x[0] + 1 <31 :
                                    if mcells[x[0]+1][x[1]].wall==False and visited[x[0]+1][x[1]]==False:
                                        path[x[0]+1][x[1]]=path[x[0]][x[1]]+1
                                        saf.put([x[0]+1,x[1]])

                                if x[1] + 1 <31 :
                                    if mcells[x[0]][x[1]+1].wall==False and visited[x[0]][x[1]+1]==False:
                                        path[x[0]][x[1]+1]=path[x[0]][x[1]]+1
                                        saf.put([x[0],x[1]+1])
                        #world.move_hero(hero=hero, direction=Model.Direction.DOWN)

            def action(self, world):
                print("action")
                for hero in world.my_heroes:
                    row_num = randint(0, world.map.row_num)
                    col_num = randint(0, world.map.column_num)
                    abilities = hero.abilities
                    world.cast_ability(hero=hero, ability=abilities[randint(0, len(abilities) - 1)],
                                       cell=world.map.get_cell(row_num, col_num))
