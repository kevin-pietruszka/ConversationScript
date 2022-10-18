from reader import *
import excel_reader as er
link = "https://gatech.co1.qualtrics.com/jfe/form/SV_3wMI1pXNJOwLJL8"

ids = {
    "AREA": "QR~QID36~13",
    "Me": "QR~QID45~227",
    "RESIDENT_NAME": "QR~QID2",
    "CRE": "QR~QID39~13",
    "CRE3": "QR~QID94~4",
    "310": "QR~QID80~60",
    "311": "QR~QID80~61",
    "312": "QR~QID80~62",
    "313": "QR~QID80~63",
    "314": "QR~QID80~64",
    "315": "QR~QID80~65",
    "316": "QR~QID80~66",
    "317": "QR~QID80~67",
    "318": "QR~QID80~68",
    "A": "QR~QID91~1",
    "B": "QR~QID91~2",
    "C": "QR~QID91~3",
    "D": "QR~QID91~4",
    "DATE": "QR~QID3",
    "IP": "QID48-1-label",
    "S": "QID41-1-label",
    "DESCRIPTION": "QR~QID49"
}

def main():
    browser.get(link)

    for resident in er.RESDIENTS:
        print(resident)

        wait_click(ids["AREA"])
        change_page(NEXT)

        wait_click(ids["Me"])

        change_page(NEXT)

        wait_keys(ids["RESIDENT_NAME"], resident["name"])
        wait_click(ids["CRE"])

        change_page(NEXT)

        wait_click(ids["CRE3"])

        change_page(NEXT)

        wait_click(ids[resident["apartment/room"]])
        # wait_click(ids[resident["bedroom"]])
        wait_keys(ids["DATE"], resident["date"])
        wait_click(ids["IP"])
        wait_click(ids["S"])

        change_page(NEXT)

        wait_keys(ids["DESCRIPTION"], resident["description"])

        change_page(NEXT)


if __name__ == "__main__":
    main()
    browser.quit()