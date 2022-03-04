print("hello world")
tal1 = 12
tal2 = 10.5
text1 = "Hej"
print(tal1*tal2)

tal3 = int(input("skriv första talet: "))
tal4 = int(input("skriv andra talet: "))
print(tal3*tal4)

mittTal = int(input("Skriv in ett heltal: "))
if mittTal>100:
    print("talet är större än 100")
elif mittTal<0:
    print("talet är negativt")
else:
    print("talet ligger mellan 0 och 100")

myArray=[10, 34.5,"hej", 18]
myArray.append(39)
print(myArray)

for i in range(7):
    print(i)
for i in range(4,9):
    print(i)

for i in range(len(myArray)):
    print(myArray[i])