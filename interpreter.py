import string
import ast
import copy

funFlag= False  
intcount = 0
mapcount = 0
funcount= 0
#IF IN HASHMAP, GO BACKWARDS IN HASHMAP TO SEE IF KEY EXISTS

#EDGE CASES
# BINDING
# USE LOOKUP FUNCITON IN CHECKING IF HASHMAP 
def LookUp(hashmap, key):
    for i in range(len(hashmap)-1,-1,-1):
        if key in hashmap[i].keys():
            return hashmap[i][key]
    raise ValueError


def isName(variable):
    if variable in ascii_lowercase or ascii_uppercase:
        return True

    else:
        return False

def interpreter (filein,fileout):
   
    hashmap=[{}]
    fundictionary= {}
    
    listoflists= [[]]


    
    funlist= [[]]
    funcounter=0
    error =":error:"
    stack = []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ,

    with open (filein,'r') as f, open(fileout,'w') as o:
        for line in f:

            if "quit" in line:

                
                for i in listoflists[intcount][::-1]:
                    o.write(str(i)+"\n") 


            if "fun" in line and "funEnd" not in line and len(line.split())==3:
                
                global funFlag
                a,b,c = line.split()
                print(line.split())
                funFlag= True
                fundictionary[b] = c,[]
                if b== c:
                    listoflists[intcount].append(error)

                else:
                    listoflists[intcount].append(":unit:")


                for line in f:
                    line = line.strip("\n")
                    if "funEnd" in line:
                        funFlag= False
                        break
                    fundictionary[b][1].append(line)
                    copy.deepcopy(hashmap)
                             
#2 THINGS: Make a sepeerate function for call helper, seperate function for stack functionary, counter,top,retunr)
            
            elif "call" in line:
                funstack= [[]]

                if len(listoflists[intcount])>1:

                    x= listoflists[intcount].pop()
                    y= listoflists[intcount].pop()
                    fundef= fundictionary[x][1]
                    funpush = 'push {}'.format(y)
                    arg_push = 'push {}'.format(fundictionary[x][0])
                    for i in range(0,len(fundictionary[x][1])):
                        if arg_push == fundictionary[x][1][i]:
                            fundictionary[x][1][i] = funpush
                    

                    for i in fundictionary[x][1]:
                        print(i)
                        if "return" in i:
                            print(funstack)
                            listoflists[intcount].append(funstack[-1][-1])
                        funhelper(i, funstack , hashmap, fundictionary)
                    
                else:
                  listoflists[intcount].append(error)
            

            else:
                
                helper(line,listoflists, hashmap,fundictionary)


            
                         
def funhelper (line,listoflists, hashmap, fundictionary):
        print(line)
        error =":error:"
        global funFlag
        global funcount

        # print("shmap = ", hashmap)    
        # print(hashmap[intcount], intcount)


   

        if "push" in line:
          
            
          try:
            
            if line[5:6]=='"':
                listoflists[funcount].append(line[6:len(line)-2])
                return
            else:
                y,z= line.split()
        
               
                if "-" in z:
                    if str(z[1:]).isdigit():

                        listoflists[funcount].append(z)
                        return
                    else:
                        listoflists[funcount].append(":error:")
                        return
                if z == '-0':
                
                    listoflists[funcount].append('0')
            
                elif str(z).isdigit()==True:
                
                  listoflists[funcount].append(z)
                
                
                else:
                    listoflists[funcount].append(z)
          except ValueError:
            listoflists[funcount].append(error)
                

#POP
    
        
                
    #BOOLEAN & ERROR
        elif ":true:" in line:
            listoflists[funcount].append(":true:")
            
        elif ":false:" in line:
            listoflists[funcount].append(":false:")

        elif ":error:" in line:
            listoflists[funcount].append(":error:")

        elif "pop" in line:
            if len(listoflists[funcount])>0:
                listoflists[funcount].pop()
            elif listoflists==[]:
                listoflists[funcount].append(error)
            else:
                listoflists[funcount].append(error)
      #ADD,SUB,MUL,DIVIDE,REM


