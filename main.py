# -------------- Input ----------------
# 1)-  number of objects:
# 3)- objects:
"""""
objects:
i.e:
     1 2 3 4 5
     1 2 3 4 5
"""

n = int(input())

objects_a = input().split()
objects_b = input().split()

# int lists:
for i in range(0, n):
    objects_b[i] = int(objects_b[i])
    objects_a[i] = int(objects_a[i])

# printing number of objects:
print(n)


# in case objects collide:
def is_collide(nu, number):
    """Function if collision occurs"""
    nu -= 1
    if nu == 0:
        return False
    else:
        for e in range(0, nu):
            if number == objects_b[e]:
                return True


# some lists to store info:
sum_a_obj = []
sum_b_obj = []
mom = []


# When no collision occurs:
def no_coll():
    """Function if no collision occurs."""
    for num in range(0, n):
        print(objects_a[num], (objects_b[num] * objects_b[num]))


# whole process:
def process(n):
    """ This function runs the all functionality."""
    for num in range(0, n):
        # sum in case they collide:
        sum_a_obj.append(objects_a[num])
        sum_b_obj.append(objects_b[num])
        total = sum(sum_a_obj) + sum(sum_b_obj)

        # Momentum when they collide:
        p = objects_a[num] * objects_b[num]
        mom.append(p)
        momentum = sum(mom)
        # if collision occurs:
        if is_collide(num - 1, objects_a[num]):
            print(total, momentum)
            break
        # if there is no collision:
        elif num == (n - 1):
            no_coll()


# Running the process.
process(n)
