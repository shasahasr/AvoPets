# AvoPets

## This project is made for the Stevenson 24 hour Hackathon on 3/4 - 3/5.

Code Written by Aditya Tiwari, Chandu Pedadda, and Shaunak Sahasrabudhe.
Art done by Isamu Hamai.

The official name is AvoPets (short for Avocado Pets), and our mission statement is to help and teach kids how to stay healthy starting at a young age. It works by incentivizing children to level up their pet and compete with their friends through rewards they earn from working out and practicing mindfulness.

# FULL APP SYNOPSIS
The app is made to help people to have more fun in a well lifestype, where the people can gain xp for their pets from workouts and mindful practices. These xp gains also increase the strength, health, and endurance of the pet, as well as the level. The higher the level of the pet, the harder bosses they have to fight in a turn-by-turn combat system. After leveling enough, you can add friends off of their username on the app and compare your levels to get ultimate bragging rights. The different workouts all are used to incentivise a varied lifestyle in the many facuets of wellness. In the end, we find that not many apps at all can replace this since many can't properly incentivise wellness, especially in our target audience of children. We fill a massive gap in the market and make it much more important for the people of this new age to use.

This app is not fully built, and many features can be added. For example, we wanted to connect to either FitBit or Apple Watch APIs to make the tracking for everything much easier. Additionally, we could add multiplayer gamemodes as previously planned to further incentivise the importance of working out.

We used (Firebase)[https://console.firebase.google.com/u/0/project/avopets-abb9b] and Firestore for login credentials + extra variables that change based on account. It is written in flet which is a combination of Flutter and Python.

## How to run the program:
MAKE SURE TO DO ALL STEPS IN VSCODE TERMINAL!!

First, verify if you have Python installed, run
```
python -V
```

next, you have to activate the environment on python. navigate to ./avopets/Scripts, and run the activating command
```
# MacOS
source activate

# Windows
activate
```

cd back into the AvoPets regular directory by typing ```cd ..``` twice
install the following packages by running
```
#Do on both Windows and MacOS
python -m pip install flet
# For Arm64 it is arch --arm64 brew install ... and Intel is just brew install 
arch --arm64 brew install firebase-admin
#Windows
pip install firebase-admin
```

now, navigate back to the ./src file, and run the main file
```
python main.py
```

bam boom bop



we are all freshman lolol
