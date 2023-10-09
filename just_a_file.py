import random
rooms = {
    "room1": {
        "hint": "This is Room 1. There is a door to your north.",
        "sunduk": False
    },
    "room2": {
        "hint": "This is Room 2. There is a door east and south.",
        "sunduk": False
    },
    "room3": {
        "hint": "This is Room 3. There is a door west and south.",
        "sunduk": False
    },
    "room4": {
        "hint": "This is Room 4. There is a door west.",
        "sunduk": False
    },
    "room5": {
        "hint": "This is Room 5. There is a door south.",
        "sunduk": False
    },
}
chest=random.randrange(1,len(rooms))
chest=rooms[f"room{chest}"]
chest['sunduk']=True
def rooms_list():
    for room in rooms.values():
        print(f'Hint: {room["hint"]}, SundukZdes?: {room["sunduk"]}')
# rooms_list()
print("We have 5 rooms. There is a Sunduk Sokrovish in one of them. Find it!")
def game():
    while True:
        x=input("Guess the room number: ")
        while not x.isdigit():
            x=input(f"You must enter a number between 1 and {len(rooms)}\nGuess the room number: ")
        if (rooms[f'room{x}'])['sunduk']==False:
            print((rooms[f'room{x}'])['hint'])
        else: 
            print('You won!');break