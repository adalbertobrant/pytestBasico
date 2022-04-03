**PYTEST** 

**UM EXEMPLO BÁSICO FÁCIL DE USO** 

`  `Olá, eu não sei nada de testes, mas achei legal essa lib pytest, estou aprendendo agora e esse pdf é uma forma de eu reforçar o meu aprendizado, se você achou legal me mandar um stars no meu repo sobre o assunto pytest. Espero a sua estrelinha e quem sabe até um issue , crítica ou um hello world.

`  `Do pouco que eu entendi sobre testes, eles ajudam a eliminar os prints da tela, quando queremos achar o bug, eu acho o debuguer também uma ferramenta super válida mas escrever um programa que vê se seu programa esta certo ou errado não tem preço.

`  `Caso queira saber como instalar o site de consulta é [https://docs.pytest.org](https://docs.pytest.org/)

 A seguir eu tirei fotos de um sistema que fiz para ver os erros e desculpem se tem alguma coisa errada, mas estou aprendendo ainda

`   `Grande abraço e gimme STARS  ![](Aspose.Words.2531020a-91df-4bd7-bb88-7f2ea0795365.001.png)

![](Aspose.Words.2531020a-91df-4bd7-bb88-7f2ea0795365.002.png)

Aqui você cria um arquivo para ser o teste, ele deve começar com a palavra test_ no início do arquivo ou no final _test. 

  Na foto vemos que optei por colocar no início então ficou test_maximo_3.py. 

![](Aspose.Words.2531020a-91df-4bd7-bb88-7f2ea0795365.003.png)

Dentro do arquivo test_maximo_3.py 
  Vamos inserir a lib do pytest dando um import

  import pytest

  E depois vamos importar o nosso arquivo nesse caso chamamos o mesmo de maximo_3.py , ou seja é um programa que pega 3 números e retorna o maior deles.

  import maximo_3 as max3 



![](Aspose.Words.2531020a-91df-4bd7-bb88-7f2ea0795365.004.png)

No terminal chamamos o programa pytest  test_maximo_3.py

E já temos o nosso primeiro teste, nesse caso mostrando o erro ou seja não temos o arquivo maximo_3.py

![](Aspose.Words.2531020a-91df-4bd7-bb88-7f2ea0795365.005.png)

Criamos o nosso arquivo maximo_3.py, que pega 3 parâmetros definidos na função maximo_3(x,y,z)

   Vamos ver agora o que o pytest tem a dizer, quando rodarmos novamente o nosso arquivo de teste qual erro ele vai mostrar ???

![](Aspose.Words.2531020a-91df-4bd7-bb88-7f2ea0795365.006.png)

Eita e eu achei que ia mostrar um super erro, kkk

   Então não mostrou nada mas ele nos diz “ no tests ran in 0.00s “ , inclusive Super Rápido.

   Isso aconteceu pois no nosso arquivo de testes não tem nenhum teste, mas agora vamos fazer alguns testes, segue a fita ...

![](Aspose.Words.2531020a-91df-4bd7-bb88-7f2ea0795365.007.png)

Aqui temos o nosso primeiro teste, nesse caso ele indica um erro de tipo pois nossa função só aceita números e não strings.

  Vamos no terminal e testamos novamente o nosso programa test_maximo_3.py usando o pytest, o que será que ele vai mostrar agora ???

![](Aspose.Words.2531020a-91df-4bd7-bb88-7f2ea0795365.008.png)

Opa deu um erro falando que esta retornando None, mas é claro eu não escrevi nada ainda no arquivo maximo_3.py, vamos escrever a função e testar novamente.

![](Aspose.Words.2531020a-91df-4bd7-bb88-7f2ea0795365.009.png)

Já escrevemos a função que retorna o maior valor e agora vamos testar novamente o programa, usando o nosso outro programa test_maximo_3.py.

  E agora o que vai ser mostrado ???

![](Aspose.Words.2531020a-91df-4bd7-bb88-7f2ea0795365.010.png)

Que bom o teste funcionou, agora podemos escrever mais testes para o nosso arquivo de testes e verificar se o nosso programa esta funcionando de acordo com o esperado. Então vamos para mais alguns testes...

![](Aspose.Words.2531020a-91df-4bd7-bb88-7f2ea0795365.011.png)

Escrevi mais umas linhas para verificar no caso se esta passando o maior número, linhas 5 a 7 e também nas linhas 12 a 14 para ver o resultado se todos os números forem iguais, poderia escrever mais testes, mas acho que já entendemos, pelo menos essa parte.

   Espero que tenha gostado e mande uns stars no meu repo sobre o pytest



Esse markdown foi convertido de um pdf, vamos arrumando com o tempo os arquivos da foto e diagramação.



