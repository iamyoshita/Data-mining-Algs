import math

file = open("decision.txt", "r")
data = []
yes = 0
no = 0
n = 0
for line in file:
    temp = line.split()
    data.append(temp)
    n+=1
    if temp[len(temp)-1] == "Yes":
        yes+=1
    else:
        no+=1

H = -1*(yes/n)*(math.log((yes/n), 2)) + -1*(no/n)*(math.log((no/n), 2))
gains = []

for i in range(len(data[0])-1):

    category = []
    for cat in data:
        category.append(cat[i])
    category = list(set(category))


    sum = 0
    for item in category:
        yes_count = 0
        no_count = 0
        count = 0
        for val in data:
            if val[i] == item:
                count+=1
                if val[len(data[0])-1] == "Yes":
                    yes_count+=1
                else:
                    no_count+=1
        E = 0
        if yes_count != 0:
            E += -1*(yes_count/count)*(math.log2(yes_count/count))
        if no_count != 0:
            E += -1*(no_count/count)*(math.log2(no_count/count))
        sum += E*(count/n)

    gains.append(H-sum)

gains.sort(reverse=True)
print(gains)