#ADD 
        elif "add" in line:
               
            if len(listoflists[funcount])>1:
                
                
                try:
                        x= listoflists[funcount].pop()
                        y= listoflists[funcount].pop()
                        print("ADDING:",x,y)
                        try:
                            x= int(LookUp(hashmap,x))

                        except ValueError:
                            pass
                            
            
                        try:
                            y = int(LookUp(hashmap,y))
                        except ValueError:
                            pass
                        print (int(x)+int(y))
                        listoflists[funcount].append(int(x)+int(y))
                        
                except ValueError or KeyError:
                        listoflists[funcount].append(y)
                        listoflists[funcount].append(x)
                        listoflists[funcount].append(error)
                except TypeError:
                        listoflists[funcount].append(y)
                        listoflists[funcount].append(x)
                        listoflists[funcount].append(error)
            else: 
                listoflists[funcount].append(":error:") 
                          
              
            

#SUB
        elif "sub" in line:                
            if len(listoflists[funcount])>1:
                try:
                    x= listoflists[funcount].pop()
                    y= listoflists[funcount].pop()
            
                    if x in hashmap[funcount]:
                        try:
                            x= int(LookUp(hashmap,x))

                        except ValueError:
                            pass
                        
                    if y in hashmap[funcount]:
                        try:
                            y = int(LookUp(hashmap,y))
                        except ValueError:
                            pass
                    listoflists[funcount].append(int(y)-int(x))
                except ValueError :
                        listoflists[funcount].append(y)
                        listoflists[funcount].append(x)
                        listoflists[funcount].append(error)
              
                except TypeError:
                        listoflists[funcount].append(y)
                        listoflists[funcount].append(x)
                        listoflists[funcount].append(error)
            else:
                listoflists[funcount].append(":error:")    

#MUL
        elif "mul" in line:  
            if len(listoflists[funcount])>1:   

                x= listoflists[funcount].pop()
                y= listoflists[funcount].pop()
            
                try:
                    try:
                        x= int(LookUp(hashmap,x))

                    except ValueError:
                        pass
                            
                        
                    try:
                        y =int(LookUp(hashmap,y))
                    except ValueError:
                        pass
                    listoflists[funcount].append(int(x)*int(y))
                except ValueError or KeyError:
                    listoflists[funcount].append(y)
                    listoflists[funcount].append(x)
                    listoflists[funcount].append(error)
                except TypeError:
                    listoflists[funcount].append(y)
                    listoflists[funcount].append(x)
                    listoflists[funcount].append(error)
            else:
                listoflists[funcount].append(error)


                
 #DIV             
        elif "div" in line:
             
            if len(listoflists[funcount])>1:
                try:
                
                        x= int(listoflists[funcount].pop())
                        y= int(listoflists[funcount].pop())
                
                        try:
                            x= int(LookUp(hashmap,x))

                        except ValueError:
                            pass
                            
                        
                        try:
                            y = int(LookUp(hashmap,y))
                        except ValueError:
                            pass
                        listoflists[funcount].append(int(y/x))
                except TypeError or KeyError:
                        listoflists[funcount].append(y)
                        listoflists[funcount].append(x)
                        listoflists[funcount].append(error)
                except ValueError:
                        listoflists[funcount].append(y)
                        listoflists[funcount].append(x)
                        listoflists[funcount].append(error)
                except ZeroDivisionError:
                        listoflists[funcount].append(y)
                        listoflists[funcount].append(x)
                        listoflists[funcount].append(error)

            else:
                listoflists[funcount].append(error)
                        


