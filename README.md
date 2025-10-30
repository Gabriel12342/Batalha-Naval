# Batalha-Naval

COMO INICIAR/TERMINAR:
-> Para iniciar o jogo, é preciso ter python instalado na sua máquina para rodar no terminal;
-> Abra o terminal na pasta onde o arquivo do jogo está salvo.
-> Execute o arquivo principal com o comando: python batalha_naval.py
-> O jogo será iniciado diretamente no terminal.
-> Para encerrar o jogo, selecione a opção 0 - Sair no menu principal ou feche o terminal.

OPÇÕES OFERECIDAS:
-> Ao abrir o jogo, é apresentado um menu inicial com quatro opções para se selecionar:
* 1 - Posicionar embarcações: onde o jogador vai preencher as posições cartesianas das embarcações para começar o jogo.
- São cinco embarcações para o jogador e para o computador e o campo consiste em um espaço de 10x10, então o jogador deve escolher posição das linhas e colunas de 0-9.
- O computador irá selecionar as posições das embarcações com números aleatórios de 0-9 pela funsão randint da biblioteca random;
* 2 - Atacar: para finalmente começar a batalha naval entre homem e maquina.
- O jogador de escolher as posições cartesianas da linha e coluna onde se supõe que esteja as embarcações do computador;
- O computador também fará isso mas escolhendo as posições das embarcações do jogador de forma aleatória.
- Tanto o computador quanto o jogador podem atacar em rodadas seguidas se acertar uma embarcação, mas passando a vez se errar ou acertar a mesma posição. 
* 3 - Mostrar tabuleiro do computador: se quiser visualizar o campo do computador antes de iniciar a partida antes ou depois de preencher o tabuleiro;
* 0 - Sair. Para sair do jogo.

PRINCIPAIS TELAS:
- Interface do menu inicial;
- Interface do preenchimento dos tabuleiros;
- Interface da escolha das posições de ataque, do resultado de acerto ou erro da embarcação do jagador e do computador;
- Interface da opção 3;
- Interface do resultado do vencedor.
- Simbolos:
* "~": água;
* "<->": embarcação;
* "X": embarcação atingida;
* "o": tiro na água (erro).

Regras dos turnos:
- Se o jogador acertar, joga novamente.
- Se errar, passa a vez para o computador.
- Se escolher uma posição já atacada, perde a vez.
- O jogo termina quando todas as embarcações de um dos lados são destruídas.

CONCLUSÃO:
O sistema Batalha Naval em Python cumpre o objetivo principal de permitir que o jogador enfrente o computador em um jogo de batalha naval no terminal. Ele apresenta uma interface simples, com menus claros e retorno visual imediato sobre os acertos e erros de cada jogada, tornando a experiência intuitiva para iniciantes.

- Considerações finais sobre o sistema:
* Funcionalidade: O jogo funciona de forma estável, com o computador atacando de forma aleatória e os turnos sendo respeitados.
* Interface: Por ser baseado em terminal, a visualização é limitada a texto e símbolos, mas ainda assim fornece feedback suficiente para jogar.
* Aprendizado: Excelente ferramenta para praticar lógica de programação, listas bidimensionais, loops e controle de fluxo em Python.

- Limitações e problemas conhecidos:
* O computador não possui inteligência estratégica, atacando apenas de forma aleatória. Isso torna o desafio limitado para jogadores mais experientes.
* Todas as embarcações têm tamanho 1x1, não sendo possível colocar navios maiores ou em posições horizontais/verticais contínuas.
* A interface de terminal pode ficar confusa em telas pequenas, pois os tabuleiros são impressos constantemente sem paginação ou rolagem.
* Não há salvamento de progresso, então cada partida precisa ser jogada do início.
* Validação de entradas impede valores fora de 0-9, mas não há tratamento para entradas não numéricas durante os turnos de ataque, o que pode gerar erros se o jogador digitar caracteres inválidos.

Apesar das limitações, o sistema oferece uma experiência completa de batalha naval em Python, sendo facilmente expansível com melhorias futuras, como:
- Adição de navios maiores e orientação vertical/horizontal;
- Implementação de inteligência artificial mais sofisticada;
- Interface gráfica com Kivy ou Pygame;
- Salvamento de partidas e estatísticas de desempenho.
