from reader import *

link = "https://gatech.co1.qualtrics.com/jfe/form/SV_3wMI1pXNJOwLJL8"

def main():
    
    browser.get(link)
    
    # Get the community names and IDs 
    resident_communities, one = get_options()
    # print(resident_communities)
    wait_click(one)

    change_page(NEXT)

    # Get RA names and IDs
    RAs, one = get_options()
    # print(RAs)
    change_page(NEXT)

    resident_name, one = get_input("resident_name")
    # print(resident_name)
    wait_keys(one, "Brett")

    tmp, one = get_options()
    buildings = {}
    for building, id in tmp.items():
        buildings[building[0:3]] = id

    floors = {}
    rooms = {}

    for building, building_id in buildings.items():

        wait_click(building_id)
        change_page(NEXT)
        # Grab floor ids
        building_floors, _ = get_options()

        for floor_num, floor_id in building_floors.items():

            floors[building + floor_num] = floor_id
            wait_click(floor_id)
            change_page(NEXT)
            # Grab room numbers
            room_numbers, _ = get_options()

            for key, val in room_numbers.items():
                if len(key) > 1:
                    rooms[building + key] = val
            change_page(BACK)
        
        change_page(BACK)
        
    change_page(NEXT)
    change_page(NEXT)

    date, one = get_input("date")
    method_and_topics = get_labels()
    wait_keys(one, "blehh")
    wait_click("QR~QID48~1")
    wait_click("QR~QID41~1")

    change_page(NEXT)

    description, one = get_input()

    ids = dict()

    ids.update(
        resident_communities,
        RAs,
        resident_name,
        buildings,
        floors,
        rooms
    )
    file = open("ids", "wb")
    pickle.dump(ids, file)
    file.close()

if __name__ == "__main__":
    try:
        main()
    finally:
        browser.close()