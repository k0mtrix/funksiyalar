#vegener shefrlash usuli
#19.10.2025
#Komiljon Narzullayev (k0mtrix)

def shefrla (matn,kalit):
    
    """ Shefrlanadigan matnimiz matn parametriga 
    kalit so'z esa kalit parametriga keladi"""
    
    shefr_matn=''
    for i in range(len(matn)):
        if('a'<=matn[i]<='z'):
            shefr_matn += (chr((ord(matn[i])-97+ord(kalit[i%len(kalit)])-97)%26+97))
        else:
            shefr_matn+=matn[i]
    return shefr_matn

#ishlatish
print(shefrla('bugun dushanba', 'salom'))
    