#REM
        elif "rem" in line:          
            if len(listoflists[funcount])>1:
                try:
                        x= listoflists[funcount].pop()
                        y= listoflists[funcount].pop()
                
                        try:
                            x= int(LookUp(hashmap,x))

                        except ValueError:
                            pass
                                
                        try:
                            y = int(LookUp(hashmap,y))
                        except ValueError:
                            pass
                        listoflists[funcount].append(int(y)%int(x))
                except ValueError or KeyError:
                        listoflists[funcount].append(y)
                        listoflists[funcount].append(x)
                        listoflists[funcount].append(error)
                except ZeroDivisionError:
                        listoflists[funcount].append(y)
                        listoflists[funcount].append(x)
                        
                        listoflists[funcount].append(error)
            else:
                listoflists[funcount].append(error)




      #NEG
        elif "neg" in line:
            if len(listoflists[funcount])> 0:
                x=listoflists[funcount].pop()
                
                try:

                    x= LookUp(hashmap,x)
                except:
                    pass
                    
                if "-" in x:
                  
                    negx=-int(x)
                    listoflists[funcount].append(negx)
                    return
                elif str(x).isdigit():
                    negx= -int(x)
                    print(negx)
                    listoflists[funcount].append(negx)
                    return
                else:
                    listoflists[funcount].append(x)
                    listoflists[funcount].append(error)
                    return
                
            else:
                 
                    listoflists[funcount].append(x)
                    listoflists[funcount].append(error)
                

#SWAP


    
        elif "swap" in line:
            if len(listoflists[funcount])>1:
                x=listoflists[funcount].pop()
                y=listoflists[funcount].pop()
          
                listoflists[funcount].append(x)
                listoflists[funcount].append(y)

            else:
                listoflists[funcount].append(error)



#################PART 2###################

#AND,OR,NOT
                
        elif "and" in line:
            if len(listoflists[funcount])>1:
                try:  
                    x= listoflists[funcount].pop()
                    y= listoflists[funcount].pop()
                 
                    try:
                        x= LookUp(hashmap,x)

                    except ValueError:
                        pass
                            
                        
                    try:
                        y =LookUp(hashmap,y)
                    except ValueError:
                        pass
                    if x== ":true:" and y== ":true:":
                        z = ":true:"
                        listoflists[funcount].append(z)
                    elif y== ":true:" and x == ":false:":
                        z= ":false:"
                        listoflists[funcount].append(z)
                    elif y== ":false:" and x == ":true:" :
                        z= ":false:"
                        listoflists[funcount].append(z)
                    elif y== ":false:" and x == ":false:":
                        z= ":false:"
                        listoflists[funcount].append(z)
                    else:
                        raise ValueError
                    
                except ValueError or TypeError or IndexError:
                    listoflists[funcount].append(y)
                    listoflists[funcount].append(x)
                    listoflists[funcount].append(error)
            else:
                listoflists[funcount].append(error)


        elif "or" in line:
            if len(listoflists[funcount])>1:
                try:
                    x= listoflists[funcount].pop()
                    y= listoflists[funcount].pop()
                
                    try:
                        x= LookUp(hashmap,x)

                    except ValueError:
                        pass
                            
                        
                    try:
                        y =LookUp(hashmap,y)
                    except ValueError:
                        pass
                    if y== ":true:" and  x== ":true:":
                        z= ":true:"
                        listoflists[funcount].append(z)
                    elif y== ":true:" and x == ":false:":
                        z= ":true:"
                        listoflists[funcount].append(z)
                    elif y == ":false:" and x == ":true:":
                        z= ":true:"
                        listoflists[funcount].append(z)
                    elif y  == ":false:" and x == ":false:":
                        z= ":false:"
                        listoflists[funcount].append(z)
                    else:
                        raise ValueError
              
                except ValueError or TypeError or IndexError:
                    listoflists[funcount].append(y)
                    listoflists[funcount].append(x)
                    listoflists[funcount].append(error)
            else:
                listoflists[funcount].append(error)

        elif "not" in line:
            
            if len(listoflists[funcount])>0:
                try:
                    x= listoflists[funcount].pop()
                
                    
                    try:
                        x= LookUp(hashmap,x)
                    except ValueError:

                        pass
                            
                        
                    
                    if x== ":true:":
                        listoflists[funcount].append(":false:")
                    elif x==":false:":
                        listoflists[funcount].append(":true:")
                    else:
                        raise ValueError
                except ValueError or TypeError:
                    
                    listoflists[funcount].append(x)
                    listoflists[funcount].append(error)
            else:
                listoflists[funcount].append(error)
              


       
