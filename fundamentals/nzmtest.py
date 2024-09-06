loan=100000

tenure=10

intrest=10

mintrest=(tenure*12)/100

minstall=(tenure*12)

emi=(loan*mintrest*(1+mintrest)**minstall/(1+mintrest)**minstall-1)

print(emi)