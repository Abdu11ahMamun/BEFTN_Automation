class Locators():
        #Login page objects
        username_xpath = '//*[@id="j_idt13"]/table[2]/tbody/tr[2]/td/input'
        password_xpath = '//*[@id="j_idt13:masked-password"]' 
        login_button_xpath = '//*[@id="j_idt13"]/table[2]/tfoot/tr/td/input'

        #Home page objects
        logout_xpath = '//*[@id="topControl"]/table/tbody/tr/td[5]/div/a'
        outward_xpath = '//*[@id="navForm:m_menu_2:hdr"]/table/tbody/tr/td[2]'
        new_transaction_link= 'http://192.168.1.154:8080/beftn/faces/outbound/txn/cieppdedit.xhtml'

        #Outward transaction
        currency_id = 'txnEntryForm:eftCurrency'
        




        