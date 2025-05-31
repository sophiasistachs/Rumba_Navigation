# 

# Licensed under 3-Clause BSD license available in the License file. Copyright (c) 2021-2022 iRobot Corporation. All rights reserved. 

# Kaitlyn, Sophia, and Theo 

 

from irobot_edu_sdk.backend.bluetooth import Bluetooth 

from irobot_edu_sdk.robots import event, hand_over, Color, Robot, Root, Create3 

from irobot_edu_sdk.music import Note 

 

robot = Create3(Bluetooth()) 

@event(robot.when_play) 

async def play(robot): 

    await robot.set_lights_on_rgb(254, 153, 0) #makes it orange 

    path_clear = True #this path is clear, meaning it can move forward. 

    obs = "clear" #obstacle, this will determine which direction the obsticle is (right, left) 

    wall = "no" #this will determine which side the wall is. 

    speed = 10 

    await robot.move(15) 

    while True: 

        sensors = (await robot.get_ir_proximity()).sensors 

        print(sensors) 

        #avoids obsticles 

        if(obs == "right"): 

            await robot.turn_left(90) 

            obs ="clear" 

        elif (obs == "left"): 

            await robot.turn_right(90) 

            obs ="clear" 

        elif (obs == "both"): 

            if(sensors[0]>sensors[6]): 

                await robot.turn_right(90) 

            elif(sensors[6]>sensors[0]): 

                await robot.turn_left(90) 

            obs = "clear" 

        elif (obs == "front"): 

            if(sensors[0]>sensors[6]): 

                await robot.turn_right(90) 

            elif(sensors[6]>sensors[0]): 

                await robot.turn_left(90) 

         

 

        if(wall == "no"): 

            if(sensors[0]>sensors[6] and sensors[0]>50): #checks if the wall is on the left 

                wall="left" 

            elif(sensors[6]>sensors[0] and sensors[6]>50): #checks if wall is on the right 

                wall="right" 

            elif(sensors[0]<10 and sensors[6]<10): 

                wall="no" 

        if(path_clear == True): 

            await robot.move(speed) 

        #checks front 

        sensors = (await robot.get_ir_proximity()).sensors 

        if(sensors[3]<300): # 

            obs = "clear" #no obs. 

            path_clear = True #there is no obstacle.  

        else: 

            obs = "front" #obsticle detected on the front side 

            path_clear = False #there is obstacle. Gotta rotate 

 

        #checks sides 

        if((sensors[2]>sensors[4] and sensors[1]>sensors[5]) and (sensors[2]>sensors[3] and sensors[3]>200)): #checks left side 

            obs = "left" #obsticle detected on the left side 

            path_clear = False #there is obstacle. Gotta rotate 

        elif((sensors[4]>sensors[2] and sensors[5]>sensors[1]) and (sensors[4]>sensors[3] and sensors[3]>200)): # checks right side 

            obs = "right" #obsticle detected on the right side 

            path_clear = False  

 

        #checks if both sides have an obsticle. 

        if(sensors[1]>200 and sensors[5]>200): 

            obs = "both" 

            path_clear=False 

 

        if(obs != "clear"):  # prints if an obstacle is detected 

            print(sensors, "Obsticle detected:", obs, " side/s") 

 

        sensors = (await robot.get_ir_proximity()).sensors 

        print(sensors) 

        if(wall == "left" and sensors[0]<60): # checks if wall left. 

            await robot.move(20) 

            await robot.turn_left(90) 

            wall = "no" 

        elif(wall == "right" and sensors[6]<60): 

            await robot.move(20) 

            await robot.turn_right(90) 

            wall = "no" 

robot.play() 