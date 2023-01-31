import json


def load_data():
    file=open('organizations1.json', 'r')
    data=json.load(file)
    file.close()
    global organizations
    organizations=data['organizations']
    print('data loaded')

def add_organization():
    organization_name = input("Organization name")
    organization_address = input ("Address")
    organization_id = input("id ")

    organization = {
        'name':organization_name,
        'address':organization_address,
        'id':organization_id,
        'contacts':[]
        }
    while(True):
        response=input("add contacts? y/n")
        if response=="y":
            contact_name = input("contact name ")
            contact_position = input ("contact position ")
            contact_id = input("contact id ")

            contact={
                'name':contact_name,
                'position':contact_position,
                'id':contact_id
                }
            organization['contacts'].append(contact)
        elif response=="n":
            break

    organizations.append(organization)

def print_organizations():
    for organization in organizations:
        print(f" Organization\n {organization['name']} ({organization['id']})\n Adrese: {organization['address']}\n Kontaktu skaits: {len(organization['contacts'])}")

def save_data():
    data={
        'organizations':organizations
    }
    print("saving data")
    file=open('organizations1.json', 'w')
    json.dump(data, file, indent=4)
    organizations=data['organizations']
    print("data saved")

def main():
    load_data()
    while (True):
        response=input("(1) Add organziation (2)Print organizations (3)Exit")
        if response=="1":
            add_organization()

        elif response=="2":
            print_organizations()

        elif response=="3":
            save_data()
            print('exit')
            exit()
        #else:
            #print('choose a number between 1 and 3')
            #continue


main()       