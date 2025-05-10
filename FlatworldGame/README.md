# Flat World Game

## Manual Flat World
WASD controlled of Blue Blob to reach the Grass lines spread out on a square world before a Red Blob attempts to attack you.

### Run Game from CMD Prompt
`cd FlatworldGame`

`py MannualFlatworld.py`

![Screenshot 2025-05-07 140041](https://github.com/user-attachments/assets/f9159bdf-96b8-49b5-b4fe-161a3e2835f3)

## Fuzzy Flat World
Automated version where we have more Blue Blobs that will attempt to stay away from Red Blobs. Eating Grass will allow them to run faster.
They slow down if they can not get to a food source, making it easier for the Red Blobs to catch them.

### Run Game from CMD Prompt
`cd FlatworldGame`

`py FuzzyFlatworld.py`

![Screenshot 2025-05-07 142436](https://github.com/user-attachments/assets/e17d23c4-f4f0-4e2a-acd8-c3ca0ef44947)

## Subsumption Flat World
Update to Fuzzy Flat World that the behaviors of Wandering, Feeding, and Fleeing are independent from each other.
This also adds the ability for the Blue Blobs to attempt to stay away from the edges for fear that they will get cornered.

Also adds a change in color to inform that they are scared when fleeing to be Orange, which will disable Wandering and Feeding Behaviors until it is no longer scared. 
A change to Cyan Blob means that they are hungry and must find food, which will disable the Wander behavior until fed on Grass.

### Run Game from CMD Prompt
`cd FlatworldGame`

`py SubsumptionFlatworld.py`

![Screenshot 2025-05-07 143644](https://github.com/user-attachments/assets/ce4521ed-3a61-42d6-816a-448a38caac67)

## Insects in Flat World
The creation of Bees who have a Hive (circle) and will attempt to find Flowers (grass from earlier).
There will be different colors to represent the type of bee colonies. The bees back at the Hive will dance 
to inform the others which direction to take to get to the Flowers. There is a rest period while Bee is in the Hive. 
The Bee will get tired of flying around and not be able to find a Flower, which will cause it to need to head back to the 
Hive.

Note that the SPACE bar will allow for a real-time view of the Bees; otherwise, it splits up the speed to go faster in the 
calculations. Note that there is an output for each Generation of Bees. Note that this program is attempting to merge 
generations before for a result that can improve or disadvantage the Bees in how efficient they are.

| Code  | Description |
| ---| --- |
| Ep | Exhaustion Period - time Bee can fly around before heading home. |
| Rp | Rest Period - how long a Bee stays in the Hive. |
| F | Fidget Chance - percentage chance Bee will change direction. |
| T | Concentrate Target - chance Bee will find the Flower target. |
| H | Concentrate Home - chance Bee will turn towards the Hive. |

### Run Game from CMD Prompt
`cd FlatworldGame`

`py Insects.py`

![Screenshot 2025-05-10 161300](https://github.com/user-attachments/assets/9fe3d455-d65a-46c7-9f65-170f382ec8a8)
