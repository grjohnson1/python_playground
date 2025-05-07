# Flat World Game

## Manual Flat World
WASD controled of Blue Blob with goal of reaching Grass lines spread out on a square world before a Red Blob attempts to attack you.

`cd FlatwroldGame`

`py MannualFlatworld.py`

![Screenshot 2025-05-07 140041](https://github.com/user-attachments/assets/f9159bdf-96b8-49b5-b4fe-161a3e2835f3)

## Fuzzy Flat World
Automatted version where we have more Blue Blobs that will attempt to stay away from Reb Blobs. Eatting Grass will allow them to run faster.
They slow down if they can not get to food source making it easier for the Red Blobs to catch them.

`py FuzzyFlatworld.py`

![Screenshot 2025-05-07 142436](https://github.com/user-attachments/assets/e17d23c4-f4f0-4e2a-acd8-c3ca0ef44947)

## Subsumption Flat World
Update to Fuzzy Flat World that has the behaviors of Wandering, Feeding, and Fleeing be independant from each other.
This also adds the ability for the Blue Blobs to attempt to stay away from the edges for fear that they will get cornered.

Also adds a change in color to inform that they are scared when fleeing to be Orange which will disable Wandering and Feeding Behaviors until it is no longer scared. 
A change to Cyan Blob means that they are hungry and must find food which will disable the Wander behavior until fed on Grass.

`py SubsumptionFlatworld.py`
![Screenshot 2025-05-07 143644](https://github.com/user-attachments/assets/ce4521ed-3a61-42d6-816a-448a38caac67)
