blocks = int(input("Enter the number of blocks: "))

height = 1
while blocks > 0:
    blocks = blocks-height
    height = height+1 if blocks-height>0 else height
    # print(f"at height: {height}, blocks: {blocks}")

print("The height of the pyramid:", height)

