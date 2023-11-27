def roll_call_dwarves(dwarves):
    for i in range(len(dwarves)):
        print(f"{i+1}. {dwarves[i]}")


def summon_captain_planet(planeteers):
    return [planeteer.title() + "!" for planeteer in planeteers]


def long_planeteer_calls(planeteers):
    for call in planeteers:
        if len(call) > 4:
            return True
    return False


def find_the_cheese(strings):
    for string in strings:
        if string == "cheddar" or string == "camembert" or string == "gouda":
            return string
