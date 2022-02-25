#use bigjson library to handle large set of data
import bigjson
#define a function which calculate BMI for the data in input.json and save the output in the required format in output.json                
def Calculator(data):
    #basic predefined values used to calculate BMI
    BMI_Range={0:[0,18.4],1:[18.5,24.9],2:[25,29.9],3:[30,34.9],4:[35,39.9],5:[40,100]}
    Health_Risk=["Malnutrition risk","Low risk","Enhanced risk","Medium risk","High risk","Very high risk"]
    BMI_Category=["Underweight","Normal weight","Overweight","Moderately obese","Severely obese","Very severely obese"]
    #intitalize variable to calculate total overweight person
    total_overweighted_person = 0
    with open('output.json', 'w') as outfile:
        
        for Item in params:
            temp = {}
            BMI=round(Item["WeightKg"]/(Item["HeightCm"]/100)**2,2)
            temp['Gender'] = Item["Gender"]
            temp["HeightCm"] = Item["HeightCm"] 
            temp["WeightKg"] = Item["WeightKg"]
            temp["BMI"] = BMI
            for key in BMI_Range:
                if key==5:
                    temp["Health_Risk"] = Health_Risk[key]
                    temp["BMI_Category"] = BMI_Category[key]
                    outfile.write(str(temp)+"\n")
                    break
                if BMI >= BMI_Range[key][0] and BMI < BMI_Range[key+1][0]:
                    
                    temp["Health_Risk"] = Health_Risk[key]
                    temp["BMI_Category"] = BMI_Category[key]
                    outfile.write(str(temp)+"\n")
                    if BMI_Category[key] == "Overweight":
                        total_overweighted_person+=1
                    break
                    
    return total_overweighted_person
#main function call    
if __name__=='__main__':
    with open('input.json', 'rb') as data:
        params = bigjson.load(data)
    total_overweighted_person=Calculator(params)
    #print total number of over weight person
    print(f"Total Number of Overweighted person {total_overweighted_person}")