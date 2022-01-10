
lists=["apple","banana","orange","mango"]
for i,li in enumerate(lists):
    if i%2==0:
        # print(i,list)
        print(li)
    i=i+1
items=["apple","banana","orange","mango"]
enumerate_prime=enumerate(items)

print(list(enumerate_prime))

