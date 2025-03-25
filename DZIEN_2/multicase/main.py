from switchcase import  SwitchCaseMulti

def greet():
    return "Witaj!"

def farewell():
    return "Do widzenia!"

def ask():
    return "Jak zdrowie?"

#Tworzymy instancję klasy SwitchCaseMulti

switch = SwitchCaseMulti()

switch.case(["cześc","hej"],greet)\
    .case(["bye","żegnaj"],farewell)\
    .case("?",ask)\
    .default(lambda :"Nieznana komenda")


print(switch.execute("cześc"))
print(switch.execute("żegnaj"))
print(switch.execute("?"))
print(switch.execute("nnn"))
print(switch.execute("bye"))

print("_"*60)

def multiply_by_two(x):
    return x*2

def square(x):
    return x**2

secondswitch = SwitchCaseMulti()
switch.case(["double","2x"],multiply_by_two)\
    .case(["square","kwadrat"],square)\
    .default(lambda x:x-100)

print(switch.execute("double",6))
print(switch.execute("2x",8))
print(switch.execute("square",4))
print(switch.execute("bla",62))