#EQUAL

        elif "equal" in line:
            if len(listoflists[funcount])>1:
                try:   
                    x= (listoflists[funcount].pop()) 
                    y= (listoflists[funcount].pop())
                    try:
                        x= LookUp(hashmap,x)

                    except ValueError:
                        pass
                            
                        
                    try:
                        y =LookUp(hashmap,y)
                    except ValueError:
                        pass
                    if int(x)==int(y):
                        listoflists[funcount].append(":true:")
                    elif int(x)!=int(y):
                        listoflists[funcount].append(":false:")
                    else:
                        raise ValueError
                except ValueError or TypeError:
                    listoflists[funcount].append(y)
                    listoflists[funcount].append(x)
                    listoflists[funcount].append(error)

            else:
                listoflists[funcount].append(error)
#LESSTHAN

        elif "lessThan" in line:
            if len(listoflists[funcount])>1:
                try:
                    x= listoflists[funcount].pop()
                    y= listoflists[funcount].pop()
                    try:
                        x= LookUp(hashmap,x)

                    except ValueError:
                        pass
                            
                        
                    try:
                        y =LookUp(hashmap,y)
                    except ValueError:
                        pass
                    if int(y)<int(x):
                        listoflists[funcount].append(":true:")
                    elif int(y)>int(x):
                        listoflists[funcount].append(":false:")
                    else:
                        raise ValueError
                except  ValueError or TypeError:
                    listoflists[funcount].append(y)
                    listoflists[funcount].append(x)
                    listoflists[funcount].append(error)
            else:
               listoflists[funcount].append(error)
#BIND

        elif "bind" in line:
            
            if len(listoflists[funcount])>1:
                  
                   
                 try:
                     
                     x= listoflists[funcount].pop()
                     y= listoflists[funcount].pop()
                     
                     print(x,y)
                     if y[0] in string.ascii_lowercase or y[0] in string.ascii_uppercase:
                          
                          if x == ":error:":
                              raise ValueError
                           
                          print(hashmap)
                          
                          if x in hashmap[funcount]:
                              hashmap[funcount][y]= hashmap[funcount][x]
                          else:
                              hashmap[funcount][y]= x

                          listoflists[funcount].append(":unit:")
                         
                          
                     else:
                          raise ValueError
                          
                 except ValueError or TypeError:
                     listoflists[funcount].append(y)
                     listoflists[funcount].append(x)
                     listoflists[funcount].append(error)
            else:
                listoflists[funcount].append(error)

#IF
                        
        elif "if" in line:
            if len(listoflists[funcount])>2:
                 try:
                     x=listoflists[funcount].pop()
                     y=listoflists[funcount].pop()
                     z=listoflists[funcount].pop()
                     if z==":true:":
                         listoflists[funcount].append(x)
                     elif z==  ":false:":
                         
                         listoflists[funcount].append(y)
                     elif z!= "false" or z!= ":true:":
                         raise ValueError
                     else:
                         raise ValueError
                 except TypeError or ValueError or IndexError:
                    listoflists[funcount].append(y)
                    listoflists[funcount].append(x)
                    listoflists[funcount].append(error)
            else:
                  listoflists[funcount].append(error)
                      



#LET>END
        elif "let" in line:
           
            print(listoflists)
            listoflists.append([])
            hashmap.append({})
            print(hashmap)
            intcount += 1
            
            
        elif "end" in line:
            listoflists[intcount-1].append(listoflists[funcount][-1])
            hashmap[funcount-1].pop()
            intcount -=1
            
      

      

            
           
def helper (line,listoflists, hashmap, fundictionary):

        error =":error:"
        global funFlag
        global intcount


        if "push" in line:
          
            
          try:
            
            if line[5:6]=='"':
                listoflists[intcount].append(line[6:len(line)-2])
                return
            else:
                y,z= line.split()
        
               
                if "-" in z:
                    if str(z[1:]).isdigit():

                        listoflists[intcount].append(z)
                        return
                    else:
                        listoflists[intcount].append(":error:")
                        return
                if z == '-0':
                
                    listoflists[intcount].append('0')
            
                elif str(z).isdigit()==True:
                
                  listoflists[intcount].append(z)
                
            
            
            
                
                else:
                    listoflists[intcount].append(z)
          except ValueError:
            listoflists[intcount].append(error)
                

