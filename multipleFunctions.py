class functionAssignments():
   
            
    def Eligible():
        gender=input("Your Gender:")
        age=int(input("Your Age:"))
        if((gender=="Male") and (age>=21)):
            msg = "ELIGIBLE"
        elif((gender=="Female") and (age>=18)):
            msg = "ELIGIBLE"
        else:
            msg = "NOT ELIGIBLE"
        return msg
    
      def percentage():
        sub1=int(input("Subject1="))
        sub2=int(input("Subject2="))
        sub3=int(input("Subject3="))
        sub4=int(input("Subject4="))
        sub5=int(input("Subject5="))
        total=sub1+sub2+sub3+sub4+sub5
        print("Total :",total)
        percentage=(total/500)*100
        return percentage
    
    def triangle():
        height=int(input("Height:"))
        breadth=int(input("Breadth:"))
        print("Area formula: (Height*Breadth)/2")
        areaOfTriangle = (height*breadth)/2
        print("Area of Triangle:",areaOfTriangle)
        height1=int(input("Height1:"))
        height2=int(input("Height2:"))
        breadth=int(input("Breadth:"))
        print("Perimeter formula: Height1+Height2+Breadth")
        perimeterOfTriangle = height1+height2+breadth
        #print("Perimeter of Triangle:",perimeterOfTriangle)
        return perimeterOfTriangle
