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
5. Emulador VS Sem Emulador (pie chart)
6. Contas por aparelho em moda, média, mediana e desvio padrão (bar chart)
7. Valor médio, mediana e moda de reinicializações (bar chart)
8. Valor médio, mediana e moda de reinicializações diário (bar chart)
9. Média, Mediana e Desvio Padrão de apps máximos instalados por dispositivo
10. Porcentagem de aplicativos instalados fora de loja oficial (pie chart)

## Perguntas a fazer:
1. Será que dispositivos com mais contas por wallpapers tem associação com account takeover?
2. Emuladores e Account Takeovers - Há relações?
3. Root VS Sem root - Quais estão mais relacionados a account takeover?
4. Quantidade de Wallpaper tem relação com account takeover?
5. Quantos aparelhos tem instalações feitas fora de loja oficial? Qual a média?
6. Download Externo (external_download) VS Evento de account takeover - Um heatmap
7. Suspicious Location VS Evento de account takeover - Um heatmap
8. Há relação entre a quantidade média de boots por dia e eventos de account takeover?
9. Existe algum dia da semana onde ocorrem mais account takeovers?
10. Heatmap de correlações