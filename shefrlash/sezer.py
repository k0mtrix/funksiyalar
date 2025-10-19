#Sezer shefrlash funksiyasi.
#19.10.2025
#Komiljon Narzullayev (k0mtrix)

def shefrla(matn,kalit):
    """ Shefrlanadigan matnimiz matn parametriga 
    kalit esa kalit parametriga keladi"""
    
    shefr_matn=''
    for belgi in matn.lower():
        if ('a'<=belgi<='z'):
            shefr_matn+=(chr((ord(belgi) - 97 + kalit) % 26 + 97))
        else:
            shefr_matn+=(belgi)
    return(shefr_matn) 

#Ishlatish 'Komiljon' shefrlanadigan matn, 5 esa kalit.
# shefr=shefrla(matn='Komiljon', kalit=5)
# print(shefr)