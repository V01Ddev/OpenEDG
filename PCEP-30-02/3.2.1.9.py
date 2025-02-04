"""
while True:
    if input("input: ") == "chupacabra":
        break
    else:
        continue

print("You've successfully left the loop")
"""
## Better implementation

while input("input: ") != "chupacabra":
    continue
print("You've successfully left the loop")
