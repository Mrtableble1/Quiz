#f = open("test1.txt","w")

#f.write("Hello world")

#f.close()

f = open("test1.txt","r")

reading_test_1 = f.readline().split(" ")

print(reading_test_1)

f.close()