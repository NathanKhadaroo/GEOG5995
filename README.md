# GEOG5995

This repository contains the files neccesary to run the Agent Based Model "Night of the Living Dead (Sheep, with landmines)" or NOTLDSWL.

**Introduction:**

This is a simple ABM with three different types of agents (behaviours described below): The Sheep, The Zombie Sheep, and The Holy Landmines of Antioch.

This ABM models the events of a night in which a zombie outbreak occurs in an otherwise peacefull, albeit suspiciously well armed, sheep community.

The length of the night is the number of iterations of the model, following Minecraft rules, the zombies do not survive into the day, thus if the sheep are able to survive until the end of the model they are considered to have won and a victory message is printed(Baaaahhhh! Sheep win!).

However if the zombies are successful in converting all the sheep into zombies before the end of the night, the zombies win and a victory message is printed ("Braiiiiins! Zombies win!").

Finally if all the zombies are killed by the Holy landmines the sheep will be delared winners and a victory message will be printed.

**How to run the model:**

To run this model the files must be in the same directory and the grapics backend for the IPython console should be set to "Automatic".

The model is via the input file (NAME), which prompts the user to enter values for the parameters of the model and then runs the model.


The model takes the following arguments:

* num_of_agents: This indicates how many sheep the model will begin with.

* num_of_iterations: This indicates how many iterations the model should run for (ie: the length of the night).

* neighbourhood = This indication the distance within which sheep will share with other sheep, and zombies will bite sheep.

* num_of_zombsheep = This indicates how many Zombie sheep, the model should begin with.

* num_of_landmines = This indication how many Landmines the model should begin with.

* detection_radius = This indicates the distance within which zombies will cause landmines to detonate.

**The agents**:

* Sheep: 
    These are our basic agents, they interact with the environment, the Zombie Sheep, and each other.
  
    Every update they move, check their environment for food, eat from their environment if food is available, check their neighborhood for other sheep, and share food with them if there any close enough.
  
    They are plotted in white in our animation.
  
* Zombie Sheep:
    Our main antagonists, they interact with Sheep, and with the Holy Landmines of Antioch.
  
    Every update they move, check their neighborhood for sheep, and bites the sheep if there are any. A bitten sheep will become a new zombie.
  
    They are plotted in red in our animation.
  
* The Holy Landmines of Antioch:
  
    Our sheeps only means of defence, they interact only with zombies.
  
    Every update they check their detection radius for any zombies. If zombies are present the landmine explodes and kills all the zombies in the radius, thus remouving them, and itself, from the model.
  
    They are plotted in gold in our animation.
