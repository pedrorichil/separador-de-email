import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)


print(Fore.GREEN + '\n\n SEPARADOR DE EMAIL POR PROVEDOR BY: Zekry \n\n')
                                                                    
                                                            
try:
    with open('db.txt', 'r', encoding="utf8") as file: 
        for line in file.readlines():
            try:
                if '@ig.com.br' in str(line.lower()): 
                    with open('IG.txt', 'a', encoding="utf8") as file2: 
                        file2.write(str(line))
                        print(f"+1   ->   {str(line)}")
                        pass
                            
                if '@gmail.com' in str(line.lower()): 
                    with open('GMAIL.txt', 'a', encoding="utf8") as file2: 
                        file2.write(str(line))
                        print(f"+1   ->   {str(line)}")
                        pass    

                if '@bol.com.br' in str(line.lower()): 
                    with open('BOL.txt', 'a', encoding="utf8") as file2: 
                        file2.write(str(line))
                        print(f"+1   ->   {str(line)}")
                        pass

                if '@globo.com.br' in str(line.lower()): 
                    with open('GLOBO.txt', 'a', encoding="utf8") as file2: 
                        file2.write(str(line))
                        print(f"+1   ->   {str(line)}")
                        pass   

                if '@hotmail.com.br' in str(line.lower()): 
                    with open('HOTMAIL.txt', 'a', encoding="utf8") as file2: 
                        file2.write(str(line))
                        print(f"+1   ->   {str(line)}")
                        pass     

                if '@outlook.com.br' in str(line.lower()): 
                    with open('OUTLOOK.txt', 'a', encoding="utf8") as file2: 
                        file2.write(str(line))
                        print(f"+1   ->   {str(line)}")
                        pass    

                if '@terra.com.br' in str(line.lower()): 
                    with open('TERRA.txt', 'a', encoding="utf8") as file2: 
                        file2.write(str(line))
                        print(f"+1   ->   {str(line)}")
                        pass    

                if '@msn.com' in str(line.lower()): 
                    with open('MSN.txt', 'a', encoding="utf8") as file2: 
                        file2.write(str(line))
                        print(f"+1   ->   {str(line)}")
                        pass    
                        
                if '@mail.com' in str(line.lower()): 
                    with open('MAIL.txt', 'a', encoding="utf8") as file2: 
                        file2.write(str(line))
                        print(f"+1   ->   {str(line)}")
                        pass    

                if '@yahoo.com' in str(line.lower()): 
                    with open('YAHOO.txt', 'a', encoding="utf8") as file2: 
                        file2.write(str(line))
                        print(f"+1   ->   {str(line)}")
                        pass  
                        
                if '@icloud.com' in str(line.lower()): 
                    with open('ICLOUD.txt', 'a', encoding="utf8") as file2: 
                        file2.write(str(line))
                        print(f"+1   ->   {str(line)}")
                        pass    
                        
                else:
                    pass
            except Exception:
                pass
        input('\n               Processo Finalizado! Pressione ENTER Para Fechar!') 
        exit()
except Exception as ee:
    print(f'\n\n      Erro Critico -> {ee}') 
    input()
    exit()


    
