colorBands=["brown","red","orange","yellow","green","blue","violet","grey","white"]
firstBand=colorBands.index((input("Enter the first color band \n")))
secondBand=colorBands.index((input("Enter the second color band \n")))
thirdBand=colorBands.index((input("Enter the third color band \n")))

resistanceOhms=int(((firstBand*10)+(secondBand))*(10**(thirdBand)))
resistanceKOhms=resistanceOhms/1000
print("\nThe Resistance Value is\n")
print(f"{resistanceOhms}Ω  and {resistanceKOhms}kΩ")