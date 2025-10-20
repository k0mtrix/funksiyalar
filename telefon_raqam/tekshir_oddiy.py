# Telefon raqamni tekshiruvchi funksiya
# 20/10/2025
# muallif: Komiljon Narzullayev (k0mtrix)

def tel_raqamni_teksher (nomer):
    """Foydalanish: nomer string tipida kiritilishi kerak string tipida malumot qaytariladi"""
    
    kompaniya_kodlari = ["20", "33", "50", "77", "88", "90", "91", "93", "94", "95", "97", "99"]
    if len(nomer)==9:
        if nomer[0:2] in kompaniya_kodlari:
            telefon_raqam=nomer
        else:
            telefon_raqam='Mavjud bo\'lmagan raqam'
    elif len(nomer)==12:
        if nomer[0:3]=='998':
            if nomer[3:5] in kompaniya_kodlari:
                telefon_raqam=nomer
            else:
                telefon_raqam='Mavjud bo\'lmagan raqam'
        else:
            telefon_raqam='Mavjud bo\'lmagan raqam yoki boshqa davlat raqami'
    elif len(nomer)==13:
        if nomer[1:4]=='998':
            if nomer[4:6] in kompaniya_kodlari:
                telefon_raqam=nomer
            else:
                telefon_raqam='Mavjud bo\'lmagan raqam'
        else:
            telefon_raqam='Boshqa davlat raqami'
    else:
         telefon_raqam='Mavjud bo\'lmagan raqam yoki boshqa davlat raqami'
         
    return telefon_raqam

pri=tel_raqamni_teksher("+99778544562")
print(pri)
        