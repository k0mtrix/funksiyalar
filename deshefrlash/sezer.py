#Sezer deshefrlash funksiyasi.
#19.10.2025
#Komiljon Narzullayev (k0mtrix)

def deshefrla(matn,kalit):
    """ Deshefrlanadigan matnimiz matn parametriga 
    kalit esa kalit parametriga keladi"""
    
    deshefr_matn=''
    for belgi in matn.lower():
        if ('a'<=belgi<='z'):
            deshefr_matn+=(chr((ord(belgi) - 97 - kalit) % 26 + 97))
        else:
            deshefr_matn+=(belgi)
    return(deshefr_matn) 

#Ishlatish 'Komiljon' deshefrlanadigan matn, 5 esa kalit.
# deshefr=deshefrla(matn='Komiljon', kalit=5)
# print(deshefr)