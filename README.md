# CatalogoHoteis
delete the worst options

Answer to this question:

Você está implementando um site de pesquisa de hotéis.
Os viajantes utilizam três critérios para escolha de um hotel: preço por diária, distância até a praia e 
qualidade (medida em estrelas).
Digamos que em uma cidade existem três hoteis: 009:52 26/09/2018
 Hotel        Preço    Distância da Praia     Estrelas
 Hotel A     160,00        200m              4 estrelas
 Hotel B     160,00        400m              3 estrelas 
 Hotel C     560,00        100m              5 estrelas 
Neste exemplo, o Hotel B é igual ou pior ao Hotel A em todos os aspectos: é mais longe da praia, tem o mesmo preço e tem
menor qualidade. Neste caso, o Hotel A é certamente uma escolha melhor que o Hotel B, e assim, o Hotel B não será exibido
para o usuário no ﬁltro de busca do seu site. Já o Hotel C é melhor que o Hotel A em dois aspectos
(distância da praia e qualidade), mas pior em preço (mais caro).
Neste caso, o Hotel C também será exibido ao usuário para que ele decida.

Escreva um programa em python que recebe os hoteis existentes em uma cidade e seus atributos de preço,
distância da praia e estrelas e ﬁltre os melhores hoteis.
Um hotel X será retirado da lista ﬁnal desde que exista um outro hotel Y, tal que Y é melhor do que X em pelo menos um 
aspecto e melhor ou igual a X em todos os outros. Exemplo de entrada: 
Hotel  Preço Distância da Praia Estrelas 
hotel0  300         100            5 
hotel1  100         900            3 
hotel2  400         100            4 
hotel3  300         200            5
Saída: hotel0 hotel1 
