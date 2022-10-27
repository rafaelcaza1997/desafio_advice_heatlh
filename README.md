<h1>Setup da aplicação:</h1>

Para a construção da imagem da aplicação no docker, o seguinte comando foi utilizado:

docker build -t [nome_imagem] . 
Por exemplo:
docker build -t carford_flask . 

Para a run da imagem:
docker run -p 5000:5000 -d [nome_imagem] 
Por exemplo:
docker run -p 5000:5000 -d carford_flask 

Caso prefira obter a imagem pelo do DockerHUB:
docker pull rafaelcazarotto/desafio_carford_flask:latest

<h1>Primeiros Passos com a aplicação:</h1>
<h2>Etapa de Sign Up</h2>
- Primeiro passo para utilizar o site é realizar o Sign Up.
- Após o sign up, a aplicação irá logar automaticamente na conta criada. 

<h2>Etapa de adição de Modelos e Cores</h2>
- Clique na opção “Models” na barra de navegação.
- Clique na opção, “Add New Vehicle Model”, e na opção disponível, coloque o nome do modelo.
- Seguindo o teste, insira o nome do modelo “Hatch” e clique em “Save”.
- Repita esse passo para os modelos “Sedan” e Conversible”.
O resultado deverá ser como o da imagem a seguir:
 
 ![image](https://user-images.githubusercontent.com/74441553/197645841-8606f7a8-5919-4609-a39c-cd3a2083784d.png)
 
- Ao finalizar, cadastre as cores, clicando na opção “Add New Color”.
- Seguindo o teste, insira o nome da cor “Yellow”, clique no quadro de cor e selecione o tom da cor desejado.  
- Repita esse passo para as cores “Blue” e “Gray”. 
O resultado deverá ser como o da imagem a seguir: 
 
![image](https://user-images.githubusercontent.com/74441553/197645852-7c2b3b8e-e292-4c27-9a0c-edecc2a92a91.png)

Importante destacar que o ícone criado a direita de cada item de “Models” e “Colors” realiza a exclusão do item. Porém, pensando na regra de negócio do site, permiti que a exclusão só acontecesse caso a cor ou modelo não esteja em nenhum carro já atribuído a algum cliente. Pois, pensando em carros de clientes, não é possível trocar o modelo ou cor sem uma alteração física, logo, excluir o modelo ou cor seria o mesmo que interferir no histórico da aplicação.
 Etapa de adição de Clientes
Continuando o processo, agora devemos criar um cliente, para isso:
- Acesse a página de cliente clicando na aba “Clients” no menu de navegação. 
Como não tem nenhum cliente cadastrado, essa tela estará com a lista vazia. 
Para cadastrar um cliente:
- Clique na opção “Add New Client”.
A seguinte tela irá aparecer:
 
 ![image](https://user-images.githubusercontent.com/74441553/197645875-7722e62f-9a4f-4c90-8a43-300fcbe305c7.png)

Coloque as informações referentes ao cliente, como nome, sobrenome, telefone e e-mail. (O telefone não é validado, qualquer valor pode ser colocado).
Nessa tela, é possível adicionar veículos caso desejado, entende-se como veículo uma combinação entre modelo e cor. 
Colocando os seguintes dados:
- First Name: Nome
- Last Name: Cliente
- Telephone: 12345678
- E-mail: cliente@cliente.com
Obtemos o seguinte resultado na lista de clientes:

![image](https://user-images.githubusercontent.com/74441553/197645889-e2145af1-68c9-40bc-bbd6-d48b3fc081ce.png)

É possível observar que o cliente já foi marcado como uma oportunidade de venda, isso se deve ao fato de não possuir nenhum veículo atribuído. 
Os ícones a direita são referentes a edição e exclusão, sucessivamente.
Clicando em edição, a seguinte tela irá aparecer:
  
 ![image](https://user-images.githubusercontent.com/74441553/197645911-08cfd042-ad9c-4505-aeca-e654c947a38b.png)

Clicando em “New Vehicle”, podemos adicionar um novo veículo ao cliente, resultando na seguinte tela:

![image](https://user-images.githubusercontent.com/74441553/197645943-61f71b42-57e6-46c8-a6a7-d129bfdb899d.png)

	Após selecionar o modelo e a cor, clique em “Confirm”.
 
 ![image](https://user-images.githubusercontent.com/74441553/197645953-1886ab67-50df-4c96-b03a-d99c9a20dcce.png)

Clicando em “Save”, o cliente será atualizado. 
É possível observar que a tag de oportunidade de venda do cliente foi removida. Isso se deve ao fato de que o cliente agora possui um veículo atribuído. 
 
 ![image](https://user-images.githubusercontent.com/74441553/197645974-a1290b1d-3e05-42b0-aab1-dd4c560b8f25.png)
 
<h2>Visualização de detalhes do Modelo</h2>
Clicando em Models, agora é possível obter informações referentes ao modelo. Clicando na aba do “Sedan”, é possível expandi-la para obter mais informações. 
  
  ![image](https://user-images.githubusercontent.com/74441553/197646001-2d411612-53ef-4d6f-b777-76d000d5b5f6.png)

Clicando no ícone de redirecionar, é possível abrir uma tela para a visualização dos clientes que possuem esse modelo. Assim como fácil acesso a edição desses clientes:
 
 ![image](https://user-images.githubusercontent.com/74441553/197646019-3fdd5027-7b61-4f3b-8873-cffe95c4c99e.png)
 
<h2>Opção New Sale</h2>
A opção “New Sale”, na barra de navegação, foi uma maneira de adicionar rapidamente um veículo a um cliente, sem a necessidade de explorar a aba de “Clients” em busca do cliente desejado. 
Clicando na opção “New Sale” na barra de navegação, a seguinte tela irá aparecer:
 
 ![image](https://user-images.githubusercontent.com/74441553/197646031-d1a9af6e-31f1-4c6e-87a9-00cd69bbe928.png)

Após selecionar as informações desejadas, clique em “Save” para salvar as informações:
 
 ![image](https://user-images.githubusercontent.com/74441553/197646044-73327277-8a12-4878-b262-cfe6982daf5c.png)

Após clicar na opção “Save”, a página será redirecionada para a tela de Clientes, onde será possível verificar a atualização.

 ![image](https://user-images.githubusercontent.com/74441553/197646057-b8f3b4bb-c4cf-487c-b5db-a7442df09a9d.png)

