name=str(input("Enter the name:-"))
sub1=int(input("Enter the marks of subject 1:-"))
sub2=int(input("Enter the marks of subject 2:-"))
sub3=int(input("Enter the marks of subject 3:-"))
if sub1<33 or sub2<33 or sub3<33:
    print("You are fail")
elif ((sub1+sub2+sub3)/300)*100<40:
    print("You are fail due to total marks")
else:
    print("You are pass")   
