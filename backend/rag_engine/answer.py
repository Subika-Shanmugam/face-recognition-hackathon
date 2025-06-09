import json
import sys
from datetime import datetime

faces = json.load(open("../face_recognition/faces.json"))

query = sys.argv[1].lower()

if "last" in query:
    last = faces[-1]
    print(f"The last person registered was {last['name']} at {last['time']}.")

elif "how many" in query:
    print(f"There are currently {len(faces)} people registered.")

elif "what time" in query:
    name = query.split("was")[1].split("registered")[0].strip().capitalize()
    for f in faces:
        if f["name"] == name:
            print(f"{name} was registered at {f['time']}")
            break
    else:
        print("Person not found.")

else:
    print("I can't answer that question.")
