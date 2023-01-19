"""organizations=[]
organizations_a={
    'name':'Tesla Motors',
    'address':'Tesla ave 1, USA', 
    'id':'123456',
    'contacts':
    [
        {
            'name':'Elon',
            'postion':'CEO', 
            'id':1
        },
        {
            'name':'Jennifer',
            'position':'CTO', 
            'id':2
        }
    ]
}

organizations_b={
    'name':'Apple',
    'address':'Apple ave 1, USA', 
    'id':'1234666656',
    'contacts':[
        {
            'name':'John',
            'postion':'CEO', 
            'id':3
        },
        {
            'name':'Anna',
            'position':'CTO', 
            'id':4
        }
    ]
}


organizations.append(organizations_a)
organizations.append(organizations_b)
#print(organizations)

for organization in organizations:
    print(f" Organization\n {organization['name']} ({organization['id']})\n Adrese: {organization['address']}\n Kontaktu skaits: {len(organization['contacts'])}")

"""



organizations=[]
while(True):
    response=input('(1) Add organziation (2)Print organizations (3)Exit ')
    if response == '1':
        organization_name = input("Organization name")
        organization_address = input ("Address")
        organization_id = input("id ")

        organization = {
            'name':organization_name,
            'address':organization_address,
            'id':organization_id,
            'contacts':[]
        }
        organizations.append(organization)

    elif response == '2':
        for organization in organizations:
            print(f" Organization\n {organization['name']} ({organization['id']})\n Adrese: {organization['address']}\n Kontaktu skaits: {len(organization['contacts'])}")
    elif response == '3':
        print("exit")
        exit()
