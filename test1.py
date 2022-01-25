

# source venv/bin/activate  (Start Virtual Enviroment)
# python3 server.py                          (Start Server)
#create and call a function that prints your name.
# execute the script
def print_name():
    print("Antwone")



def list1():
    print("Working with lists (arrays)")

    names = ['Tony', 'Justine']
    # add values to the list

    names.append("Ebony")
    names.append("Antionette")


    # get the values
    print(names[0])
    print(names[3])

    print(names)


    # for loop
    for name in names:
        print(name)



def list2():
    print("-" * 30)

    nums = [123, 456, 123, 3456, 6, 689, 23, 6, 8, 7887,
            123, 46, 3, 89, 12, 9, 9, 565, 8, 33, 1, -200, 23]
# 1 - print  the sum of all numbers
    total = 0
    for n in nums:
            total += n

    print(total)

    # 2 - print numbers lower than 50
    # 2b - count how many numbers are lower than 50
    count = 0
    for num in nums:
        if(num < 50):
            print(num)
            count +=  1

    print(f"There are: {count} nums lower than 50")

    # 3- find the smallest number in the list
    # variable that start with any number from the list (first)
    # forloop
    # compare if the num is lower than your smallest number,
    smallest = nums[0]
    for num in nums:
        if num < smallest:
            smallest = num

    print(f"The smallest in the list is: {smallest}")
   
            



def dict1():
    print("Dictionary tests 1 ----------------")


    me = {
        "name": "Antwone",
        "last": "Adams",
        "age": 38,
        "hobbies": [],
        "address": {
            "street": "Southview",
            "number": "83",
            "city": "Springfield"
        }

    }
    print( me["name"])

    print(me["name"] + " " + me["last"])

    me["age"] = 99

    me["email"] = "alwaysontop@aol.com"

  

    print( me )

    # print the full address in a single line
    address = me["address"]
    print(f"{address['number']} {address['street']} {address['city']}")


print_name()
list1()
list2()

dict1()