#POP
    
        
                
    #BOOLEAN & ERROR
        elif ":true:" in line:
            listoflists[intcount].append(":true:")
            
        elif ":false:" in line:
            listoflists[intcount].append(":false:")

        elif ":error:" in line:
            listoflists[intcount].append(":error:")

        elif "pop" in line:
            if len(listoflists[intcount])>0:
                listoflists[intcount].pop()
            elif listoflists==[]:
                listoflists[intcount].append(error)
            else:
                listoflists[intcount].append(error)
      #ADD,SUB,MUL,DIVIDE,REM


#ADD 
        elif "add" in line:
               
            if len(listoflists[intcount])>1:
                
                
                try:
                        x= listoflists[intcount].pop()
                        y= listoflists[intcount].pop()
                        
                        try:
                            x= int(LookUp(hashmap,x))

                            y = int(LookUp(hashmap,y))
                        except ValueError:
                            pass

                        print (int(x)+int(y))
                        listoflists[intcount].append(int(x)+int(y))
                        
                except ValueError or KeyError:
                        listoflists[intcount].append(y)
                        listoflists[intcount].append(x)
                        listoflists[intcount].append(error)
                except TypeError:
                        listoflists[intcount].append(y)
                        listoflists[intcount].append(x)
                        listoflists[intcount].append(error)
            else: 
                listoflists[intcount].append(":error:") 
                          
              
            

#SUB
        elif "sub" in line:                
            if len(listoflists[intcount])>1:
                try:
                    x= listoflists[intcount].pop()
                    y= listoflists[intcount].pop()
            
                    try:
                        x= int(LookUp(hashmap,x))

                    
                        y =int(LookUp(hashmap,y))
                    except ValueError:
                        pass
                    listoflists[intcount].append(int(y)-int(x))
                except ValueError :
                        listoflists[intcount].append(y)
                        listoflists[intcount].append(x)
                        listoflists[intcount].append(error)
              
                except TypeError:
                        listoflists[intcount].append(y)
                        listoflists[intcount].append(x)
                        listoflists[intcount].append(error)
            else:
                listoflists[intcount].append(":error:")    

#MUL
        elif "mul" in line:  
            if len(listoflists[intcount])>1:   

                x= listoflists[intcount].pop()
                y= listoflists[intcount].pop()
            
                try:
                    try:
                        x= int(LookUp(hashmap,x))

                    
                        y =int(LookUp(hashmap,y))
                    except ValueError:
                        pass
                    listoflists[intcount].append(int(x)*int(y))
                except ValueError or KeyError:
                    listoflists[intcount].append(y)
                    listoflists[intcount].append(x)
                    listoflists[intcount].append(error)
                except TypeError:
                    listoflists[intcount].append(y)
                    listoflists[intcount].append(x)
                    listoflists[intcount].append(error)
            else:
                listoflists[intcount].append(error)


                
 #DIV             
        elif "div" in line:
             
            if len(listoflists[intcount])>1:
                try:
                
                        x= int(listoflists[intcount].pop())
                        y= int(listoflists[intcount].pop())
                
                        try:
                            x= int(LookUp(hashmap,x))

                    
                            y =int(LookUp(hashmap,y))
                        except ValueError:
                            pass
                        listoflists[intcount].append(int(y/x))
                except TypeError or KeyError:
                        listoflists[intcount].append(y)
                        listoflists[intcount].append(x)
                        listoflists[intcount].append(error)
                except ValueError:
                        listoflists[intcount].append(y)
                        listoflists[intcount].append(x)
                        listoflists[intcount].append(error)
                except ZeroDivisionError:
                        listoflists[intcount].append(y)
                        listoflists[intcount].append(x)
                        listoflists[intcount].append(error)

            else:
                listoflists[intcount].append(error)
                        


