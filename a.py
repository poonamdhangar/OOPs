# lists=["apple","banana","orange","mango"]
lists=("apple","banana","orange","mango")
# lists={"apple","banana","orange","mango"}
i=1
print(type(lists))
for list in lists:
    if i%2!=0:
    # if i%2==0:
        print(list)
    i=i+1

    