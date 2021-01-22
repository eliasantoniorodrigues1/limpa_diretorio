# limpa_diretorio
Percorre o diretório deletando arquivos com data de modificação maior que 30 dias.
Esse script foi desenvolvido para resolver um problema no servidor que estava com excesso de arquivos, quando na verdade precisavamos que o servidor mantesse somente
os arquivos dos últimos 30 dias.
Foi utilizado as bibliotecas os, re, pathlib e datetime para executar essa tarefa.
O algoritmo contém três funções básicas: 
  - remove_arquivos_antigos (recebe uma pasta como parâmetro)
  - grava_log (grava o log do que foi deletado pegando a data e hora da da data de modificação do arquivo.)
  - pega_somente_numero (função utilizada para manter na data somente os números com o uso de uma expressão regular simples)
  
