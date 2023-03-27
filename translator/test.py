#HW1

print("Please select one:")
print(' 1.Check-in')
print(" 2.Check-out")
print(' 3.Print the totals')
option=int(input('option no.:'))
while option<1 or option>3:
    print('Invalid option')
    option=int(input('Enter a valid option:'))
status1= 'Available'
status2= 'Available'
status3= 'Available'
status4= 'Available'
status5= 'Available'
Total_Check_out=0
Total_tax=0
def op1():
  global status1
  global status2
  global status3
  global status4
  global status5
  global Total_Check_out
  global Total_tax
  print(' select one of the available rooms:')
  print('--------------------------------------------------------------')
  print('No. \t Category \t Satuts \t Cost/day')
  print('--------------------------------------------------------------')
  print('1'  '\t  Single  \t',  status1  ,'\t  QR200')
  print('2  \t  Single  \t' ,status2 , '\t  QR200')
  print('3  \t  Double  \t' ,status3 , '\t  QR350')
  print('4  \t  Double  \t' ,status4,  '\t  QR350')
  print('5  \t  Suit  \t' ,status5,  '\t  QR650')
  Choice=int(input('Your choice:'))
  while Choice<1 or Choice>5:
      print(" NOT VALID ROOM NUMBER")
      Choice=int(input('Enter valid room number'))
  if Choice==1 and status1== 'Available':
    status1='Rented'
    print('Room 1 is checked in')
  elif Choice==2 and status2== 'Available':
    status2='Rented'
    print('Room 2 is checked in')
  elif Choice==3 and status3== 'Available':
    status3='Rented'
    print('Room 3 is checked in')
  elif Choice==4 and status4== 'Available':
    status4='Rented'
    print('Room 4 is checked in')
  elif Choice==5 and status5== 'Available':
    status5='Rented'
    print('Room 5 is checked in')
  else:
     print('Room not Available ')
  more_op='y'
  more_op='Y'
  while more_op=='y' or more_op=='Y':
    more_op=input('More operations? [Y/N]')
    if more_op=='n' or more_op=='N':
     break
    while more_op!='y' and more_op!='Y':
       print("invale input")
       more_op=input('More operations? [Y/N]')
    if more_op=='y' or more_op=='Y':
       print("Please select one:")
       print(' 1.Check-in')
       print(" 2.Check-out")
       print(' 3.Print the totals')
       option=int(input('option no.:'))
       if option==1:
        return op1()

    if option==2:
       room_number=int(input("Enter room number:"))
       if  room_number==1 and status1=='Rented':
          status1='Available'
          days=float(input('Enter the number of days:'))
          Check_out1=days*200
          Tax=0.20*Check_out1
          Total=Check_out1+Tax
          Total_Check_out=Total_Check_out+Check_out1
          Total_tax=Total_tax+Tax
          print('Room',room_number,'is checked out')
          print('Rental cost:',' QR',format(Check_out1,'.2f'))
          print('Tax:', 'QR',format(Tax,'.2f'))
          print('------------------')
          print('Total:', 'QR',format(Total,'.2f'))
       elif room_number==2 and status2=='Rented':
           status2='Available'
           days=float(input('Enter the number of days:'))
           Check_out2= days*200
           Tax=0.20*Check_out2
           Total=Check_out2+Tax
           Total_Check_out=Total_Check_out+Check_out2
           Total_tax=Total_tax+Tax
           print('Room',room_number,'is checked out')
           print('Rental cost:',' QR',format(Check_out2,'.2f'))
           print('Tax:', 'QR',format(Tax,'.2f'))
           print('------------------')
           print('Total:', 'QR',format(Total,'.2f'))
       elif room_number==3 and status3=='Rented':
           status3='Available'
           days=float(input('Enter the number of days:'))
           Check_out3=days*350
           Tax=0.20*Check_out3
           Total=Check_out3+Tax
           Total_Check_out=Total_Check_out+Check_out3
           Total_tax=Total_tax+Tax
           print('Room',room_number,'is checked out')
           print('Rental cost:',' QR',format(Check_out3,'.2f'))
           print('Tax:', 'QR',format(Tax,'.2f'))
           print('------------------')
           print('Total:', 'QR',format(Total,'.2f'))
       elif room_number==4 and status4=='Rented':
           status4='Available'
           days=float(input('Enter the number of days:'))
           Check_out4=days*350
           Tax=0.20*Check_out4
           Total=Check_out4+Tax
           Total_Check_out=Total_Check_out+Check_out4
           Total_tax=Total_tax+Tax
           print('Room',room_number,'is checked out')
           print('Rental cost:',' QR',format(Check_out4,'.2f'))
           print('Tax:', 'QR',format(Tax,'.2f'))
           print('------------------')
           print('Total:', 'QR',format(Total,'.2f'))
       elif room_number==5 and status5=='Rented' :
           status5='Available'
           days=float(input('Enter the number of days:'))
           Check_out5=days*650
           Tax=0.20*Check_out5
           Total=Check_out5+Tax
           Total_Check_out=Total_Check_out+Check_out5
           Total_tax=Total_tax+Tax
           print('Room',room_number,'is checked out')
           print('Rental cost:',' QR',format(Check_out5,'.2f'))
           print('Tax:', 'QR',format(Tax,'.2f'))
           print('------------------')
           print('Total:', 'QR',format(Total,'.2f'))
       else: 
         print('This room is not rented')
    if option==3:
          print('Total income:','QR',format(Total_Check_out,'.2f'))
          print('Total tax:','QR',format(Total_tax,'.2f'))
    
if option==1:
  op1()
  
