# Artificial_Intelligence_Second_Assignment_INF01048

## Alunos:
- Leonardo Barros Bilhalva - Turma A - Cartao: 315768
- Gilmar Felix - Turma B - Cartao: 303051

## Decisões de projeto e Estratégia de parada:
A função MINMAX com poda alfa-beta foi utilizada para executar as escolhas de movimento. A cada execução dela, isto é, hora min, hora max, a função shouldEval verifica a condição de parada com base em três fatores: profundidade máxima avaliada igual a 5 e se não há movimentos legais ou jogadas disponíveis. Não foram utilizadas bibliotecas extras fora as já mencionadas pelo professor.

## Função de avaliação:
A função de avaliação foi escolhida baseada no artigo "An analysis of Heuristics in Othello". Desse artigo, foram utilizados os seguintes fatores:
- Parity: Essa característica versa sobre a diferença de moedas totais entre o jogador max e min. Minimizar as peças convertidas se mostrou uma boa estratégia. O peso final para essa estratégia foi de 20.
- Mobility: Essa característica utiliza de uma relação entre o máximo de movimentos do jogadores max e min. A ideia é maximizar as jogadas possíveis de max enquanto se minimiza as jogadas possíveis de min. O peso final para essa estratégia foi de 40 pontos.
- Corner: Os principais quatro cantos do tabuleiro são posições preciosas dentro do jogo. A peça alocada nele não pode ser flanqueada, ou seja, esta sempre protegida de eventuais jogadas de ataque. O maior peso da nossa heurística se baseou na busca por cantos, com um total de 180 pontos.

A função de avaliação também utilizou um método de cálculo baseado na implementação de uma interpretação do artigo anterior chamado "Heuristic/Evaluation Function for Reversi/Othello":
- CornerReach: As posições ao redor dos 4 cantos também são fundamentais para serem analisadas. Repare que um posicionamento pode abrir margem para que o adversário chegue ao canto por meio de uma jogada de ataque. Essa ideia foi recolhida da implementação, porém adicionamos um peso maior a ela, visto que os testes se mostraram positivos com relação a isso. O peso final para esta heuristica foi de 60 pontos.

# Dificuldades do projeto:
As maiores dificuldades se deram na organização do grupo. A falta de tempo disponível para o trabalho dificultou muito a entrega. Talvez, com um membro a mais as coisas pudessem ter sido diferentes. Esperamos conseguir organizar melhor para o próximo trabalho. A execução dos testes para divisão dos pesos também foram trabalhosas, pois os testes foram feitos todos manualmente(trocando pesos e rodando certo número de vezes o projeto).

# Melhorias futuras:
Os próximos passos seriam implementar as estratégias restantes no artigo analisado. Também dedicar mais tempos aos testes e balanceamento de pesos, rodando contra outros agentes a fim de ter uma simulação melhor da realidade.

# Referências:
- "An analysis of Heuristics in Othello" - https://courses.cs.washington.edu/courses/cse573/04au/Project/mini1/RUSSIA/Final_Paper.pdf

- "Heuristic/Evaluation Function for Reversi/Othello" - https://kartikkukreja.wordpress.com/2013/03/30/heuristic-function-for-reversiothello/