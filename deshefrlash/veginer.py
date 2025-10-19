#vegener deshefrlash usuli
#19.10.2025
#Komiljon Narzullayev (k0mtrix)

def deshefrla (matn,kalit):
    
    """ deshefrlanadigan matnimiz matn parametriga 
    kalit so'z esa kalit parametriga keladi"""
    
    deshefr_matn=''
    for i in range(len(matn)):
        if('a'<=matn[i]<='z'):
            deshefr_matn += (chr(((ord(matn[i])-97-(ord(kalit[i%len(kalit)])-97))+26)%26+97))
        else:
            deshefr_matn+=matn[i]
    return deshefr_matn

#ishlatish
print(deshefrla('turiz dfgtanma', 'salom'))
    