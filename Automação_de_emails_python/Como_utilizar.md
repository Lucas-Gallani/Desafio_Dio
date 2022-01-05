# Automação de E-mails com gmail em Python

bem vindos ao tutorial de como enviar e-mails repetitivos e cansativos utilizando a linguagem de programação Python!

utilizarei de prints para facilitar o entendimento

- #### Importar as bibliotecas yagmail e time

![image-20220105154805705](https://user-images.githubusercontent.com/97065309/148282988-eafaef16-54c3-43a8-a2a4-dda0ed839364.png)

Logo no topo do código podemos ver as duas bibliotecas que foram importadas. Explicarei sobre o uso delas na hora certa. Porém deixarei um link para a documentação de ambas.

[Link_Doc_Yagmail](https://pypi.org/project/yagmail/)

[Link_Doc_time](https://docs.python.org/3/library/time.html?highlight=sleep#time.sleep)

- ### Contador & emails

![image-20220105155453353](https://user-images.githubusercontent.com/97065309/148282563-e7443edf-2059-4378-aa89-281ac3019258.png)

duas variáveis  foram declaradas:

- cont = 0 - Será utilizado para percorrer pela lista de e-mails. (Não é necessário modifica-la)
- e-mails = [] - Será onde armazenaremos os e-mails. (Aqui você irá inserir todos os e-mails dos destinatários)

No exemplo abaixo mostrarei como enviar currículos para empresas, mas visando  o seu contexto, pode utilizar para o que for necessário.

![image-20220105160019911](https://user-images.githubusercontent.com/97065309/148283105-104f4338-39dd-4447-81a2-ea66f2f76bd2.png)

Você pode inserir quantos e-mails forem necessários, lembrando sempre de separar todos pela virgula e mantê-los dentro dos colchetes. 

- ### While

![image-20220105160404247](https://user-images.githubusercontent.com/97065309/148283259-55046d32-b0f8-49cc-ba26-52e5edefc90b.png)

Dentro do meu laço de repetição **while**, foi declarado que enquanto o contador for menos do que a quantidade de itens na variável e-mail, ele prossiga repetindo o laço.

O comando **len(e-mails)** traz a quantia de itens dentro de uma lista

no meu caso

![image-20220105160019911](https://user-images.githubusercontent.com/97065309/148283105-104f4338-39dd-4447-81a2-ea66f2f76bd2.png)

O comando: print(len(emails))

me retorna o valor **3**

Ou seja enquanto o contador for menor do  que 3 ele continua se repetindo.

- ### Dentro do While

###### receiver

![image-20220105161138810](https://user-images.githubusercontent.com/97065309/148283351-459f1ee3-330d-471f-97e9-262cf6438e08.png)

Nesta variável será onde pegaremos cada e-mail separadamente, o comando emails[cont], Pegaremos eles pelo índice.

Exemplo: 

Por mais que tenhamos 3 itens dentro de emails, em relação a índice eles possuem valores diferentes. 

![image-20220105160019911](https://user-images.githubusercontent.com/97065309/148283105-104f4338-39dd-4447-81a2-ea66f2f76bd2.png)

                  ^                      ^                        ^

		      0                      1                        2

Na foto acima vemos os índices, então quando falamos emails[0] estamos dizendo de **empresa1@gmail.com**, ou emails[1] **empresa2@gmail.com** e assim por diante.

###### Corpo do email e anexos

![image-20220105161954202](https://user-images.githubusercontent.com/97065309/148283823-3c209752-bfd4-441a-82b4-c78d0d71220d.png)

Dentro desta variável iremos preencher com o corpo do e-mail, e se nescessário iremos adicionar um anexo a ele.

Se adicionar aspas triplas no inicio e final podemos adicionar quebras de linha no texto.

![image-20220105162340342](https://user-images.githubusercontent.com/97065309/148283908-2c750f86-dd63-4d39-9dd8-b1806703692e.png)

![image-20220105162438287](https://user-images.githubusercontent.com/97065309/148283935-de15bdb1-85a5-496b-86d0-c358fbbd7647.png)

Logo após adicionar o corpo do seu e-mail é possível também é possível adicionar um anexo, logo após as ultimas 3 aspas, adicionando uma virgula, podemos adicionar o nome do arquivo.

Porém o arquivo deve estar nas mesma pasta de seu projeto de python.

![image-20220105163102720](https://user-images.githubusercontent.com/97065309/148284072-409e8969-7a2c-420f-a6b4-fe7ac986c6db.png)

Agora com todos os arquivos na mesma pasta podemos adiciona-lo.

![image-20220105163229284](https://user-images.githubusercontent.com/97065309/148284259-6b0c16fc-d440-4ea5-a170-dd66c1b9c5e8.png)

###### login

![image-20220105164313885](https://user-images.githubusercontent.com/97065309/148284367-4526c153-ba25-4f02-949d-deeb65317d5b.png)

Nesta variável iremos inserir o e-mail e senha do nosso gmail da seguinte forma:

![image-20220105164528733](https://user-images.githubusercontent.com/97065309/148284420-d7c3d971-335c-4b3c-8ad8-fc628761ae21.png)

nada muito difícil de se entender.

###### montando todo o e-mail

![image-20220105164221695](https://user-images.githubusercontent.com/97065309/148284490-1daf5e2d-3369-4a93-ad49-78025631736c.png)

o comando sender.send, é o comando onde tudo o que definimos acima será utilizado.

O campo **to** recebe a variável **receiver**, que já foi definido acima, é nele onde será definido quem irá receber o e-mail.

O campo **subject** irá receber o Assunto de nosso e-mail, por isso preencha da forma que lhe for nescessário.

![image-20220105164729566](https://user-images.githubusercontent.com/97065309/148284542-0a0112b2-56ab-418d-b541-0d5f0790253a.png)

O campo **contents** receberá a variável **message**, que foi definida com o corpo do e-mail e o anexo (caso tenha utilizado o anexo)

E por fim chegamos aos dois últimos comandos.

![image-20220105165053238](https://user-images.githubusercontent.com/97065309/148284576-d1a497de-9fed-4095-870a-c88a0fd9662c.png)

Em **cont += 1**, a variável contador que lá em cima do código recebeu o valor de 0, irá se somar com o valor 1, ou seja o código percorrerá cada linha, irá ler o corpo, usuário/senha, anexo e todos os outros comando.

O primeiro e-mail será enviado ao empresa1@gmail.com, assim que o programa ler o comando **cont += 1**, o contador que começou em 0, agora terá o valor de 1, afinal 0 + 1 = 1.

No segundo e-mail será enviado ao empresa2@gmail.com, e assim por diante até que o contador atinja o número final que será 2, já que o código só funciona enquanto for menor do que o número 3.

Em **sleep(30)**, estou dizendo ao computador para antes de repetir o código ele espere por 30 segundos, para evitar suspensão da sua conta no gmail.



Espero que tenha ficado claro a explicação, qualquer duvida estou a disposição.



Lucas Gallani.