#REM
        elif "rem" in line:          
            if len(listoflists[intcount])>1:
                try:
                        x= listoflists[intcount].pop()
                        y= listoflists[intcount].pop()
                
                        try:
                            x= int(LookUp(hashmap,x))

                    
                            y =int(LookUp(hashmap,y))
                        except ValueError:
                            pass
                        listoflists[intcount].append(int(y)%int(x))
                except ValueError or KeyError:
                        listoflists[intcount].append(y)
                        listoflists[intcount].append(x)
                        listoflists[intcount].append(error)
                except ZeroDivisionError:
                        listoflists[intcount].append(y)
                        listoflists[intcount].append(x)
                        
                        listoflists[intcount].append(error)
            else:
                listoflists[intcount].append(error)




      #NEG
        elif "neg" in line:
            if len(listoflists[intcount])> 0:
                x=listoflists[intcount].pop()
                
                try:

                    x= LookUp(hashmap,x)
                except ValueError:
                    pass
                    
                if "-" in x:
                  
                    negx=-int(x)
                    listoflists[intcount].append(negx)
                    return
                elif str(x).isdigit():
                    negx= -int(x)
                    print(negx)
                    listoflists[intcount].append(negx)
                    return
                else:
                    listoflists[intcount].append(x)
                    listoflists[intcount].append(error)
                    return
                
            else:
                 
                    listoflists[intcount].append(x)
                    listoflists[intcount].append(error)
                

#SWAP


    
        elif "swap" in line:
            if len(listoflists[intcount])>1:
                x=listoflists[intcount].pop()
                y=listoflists[intcount].pop()
          
                listoflists[intcount].append(x)
                listoflists[intcount].append(y)

            else:
                listoflists[intcount].append(error)



#################PART 2###################

#AND,OR,NOT
                
        elif "and" in line:
            if len(listoflists[intcount])>1:
                try:  
                    x= listoflists[intcount].pop()
                    y= listoflists[intcount].pop()
                 
                    try:
                        x= LookUp(hashmap,x)

                    
                        y =LookUp(hashmap,y)
                    except ValueError:
                        pass
                    if x== ":true:" and y== ":true:":
                        z = ":true:"
                        listoflists[intcount].append(z)
                    elif y== ":true:" and x == ":false:":
                        z= ":false:"
                        listoflists[intcount].append(z)
                    elif y== ":false:" and x == ":true:" :
                        z= ":false:"
                        listoflists[intcount].append(z)
                    elif y== ":false:" and x == ":false:":
                        z= ":false:"
                        listoflists[intcount].append(z)
                    else:
                        raise ValueError
                    
                except ValueError or TypeError or IndexError:
                    listoflists[intcount].append(y)
                    listoflists[intcount].append(x)
                    listoflists[intcount].append(error)
            else:
                listoflists[intcount].append(error)


        elif "or" in line:
            if len(listoflists[intcount])>1:
                try:
                    x= listoflists[intcount].pop()
                    y= listoflists[intcount].pop()
                
                    try:
                        x= LookUp(hashmap,x)

                    
                        y =LookUp(hashmap,y)
                    except ValueError:
                        pass
                    if y== ":true:" and  x== ":true:":
                        z= ":true:"
                        listoflists[intcount].append(z)
                    elif y== ":true:" and x == ":false:":
                        z= ":true:"
                        listoflists[intcount].append(z)
                    elif y == ":false:" and x == ":true:":
                        z= ":true:"
                        listoflists[intcount].append(z)
                    elif y  == ":false:" and x == ":false:":
                        z= ":false:"
                        listoflists[intcount].append(z)
                    else:
                        raise ValueError
              
                except ValueError or TypeError or IndexError:
                    listoflists[intcount].append(y)
                    listoflists[intcount].append(x)
                    listoflists[intcount].append(error)
            else:
                listoflists[intcount].append(error)

        elif "not" in line:
            
            if len(listoflists[intcount])>0:
                try:
                    x= listoflists[intcount].pop()
                
                    
                    try:
                        x= LookUp(hashmap,x)
                    except ValueError:

                        pass
                            
                        
                    
                    if x== ":true:":
                        listoflists[intcount].append(":false:")
                    elif x==":false:":
                        listoflists[intcount].append(":true:")
                    else:
                        raise ValueError
                except ValueError or TypeError:
                    
                    listoflists[intcount].append(x)
                    listoflists[intcount].append(error)
            else:
                listoflists[intcount].append(error)
              


       
