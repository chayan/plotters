import os
import csv
import json


def process_area_boundary(area_boundary):
    left, bottom = {"Lat": 10000.0, "Lng": 10000.0}, {"Lat": 10000.0, "Lng": 10000.0}
    right, top = {"Lat": -1.0, "Lng": -1.0}, {"Lat": -1.0, "Lng": -1.0}

    for loc in area_boundary:
        # print(str(loc["Lat"]) + "," + str(loc["Lng"]))
        if loc["Lat"] < bottom["Lat"]:
            bottom = loc
        if loc["Lat"] > top["Lat"]:
            top = loc
        if loc["Lng"] < left["Lng"]:
            left = loc
        if loc["Lng"] > right["Lng"]:
            right = loc

    return str({"Lat": top["Lat"], "Lng": left["Lng"]}), str({"Lat": bottom["Lat"], "Lng": right["Lng"]})


if __name__ == "__main__":
    print(os.getcwd())
    rectangle_areas = []
    with open('areas.csv', newline='') as ac:
        rows = csv.reader(ac, delimiter='\t')
        for row in rows:
            boundary = row[3]
            boundary_json = json.loads(boundary)
            rectangle = process_area_boundary(boundary_json)

            rectangle_areas.append({
                "id": row[0],
                "name": row[2],
                "city": row[1],
                "rectangle_top_left": rectangle[0],
                "rectangle_bottom_right": rectangle[1]
            })

    print(rectangle_areas)

    with open('rectangle_areas.csv', 'w', newline='') as ac:
        writer = csv.writer(ac, delimiter='\t')

        for area in rectangle_areas:
            writer.writerow([area["id"], area["name"], area["city"], area["rectangle_top_left"],
                             area['rectangle_bottom_right']])


