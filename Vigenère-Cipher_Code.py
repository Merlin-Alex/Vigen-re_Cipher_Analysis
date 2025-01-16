#Vigenère Cipher Analysis
file = open("cipher.txt", 'r') 
#reading the cipher text
vicipher= file.read() 
# key lengths initialised in list
k =[4, 5, 6] 
Most_likely = []
def cipher(N):
    def matrix_form(): #function to convert string to matrix form
        mat = [[] for _ in  range(N)]
        for i , char in enumerate(vicipher):
             mat[i% N].append(char)  
        return [''. join(col) for col in mat]  
    
    def IC_Averages(): #function to calculate the average Ic value
         colum= [col for col in matrix_form()]
         ic =0
         for i in range(N): 
             total_letters = len(colum[i])
             freqs = [colum[i].count(letter) for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ']
             ic += (sum(f * (f - 1) for f in freqs) / (total_letters * (total_letters - 1)))  # ic formula applied 
         ics = ic/N
         return(f"{ics:.4f}")
    Avg_ICs =IC_Averages() 
    return Avg_ICs  

def possible_keylength(): #function to print out the most likely key length
     for y in k: 
         IC_english = 0.0686
         Most_like= cipher(y)
         print ("Avergae IC of the key length",y,":",Most_like)        
         Most_likely.append([Most_like,f"key Length:{y}"])
     print ("And the IC_English is :",IC_english )         
     print("Thus, The key is most likely of",":",max(Most_likely))
possible_keylength()  