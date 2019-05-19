# Interfatec2019
Resolução dos problemas apresentados na maratona de programação: interfatecs 2019

#Parking - Problema A
O estacionamento funciona desde o primeiro carro chegar, até o último sair, independente de ficar vazio entre esse tempo.
O programa lê todas os horários de entrada/saída os comparando primeiramente com um valor fora do limite, e após entre si para determinar o maior e menor horário em minutos. O programa retorna a maior hora de saída em minutos, menos a menor hora de entrada também em minutos.

#Xuquism - Problema B
Há uma relação matemática entre as respostas (true/false) e a saída esperada.
O programa não monta a arvore como indicada, no lugar ele salva a posição de cada programa de tv em um dicionário com a chave sendo o primeiro número da entrada e o valor a string após o espaço. Para chegar na chave esperada o programa começa com o valor 1, o dobrando para toda resposta verdadeira, e o dobrando e somando 1 para toda resposta falsa. Com a chave obtida o programa imprime o valor correspondente a ela armazenado no dicionário.

#Epidemia - Problema C
Se os pacientes podem apenas tomar todos os remedios ou nenhum, o número maximo de pacientes é definido pelo remédio com menor quantidade.
O programa lê a quantidade de cada remédio, os adiciona a uma lista e a ordena de menor para o maior, após o programa retorna o primeiro valor da lista.

#Megabobagem - Problema I
Para um conjunto de letras ser um palíndromo, é necessário que quando dividir ele ao meio, haja o mesmo número de letras de cada lado. Ou seja, se o conjunto for par, é necessário que todas ocorrencias de cada letra seja um número par, se o conjunto for impar, no máximo uma letra pode ter suas ocorrencias como impar.
O programa lê o conjunto de letras e analisa as ocorrencias de cada letra. Após ele conta o número de ocorrencias impares. Se esse valor for menor que 1, retorna verdadeiro, se for 1 e o número de letras no conjunto for impar, retorna verdadeiro. Nos outros casos retorna falso.

