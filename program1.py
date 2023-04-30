book1cost=499.00
book2cost=855.00
book3cost=645.00
a=int(input("Enter no.of books: "))
b=int(input("Enter no.of books: "))
c=int(input("Enter no.of books: "))
total=book1cost*a+book2cost*b+book3cost*c
gst=0.12
taxes=total*gst
delivery_charges=250.00
total_invoice=total+taxes+delivery_charges
print(total)
print(taxes)
print(total_invoice)