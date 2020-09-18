try:
    
    from selenium import webdriver
    import time
    # import os

    
    def root():
        print("""
                    _    ____       _     _
    _ __ ___   ___ | |_ / __ \  ___| |__ | |__  _   _
    | '__/ _ \ / _ \| __/ / _` |/ _ \ '_ \| '_ \| | | |
    | | | (_) | (_) | || | (_| |  __/ |_) | |_) | |_| |
    |_|  \___/ \___/ \__\ \__,_|\___|_.__/|_.__/ \__, |
                        \____/                  |___/
    This is the tale of a ghost
    I have been dead since the day
    I came out of the w*mb

    Slittin' the right hand couldn't sleep just like
    Humans I thought as I sat in the dark of my room
    """)
    time.sleep(2)

    
    def logo1():
        print("""
    *************************
    | coded by root@ebby:~# |
    *************************
    |    Seçenekler         |
    *************************
    |    1. Mesaj Yolla     |
    *************************
    |    2. Yok :D (henüz)  |
    *************************
    |    3. Sayfa Yenile    |
    *************************
    |    4. Çıkış           |
    ************************* 
        """)

    
    def logo2():
        print("""
    *************************
    | coded by root@ebby:~# |
    *************************
    |    Seçenekler         |
    *************************
    |    1. Mesaj Yolla     |
    *************************
    |    2. Dosya Okutarak  |
    *************************        
            """)
        

    browser = webdriver.Firefox()
    whatsapp = "https://web.whatsapp.com"
    browser.get(whatsapp)

    print("Lütfen QR Kodu Hazır hale getirip onay veriniz  !")
    onay_2143123 = input("Onay : ")
    
    
    
    
    while True:
        logo1()
        
        __cho__ = int(
            input("Seçenek  : ")
        )

        if __cho__ == 1:
            
            logo2()
            select = int(
                input("Seçenek : ")
            )

            if select == 1:
                isim = input("Telefonunuzda kayıtlı olduğu isim(veya grup adı) : ")
                mesaj = input("Mesajınız : ")
                user = browser.find_element_by_xpath('//span[@title = "{}"]'.format(isim))
                user.click()
                time.sleep(2)
                msg_box = browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
                msg_box.send_keys(mesaj)
                
                buton = browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')        
                time.sleep(1)
                buton.click()
            
            elif select == 2:
                isim = input("Telefonunuzda kayıtlı olduğu isim(veya grup adı) : ")
                dosya = input("Notların adı : ")
                user = browser.find_element_by_xpath('//span[@title = "{}"]'.format(isim))
                user.click()
                time.sleep(2)            
                with open(dosya,"r",encoding="UTF-8") as ebby_note_file:
                    while True:
                        for note in ebby_note_file:
                            
                            msg_box = browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
                            msg_box.send_keys(note)

                    buton = browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')        
                    buton.click()


            else:
                pass
            
        elif __cho__ == 3:
            browser.get(whatsapp)

        elif __cho__ == 4:
            exit()    

        else:
            pass                    
                        
    


except KeyboardInterrupt:
    browser.close()
    exit()
