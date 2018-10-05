def crime():#function for list of unique crime numbers
 fin = open("Crime.csv","r") # reading data from csv
 d = {}
 lst = []
 for line in fin:
    line=line.strip()
    word = line.split(',')
    lst.append(word[-1])  #appending data 
 
 for i in lst:     #Adding keys in dictionary (histogram)
    if(i not in d):  
      d[i]=1          
    else:
      d[i]+=1           
 print ("{:} {:}".format('Key','Label'))# tabular format 
 for k, v in d.items():   # printing tabular format
    print("{:} {:}".format(k, v))
       
 
crime()    # calling function