#EQUAL

        elif "equal" in line:
            if len(listoflists[intcount])>1:
                try:   
                    x= (listoflists[intcount].pop()) 
                    y= (listoflists[intcount].pop())
                    try:
                        x= int(LookUp(hashmap,x))

                    
                        y =int(LookUp(hashmap,y))
                    except ValueError:
                        pass
                    if int(x)==int(y):
                        listoflists[intcount].append(":true:")
                    elif int(x)!=int(y):
                        listoflists[intcount].append(":false:")
                    else:
                        raise ValueError
                except ValueError or TypeError:
                    listoflists[intcount].append(y)
                    listoflists[intcount].append(x)
                    listoflists[intcount].append(error)

            else:
                listoflists[intcount].append(error)
#LESSTHAN

        elif "lessThan" in line:
            if len(listoflists[intcount])>1:
                try:
                    x= listoflists[intcount].pop()
                    y= listoflists[intcount].pop()
                    try:
                        x= int(LookUp(hashmap,x))

                    
                        y =int(LookUp(hashmap,y))
                    except ValueError:
                        pass
                    if int(y)<int(x):
                        listoflists[intcount].append(":true:")
                    elif int(y)>int(x):
                        listoflists[intcount].append(":false:")
                    else:
                        raise ValueError
                except  ValueError or TypeError:
                    listoflists[intcount].append(y)
                    listoflists[intcount].append(x)
                    listoflists[intcount].append(error)
            else:
               listoflists[intcount].append(error)
#BIND

        elif "bind" in line:
            
            if len(listoflists[intcount])>1:
                  
                   
             
                 
                 x= listoflists[intcount].pop()
                 y= listoflists[intcount].pop()
                 try:
                     print(x,y)
                     if y[0] in string.ascii_lowercase or y[0] in string.ascii_uppercase:
                          
                          if x == ":error:":
                              raise ValueError
                           
                          print(hashmap)
                          
                          if x in hashmap[intcount]:
                              print(hashmap[intcount][y])
                              hashmap[intcount][y]= hashmap[intcount][x]
                          else:
                              hashmap[intcount][y]= x
                              listoflists[intcount].append(":unit:")
                          
                          
                     else:
                          raise ValueError
                          
                 except ValueError or TypeError:
                     listoflists[intcount].append(y)
                     listoflists[intcount].append(x)
                     listoflists[intcount].append(error)
            else:
                listoflists[intcount].append(error)

#IF
                 
        elif "if" in line:
            if len(listoflists[intcount])>2:
                 try:
                     x=listoflists[intcount].pop()
                     y=listoflists[intcount].pop()
                     z=listoflists[intcount].pop()
                     if z==":true:":
                         listoflists[intcount].append(x)
                     elif z==  ":false:":
                         
                         listoflists[intcount].append(y)
                     elif z!= "false" or z!= ":true:":
                         raise ValueError
                     else:
                         raise ValueError
                 except TypeError or ValueError or IndexError:
                    listoflists[intcount].append(y)
                    listoflists[intcount].append(x)
                    listoflists[intcount].append(error)
            else:
                  listoflists[intcount].append(error)
                      



#LET>END
        elif "let" in line:
           
            print(listoflists)
            listoflists.append([])
            hashmap.append({})
            print(hashmap)
            intcount += 1
            
            
        elif "end" in line:
            listoflists[intcount-1].append(listoflists[intcount][-1])
            hashmap.pop()
            intcount -=1
            
if __name__=="__main__":
    interpreter("input.txt","output.txt")  

      
