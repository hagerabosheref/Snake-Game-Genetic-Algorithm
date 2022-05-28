# Hager Mohamed Abdo Abdo Abo Sheref
# Snake game using Genetic algorithm

import turtle, os
from GA import snake_game


# all generation && all fitness
# all generation ----> generations ----> chromosomes ----> genes
all_generation, all_fitness, position_food = snake_game(10,0.9,0.9)

#print(all_generation,all_fitness,position_food)
#print()
#print(all_generation)
#print()
#print(len(all_generation[0][0][0][0][0]))
#print()
#print(all_generation[1][0][1])
#print()
#print(all_generation[0][0][1][0][0])
#print(all_fitness[0][0][1])


#############
#screen
sc=turtle.Screen()
sc.title("Snake Game && Genetic Algorithm")
sc.setup(700,700)
sc.bgcolor("#000428")
sc.bgpic("snakegamepic.png")


#############
# random position for food
xfood = position_food[0]
yfood = position_food[1]

#print(xfood)   
#print(yfood)


#############
# numbers of generation
num_generation = len(all_generation)
#print(num_generation)


def setbackground(): # to set background
    sc.bgcolor("#000428")
    sc.bgpic("1.png")
    
    #############
    #head 
    head=turtle.Turtle()
    sc.addshape(os.path.expanduser("~/Desktop/Snake-Game-by-Genetic-Algorithm/GA project/snake.gif"))
    head.shape(os.path.expanduser("~/Desktop/Snake-Game-by-Genetic-Algorithm/GA project/snake.gif"))
    #head.speed(0) 
    head.pu()

    #############
    #food
    food=turtle.Turtle("circle")
    sc.addshape(os.path.expanduser("~/Desktop/Snake-Game-by-Genetic-Algorithm/GA project/frog.gif"))
    food.shape(os.path.expanduser("~/Desktop/Snake-Game-by-Genetic-Algorithm/GA project/frog.gif"))
    food.pu()
    food.goto(xfood,yfood)
    #food.speed(0) 
    
    #############
    # text 
    text = turtle.Turtle()
    text.hideturtle()
    text.pu()
    text.goto(-260,-260)
    text.color('#B91646')
    
    #############
    #functions
    def up():
        ycurrent=head.ycor()
        head.sety(ycurrent+20)
    def down():
        ycurrent=head.ycor()
        head.sety(ycurrent-20)    
    def right():
        head.fd(20) 
    def left():
        head.bk(20)


    #############
    #update screen
    global num_generation
    #all_generation[numOfGeneration][0][numOfChromosome][numOfGene]
    for num in range(num_generation):
        sc.update()   # update screen to get current x axis and current y axis 
        for chromosome_num in range(8):
            text.clear()
            text.write(f'Generation {num+1}, Chromosome {chromosome_num+1}',font=('Arial', 14 ,'normal'))
            for gene_num in range(4):
                #print(all_generation[num][0][chromosome_num][gene_num])
                step = all_generation[num][0][chromosome_num][gene_num][0]
                if(all_generation[num][0][chromosome_num][gene_num][1] == 'up'):
                    for k in range(step):
                        up()
                elif(all_generation[num][0][chromosome_num][gene_num][1] == 'down'):
                    for k in range(step):
                        down()
                elif(all_generation[num][0][chromosome_num][gene_num][1] == 'left'):
                    for k in range(step):
                        left()    
                elif(all_generation[num][0][chromosome_num][gene_num][1] == 'right'):
                    for k in range(step):
                        right() 
                        
            if(head.xcor()>=280 or head.xcor()<=-280 or head.ycor()>=250 or head.ycor()<=-250):
                head.hideturtle() 
                head.goto(0,0)
                head.showturtle() 
            else:
                head.hideturtle() 
                head.goto(0,0)
                head.showturtle() 

            if (all_fitness[num][0][chromosome_num] <= 60):
                print(all_generation[num][0][chromosome_num])
                sc.clear()
                sc.bgpic("Congratulation.png")
                break; 


turtle.ontimer(setbackground,3000) 
turtle.done()