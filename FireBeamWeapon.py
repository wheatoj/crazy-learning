import Tkinter as Tk

from random import randint


class Curry:
    def __init__(self, f, arg):
        self.f = f
        self.arg = arg

    def __call__(self):
        self.f(self.arg)


def fire(arg):
    arg = arg+1
    print 'Firing', beamType, '#%s !' % arg
    # Get the target range
    tar_range = targetRange.get()
    max_range = len(fc[bw[beamType][0]])
    # Check if target range is within weapon limits
    hitCalc = 0
    if tar_range == 0:
        msg = "Cannot fire within same hex!"
    elif tar_range > max_range:
        msg = "Target is out of range!"
    elif tar_range in range(0, max_range + 1):
        hitCalc = fc[bw[beamType][0]][tar_range - 1]
        msg = "In Range"
    else:
        msg = "Something went wrong..."
    # Show the result
    msg_result["text"] = msg
    toHitRoll["text"] = hitCalc

    # Random roll to see if firing attempt resulted in successful hit
    rollFire = randint(1, 10)
    numberRolled["text"] = rollFire
    if rollFire > hitCalc:
        hit_result["text"] = "Sorry, you missed."
    elif rollFire <= hitCalc:
        hit_result["text"] = "It's a hit!"
    else:
        hit_result["text"] = "something went wrong..."


# Sample from Beam Weapon dictionaries
fc = {'R': [10, 10, 9, 9, 8, 8, 7, 7, 6, 6, 5, 5, 4, 3, 2, 1]}
bw = {'FH-5': ['R', 4, range(0), range(1, 9), range(9, 17)]}

# Enter Beam Weapon Data
beamType = 'FH-5'
weaponMaxPwr = bw[beamType][1]
beamWepCount = input("How many beam weapons: ")

# Create root window
root = Tk.Tk()
root.title("Fire Weapons")

# Tk variables
targetRange = Tk.IntVar()
# weaponPower = Tk.IntVar()

# Top row labels in GUI
targetRangeLabel = Tk.Label(root, text="Target Range")
targetRangeLabel.grid(row=1, column=1)
targetRangeScale = Tk.Scale(root, from_=0, to=24, orient='horizontal', length=300, variable=targetRange)
targetRangeScale.grid(row=1, column=2)
beamWepLabel = Tk.Label(root, text="Beam Type")
beamWepLabel.grid(row=2, column=1)
beamChartLabel = Tk.Label(root, text=("Firing chart---{} Max Range---{}".format(bw[beamType][0],
                                                                                len(fc[bw[beamType][0]]))))
beamChartLabel.grid(row=2, column=2)
firedLabel = Tk.Label(root, text="Weapon Fired?")
firedLabel.grid(row=2, column=3)

# Dynamically create widgets
FireButtons = []
PowerScales = []
weaponFiredLabel = []
for ii in range(0, beamWepCount):
    FireButtons.append(Tk.Button(root, text=beamType, command=Curry(fire, ii)))
    FireButtons[-1].grid(row=ii + 3, column=1)
    PowerScales.append(Tk.Scale(root, from_=0, to=weaponMaxPwr, orient="horizontal", length=200))
    PowerScales[-1].grid(row=ii + 3, column=2)
    weaponFiredLabel.append(Tk.Label(root, text="?"))
    weaponFiredLabel[-1].grid(row=ii + 3, column=3)

# Check the To-Hit Roll and number rolled
toHitLabel = Tk.Label(root, text="To Hit:")
toHitLabel.grid(row=beamWepCount + 4, column=1)
toHitRoll = Tk.Label(root, text="?")
toHitRoll.grid(row=beamWepCount + 4, column=2)
rolledLabel = Tk.Label(root, text="Number rolled:")
rolledLabel.grid(row=beamWepCount + 5, column=1)
numberRolled = Tk.Label(root, text="?")
numberRolled.grid(row=beamWepCount + 5, column=2)

# Print message to user for target range issues
msg_result = Tk.Label(root, text="Good Luck!", bg="white")
msg_result.grid(row=beamWepCount + 6, column=2)

# Print message to user to indicate hit or miss (want message to be visible for only a short time)
hitResultLabel = Tk.Label(root, text="Hit Result:")
hitResultLabel.grid(row=beamWepCount + 7, column=1)
hit_result = Tk.Label(root, text="?")
hit_result.grid(row=beamWepCount + 7, column=2)

# Print message to user to indicate damage result from a hit
damageResultLabel = Tk.Label(root, text="Damage Result:")
damageResultLabel.grid(row=beamWepCount + 8, column=1)
dmg_result = Tk.Label(root, text="?")
dmg_result.grid(row=beamWepCount + 8, column=2)

print(FireButtons)

root.mainloop()
