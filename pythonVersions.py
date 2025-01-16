#! pyhon3
# pythonVersions.py - compara a versões do python utilizada pelo computador
# com a versão mais recente encontrada no sítio ‘web’ do python

import sys, requests,bs4
from windows_toasts import WindowsToaster, Toast


def searchNewVersion(r, actual, url):
    try:
        # Faz uma busca na página pela versão mais recente do python
        if r.status_code == 200:
            soup = bs4.BeautifulSoup(r.text, 'html.parser')

            firstItem = soup.find('ol', {'class': 'list-row-container menu'}).find('li')
            lastVersion = firstItem.find('span', {'class': 'release-version'}).text.strip()
            lastVersion = list(map(int, lastVersion.split('.')[0:2])) # salva o major e o minor de uma nova versão em uma lista
            
            lVer = str(lastVersion[0]) + '.' + str(lastVersion[1])
            aVer = str(actual[0]) + '.' + str(actual[1])
            
            for i in range(2):
                if (lastVersion[i]) > (actual[i]): # compara a versão atual do computador com a buscada na página
                    guiAlert(lVer, aVer, url)
                    break
                
            return 0
        
    except AttributeError:
        return 1


def guiAlert(lv, av, url):
    # mostra uma mensagem de alerta no Gui  
    title = WindowsToaster('Python') 
    message = Toast()

    message.text_fields = [f'Bom dia Alexssandro!\nVocê está usando a versão {av} do python, por favor visite o site:\n\'{url}\'\t para instalar a versão {lv} ;)'] 
    title.show_toast(message)


def main():
    url = 'https://www.python.org/downloads/'
    actualVersion = list(sys.version_info[:2]) # verifica a versão do python sendo utilizada e salva o major e o minor em uma lista
    r = requests.get(url) # faz uma chamada a pagina destacada
    searchNewVersion(r, actualVersion, url)
    
if __name__ == '__main__':
    main()
