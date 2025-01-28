# Função JDcrc16
Cálculo CRC16 para validações de informações, Pix, etc..


### Linguagem de programação utilizada
>**python** 


### Dependencia para criação de um executável desta aplicação
pyinstaller  
>https://pyinstaller.org/en/stable/


### Parâmetros necessários para utilização do programa
**Parâmetro 01**: string que será validada  
**Parâmetro 02**: caminho completo do arquivo que será criado com o resultado da requisição  


### Exemplo de utilização
Parâmetro 01: 123456789  
Parâmetro 02: resultado.txt  
Comando: **python main.py 123456789 resulado.txt**  
Resultado esperado: **29B1**  


### Como criar um executável desta aplicação
No terminal digite o comando:  
    pyinstaller main.py -F -n JDcrc  

<a name="my-custom-anchor-point"></a>
    -F: Cria um único arquivo executável com todas as dependências incluídas  
    -n: nome do arquivo executável desejado. (Padrão: nome da rotina principal, neste caso seria: main.exe)  