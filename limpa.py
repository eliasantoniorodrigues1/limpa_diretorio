import os
import re
from pathlib import Path
from datetime import datetime, timedelta


delta = datetime.today() - timedelta(days=30)
def remove_arquivos_antigos(pasta):
    if not os.path.isdir(pasta):
        raise NotADirectoryError(f'{pasta} não existe.')

    for root, dir, files in os.walk(pasta):
        arq_deletado = []
        for file in files:
            caminho = pasta + '/' + str(file)
            info = Path(caminho).stat()
            if datetime.fromtimestamp(info.st_mtime) <= delta:
                print(f'Removendo "{caminho}" ...')
                try:
                    os.remove(caminho)
                except Exception as erro:
                    file = erro

            arq_deletado.append(file)
    return arq_deletado


def grava_log(lista):
    data = pega_somente_numero(str(delta))
    arquivo = 'log_' + data + '.txt'
    with open(arquivo, 'w', encoding='utf-8') as file:
        for nome in lista:
            file.writelines(f'{nome}\n')
    print('Arquivos removidos do diretório com sucesso!')


def pega_somente_numero(texto):
    return re.sub(r'[^0-9]', '', texto)


if __name__ == '__main__':
    string_path = r"D:\Projetos\17 - Programação\limpa_diretorio\H"
    nova_string = re.sub(r'[\\]', '/', string_path)
    lista = remove_arquivos_antigos(nova_string)
    grava_log(lista)
