# Projeto-Engenharia-de-Dados
Projeto de Engenharia de Dados da cadeira IF997

## Atitudes de Pre-processamento propostas:
* Usar médias/medianas em linhas com inteiros pendentes
* Deletar linhas com strings faltantes
* Tentar tratar caso hajam dados diferentes de bool em colunas bool
* Deletar linhas com booleanos faltantes
* Deletar linhas com timestamps faltantes

## Transformações de Dados Propostas:
* timestamp (int) -> weekday (string)

## Novas Colunas Propostas:
* Aparelhos por conta (int)
* Wallpaper por contas no dispositivo (float)
* Download Externo (bool) = root (true) + loja oficial (false)
* Instalação em dispositivo diferente? (bool) (count_installation_on_different_devices)


## Coisas a pensar:
1. Quais dados importam pra validação cadastral?
  * Apps instalados da loja oficial?
  * É emulador?
  * Tem app de localização falsa?
  * O aparelho tem root?
  * Contas por aparelho
  * Aparelhos por conta
  * Dia do acesso da conta

2. O que ajuda a identificar um dispositivo?
  * ID do dispositivo
  * Em quantos dispositivos diferentes essa conta fez uma instalação (num período de tempo determinado)

3. Como a localização se comporta em dispositivos?
  * Analisar uso de fake localização e sua ativação

## Gráficos Relevantes:
1. Valor médio, valor máximo e desvio padrão da idade (bar chart)
2. Porcentagem de celulares rooteados (bar chart)
3. Logins por dia da semana (pie chart)
4. Logins por timestamp (plot)
5. Média de logins por dia (plot)
6. Aparelhos por conta em média, mediana e desvio padrão (bar chart)
7. Valor médio de reinicializações (bar chart)
8. 
9. 
10. 

## Perguntas a fazer:
1. Será que dispositivos com mais contas por wallpapers tem associação com account takeover?
2.
3.
4.
5.
6.
7.
8.
9.
10.
