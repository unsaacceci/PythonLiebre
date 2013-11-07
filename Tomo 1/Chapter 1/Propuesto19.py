'''
Created on 22/10/2013

@author: CARLOS1
'''
#Write the Scalar Product of 2 vectors in the space
#Read the first vector
X1 = int(raw_input("Enter the first component(X1): "))
Y1 = int(raw_input("Enter the second component(Y1): "))
#Read the second vector
X2 = int(raw_input("Enter the first component(X2): "))
Y2 = int(raw_input("Enter the second component(Y2): "))    
#Calculate the multiplication
ScalarProduct=X1*X2 +Y1*Y2
#Print the product
print "Scalar Product: " + str (ScalarProduct) 