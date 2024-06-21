x = input("Item: ").lower().strip()
fruits =  {"apple": "130","banana": "110","avocado": "50","kiwifruit": "90","pear":"100","sweet cherries": "100"}
if x in fruits:
    print("Calories: ",fruits[x])