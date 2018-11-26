#Author: Ronald Adomako
#Date: May 26th, 2017
#IBM Cloud Garage Code exercise part 1

import string, re

class SalesTax:
    def __init__(self):
        '''
        Basic sales tax is applicable at a rate of 10% on all goods,
        except books, food, and medical products that are exempt.
        '''
        self.exempt = {
            "books":["book"],
            "food":["chocolate bar"],
            "medical products":[""]}
        return

    def isItemExempt(self,item):
        for key in self.exempt:
            if item in self.exempt[key]:
                return float(1.0)
            else:
                return float(1.1)

    def isItemImported(self,item):
        '''
        Import duty is an additional sales tax applicable on all
        imported goods at a rate of 5%, with no exemptions.
        '''
        if "imported" in item:
            factor = float(1.05)
            return factor 
        else:
            factor = float(1.1)
            return factor

    def readInput(self, output):
        #print output header
        print ("Output " + output)
        myFile = ["space.rtf","pipe.txt","comma.txt"]
        return myFile[int(output)-1]

    def parseInput(self, output):
        fileName = self.readInput(output)
        myFile = open(str(fileName))
        inputFile = myFile.readlines()

        #clean the data
        inputFile = [rawLine.rstrip('\n') for rawLine in inputFile]
        inputFile = inputFile[8:]
        inputFile[0] = inputFile[0][14:]
        
        salesTax = float(0.00)
        total = float(0.00)

        for line in inputFile:
            
            line = re.split(r"\\|{", line)
            line = line[:-1]
            line = line[0]
            if output == "1":#space
                line = line.split(" ")
                print (str(line))
                quantity = line[0]
                price = float(line[-1])
                item = " ".join(line[1:-1])
                
            elif output == "2":#pipe
                line = line.split(" | ")
                quantity = line[1][0]
                price = float(line[-1])
                item = line[0] + line[1][1:]
                
            else: #output 3, comma
                line = line.split(", ")
                quantity = line[0][0]
                price = int(line[1])
                del line[1]
                line[0] = line[0][2:]
                item = " ".join(line.reverse())

            #print each transaction    
            preFactor = self.isItemExempt(price)
            factor = self.isItemImported(item)
            salesPrice = factor * price
            print(str(quantity)+" "+str(item)+": "+str(salesPrice))

        inputFile.close()
        
        salesTax += salesPrice - price
        total += salesPrice
        
        print ("Sales Tax: " + str(salesTax))#print sales tax
        print ("Total: " + str(total))#print total
        
        return
        

def main():
    MyTransaction = SalesTax()
    MyTransaction.parseInput("1")
    return

if __name__ == 'main':
    main()

main()


        
        

    
    
