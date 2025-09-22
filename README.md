# Battleship 
The classic game that now has been made into a terminal python game, that runs of Code institutes mock terminal on Heroku. 

Players can take on the challange and see if they are better then the computer. The battleships occupies one square on the board randomly every game. 


# How to play! 
Anyone can play and its fairly easy aswell. 
Every turn you are allowed to make one guess to score a hit but first before you start the game you need to enter your name. 
This will generate two random boards. 
You as the player will be able to see where your own ships are on your side of the board, because they will have the `@` as an indication.
But you wont be able to see the computers ships. 

If you make a guess and unfortunatly Miss then the `X` will appear to show where you missed. But if you hit then you will get `*` sign as a indication. 
The winner is the one that sinks all of their opponent's battleship first. 


## Features 
* Random board generation
  * Ships are randomly placed on both the player and computers boards
  * The player can't see where the computer's ships are

+ Computer is your opponent
+ Current score will be taking with to the next round if you continue to play

<img width="280" height="390" alt="image" src="https://github.com/user-attachments/assets/b0bc873e-ec6f-472a-97d9-abf2054e8199" />
<img width="280" height="390" alt="image" src="https://github.com/user-attachments/assets/63f871e7-0ac4-44ca-8ab4-92253253c948" />
<img width="280" height="390" alt="image" src="https://github.com/user-attachments/assets/bccd7a0e-f254-48bb-8754-b3c7c2e0fb4e" />


+ Input validation and error-controll
    + You wont be able to guess the same thing twice
    + The coordinates must be inside of the desegnated area of the grid
    + You must enter numbers
 

##Bugs 
###solved 
+ had the missfortune of having to deal with TypeErrors. Easy to solve but small misses like that should not be made so often.
+ Had issues with the Boards because i wanted one to show the players name after you've typed it in. When I thought I solved it just showed that i had dupplicated the problem instead but in the end by retracing my steps and by making the code simpler then i initially did

##Remaining Bugs
+ No bugs remaining


## Future Features 
+ Allow player to select difficulty level of the computer
+ Allow players to choose the amount of ships and the boards size
+ Be able to move and put the ships down on the map however the play feels like

## Testing 
I have done test on the PP3 by doing the following things:
 + Put invalid inputs just to see if there needed to get fixed or if it was working as intended


##Deployment 
I used Code institute's mock tyerminal when i deployed it on Heroku 
