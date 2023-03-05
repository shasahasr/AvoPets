# AvoPets

This project is made for the Stevenson 24 hour Hackathon on 3/4 - 3/5.

The official name is AvoPets (short for Avocado Pets), and our mission statement is to help and teach kids how to stay healthy starting at a young age. It works by incentivizing children to level up their pet and get cooler outfits (may not be implemented yet) through rewards they earn from working out and practicing mindfulness.

It is written in flet which is a combination of Flutter and Python.

This app is not fully built, and many features can be added.
For example, we wanted to connect to either FitBit or Apple Watch APIs to make the tracking for everything much easier.

We used Firebase and Firestore for login credentials + extra variables that change based on account.

Code Written by Aditya Tiwari, Chandu Pedadda, and Shaunak Sahasrabudhe.
Art done by Isamu Mojica.

How to run the program:
MAKE SURE TO DO ALL STEPS IN VSCODE TERMINAL!!

first, verify if you have Python installed, run
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
