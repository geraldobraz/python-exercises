class Human:
    print("Human")
class Man(Human):
    print("Man")
class Woman(Human):
    print("Woman")

def God():
    # lst = []
    Adam = Man()
    Eve = Woman()
    return [Adam,Eve]

