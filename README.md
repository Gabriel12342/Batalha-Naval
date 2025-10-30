BATALHA NAVAL

COMO INICIAR/TERMINAR:
- Para iniciar o jogo, é preciso ter Python instalado na sua máquina para rodar no terminal.
- Abra o terminal na pasta onde o arquivo do jogo está salvo.
- Execute o arquivo principal com o comando: python batalha_naval.py
- O jogo será iniciado diretamente no terminal.
- Para encerrar o jogo, selecione a opção 0 - Sair no menu principal ou feche o terminal.

OPÇÕES OFERECIDAS:
Ao abrir o jogo, é apresentado um menu inicial com quatro opções (de 0 a 3):

1 - Posicionar embarcações:
- O jogador deve preencher as posições cartesianas das suas embarcações (coordenadas de linha e coluna entre 0 e 9).
- São cinco embarcações tanto para o jogador quanto para o computador.
- O campo de batalha é um tabuleiro 10x10.
- O computador posiciona suas embarcações automaticamente, escolhendo posições aleatórias com a função randint() da biblioteca random.

2 - Atacar:
- O jogador deve escolher as posições cartesianas da linha e coluna onde acredita que estejam as embarcações do computador.
- O computador também atacará as embarcações do jogador, escolhendo posições de forma aleatória.
- Tanto o computador quanto o jogador podem atacar em rodadas seguidas se acertar uma embarcação, passando a vez apenas se errar ou atacar uma posição já atingida.

3 - Mostrar tabuleiro do computador:
- Permite visualizar o campo do computador antes ou depois de posicionar as embarcações, ou durante o jogo para acompanhar o progresso.

0 - Sair:
- Para encerrar o jogo.

PRINCIPAIS TELAS:
- Menu inicial
- Preenchimento dos tabuleiros
- Escolha das posições de ataque e exibição dos resultados (acerto ou erro)
- Visualização do tabuleiro do computador
- Resultado final com o vencedor

Símbolos utilizados:
- "~": água
- "<->": embarcação
- "X": embarcação atingida
- "o": tiro na água (erro)

REGRAS DOS TURNOS:
- Se o jogador acertar, joga novamente.
- Se errar, passa a vez para o computador.
- Se escolher uma posição já atacada, perde a vez.
- O jogo termina quando todas as embarcações de um dos lados são destruídas.

REQUISITOS:
- Python 3.8+
- Nenhuma biblioteca externa é necessária (usa apenas random).

CONCLUSÃO:
O sistema Batalha Naval em Python cumpre o objetivo principal de permitir que o jogador enfrente o computador em um jogo de batalha naval no terminal. Ele apresenta uma interface simples, com menus claros e retorno visual imediato sobre os acertos e erros de cada jogada, tornando a experiência intuitiva para iniciantes.

Considerações finais:
- Funcionalidade: O jogo funciona de forma estável, com o computador atacando de forma aleatória e os turnos sendo respeitados.
- Interface: Por ser baseado em terminal, a visualização é limitada a texto e símbolos, mas ainda assim fornece feedback suficiente para jogar.
- Aprendizado: Excelente ferramenta para praticar lógica de programação, listas bidimensionais, loops e controle de fluxo em Python.

Limitações e problemas conhecidos:
- O computador não possui inteligência estratégica, atacando apenas de forma aleatória.
- Todas as embarcações têm tamanho 1x1, não sendo possível colocar navios maiores ou em posições contínuas.
- A interface de terminal pode ficar confusa em telas pequenas, pois os tabuleiros são impressos constantemente sem paginação.
- Não há salvamento de progresso, então cada partida precisa ser jogada do início.
- Validação de entradas impede valores fora de 0-9, mas não há tratamento para entradas não numéricas durante os turnos de ataque.

Possíveis melhorias futuras:
- Adição de navios maiores e orientação vertical/horizontal
- Implementação de inteligência artificial mais sofisticada
- Interface gráfica com Kivy ou Pygame
- Salvamento de partidas e estatísticas de desempenho
