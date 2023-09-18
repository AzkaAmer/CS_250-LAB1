#Task 1.
rivers=[{'name': 'Nile','length':4157}, 

        {'name': 'Yangtze','length':3434}, 

        {'name': 'Murray-Darling','length':2310}, 

        {'name': 'Volga','length':2290}, 

        {'name': 'Mississipi','length':2540}, 

        {'name': 'Amazon','length':3915}] 

for i in range(len(rivers)): 
    print(rivers[i]['name']) 
    print('Length of',rivers[i]['name'],'river in kilometers is ',rivers[i]['length']*1.6)
m=0 
for j in range(len(rivers)): 
    m+=rivers[j]['length'] 
print(m) 
for x in range(len(rivers)): 
    if (rivers[x]['name'][0])=='M': 
        print(rivers[x]['name']) 
        
#Task 2.
List1=[1.0, 2.0, 4.5] 
List2=[2.0, 4.5, 5.0] 
def overlap(List1, List2): 
    z=[] 
    for l in List1: 
        if l in List2: 
            z.append(l) 
    print(z) 

def join(List1, List2): 
    result=[] 
    for i in List1: 
        if i not in result: 
            result.append(i) 
    for i in List2: 
        if i not in result: 
            result.append(i) 
    print(result) 
    
#Task 3.
spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]
    
def get_names(spicy_foods):
    m=[]
    for i in spicy_foods:
        m+=[i['name']]
    return m

def get_spiciest_foods(spicy_foods):
    m=[]
    for i in spicy_foods:
        if i['heat_level']>=5:
            m+=[i]
    print(m)    
    return

def print_spicy_foods(spicy_foods):
    for i in spicy_foods:
        n=i['name']
        c=i['cuisine']
        h=i['heat_level']
        print(n,'(',c,')','Heat Level:',('🌶')*h)

def get_spicy_food_by_cuisine(spicy_foods,cuisine):
    for i in spicy_foods:
        c=i['cuisine']
        if c==cuisine:
            print(i)

def print_spiciest_foods(spicy_foods):
    for i in spicy_foods:
        if i['heat_level']>5:
            n=i['name']
            c=i['cuisine']
            h=i['heat_level']
            print(n,'(',c,')','Heat Level:',('🌶')*h)

def get_average_heat_level(spicy_foods):
    m=0
    for i in spicy_foods:
        m+=i['heat_level']
    print('Average heat level of all spicy foods is',m/len(spicy_foods))
    
def create_spicy_food(spicy_foods, spicy_food):
   print(spicy_foods+[spicy_food])

spicy_food= {
 'name': 'Griot',
 'cuisine': 'Haitian',
 'heat_level': 10,
 }
cuisine='Thai'

def main():
    print("Calling all the functions in main")
    print(get_names(spicy_foods))
    get_spiciest_foods(spicy_foods)
    print_spicy_foods(spicy_foods)
    get_spicy_food_by_cuisine(spicy_foods, cuisine)
    print_spiciest_foods(spicy_foods)
    get_average_heat_level(spicy_foods)
    create_spicy_food(spicy_foods, spicy_food)


if __name__=="__main__":
    main()