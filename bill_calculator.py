#!/usr/bin/python2.7
slabs_charges = [(1,100),(2,200),(3,300),(5,400),(7,500)]
your_unit = int(raw_input("Your value: "))
charge = 0

for index,slab in enumerate(slabs_charges):

    if index == 0:
       if your_unit < slabs_charges[index][1]:
          charge = your_unit*slabs_charges[index][0]
          break
       else:
          charge = slabs_charges[index][0]*slabs_charges[index][1]
    elif your_unit <= slabs_charges[index][1]:
       charge = charge + (your_unit - slabs_charges[index-1][1])*slabs_charges[index][0]
       break
    else:
       charge = charge + slabs_charges[index][0]*(slabs_charges[index][1]-slabs_charges[index-1][1])
       if index+1 == len(slabs_charges):
          charge = charge + (your_unit - slabs_charges[index][1])*slabs_charges[index][0]

print charge
