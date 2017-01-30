import re

def open_text():  
      with open('Programming.txt', 'r', encoding = 'utf - 8') as f:  
                text = f.read()
                text = text.lower()  
                arr = text.split()  
                for i, w in enumerate(arr):  
                    arr[i] = arr[i].strip(',.?!-')   
                
      return arr 

def prog():
      arr = open_text() 
      regex = r'\bпрограммир(ова(ть(ся)?|нн(ым|о(е|го|му?))|вш(ая|ую|и(е|й|ми?|х)|е(й|е|му?|го))(ся)?|в|л([иа]?(сь)?)|(ся)?)|у((я(сь)?|ем(о(е|го|й|му?)|ы(е|й|х|ми?)|ая|ую)|ю(щ(ая|ую|и(е|й|х|ми?)|е(го|й|му?))(ся)?))|ют(ся)?|е((шь|т|ем)(ся)?)|ю(сь)?|ете(сь)?))\b'
      arr1 = []
      for i in range(len(arr)):
          m = re.search(regex,arr[i])
          if m != None:
                if arr[i] in arr1:
                      pass
                else:
                      arr1.append(arr[i])
      return ', '.join(map(str,arr1))


print(prog())


    
