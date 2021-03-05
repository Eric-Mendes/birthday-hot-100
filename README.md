# birthday-hot-100 <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/95/Billboard_logo.svg/1280px-Billboard_logo.svg.png" width=100 align="right">

## Descubra como estava a Billboard Hot 100 no dia do seu aniversário!
Este script é um web-scraper da página da Billboard que pega o Hot 100 chart no dia do seu aniversário, ou em qualquer dia que você definir.

## Para rodar
Para rodar este script você precisa - além de instalar tudo o que é importado no script - [baixar o gecko-driver](https://github.com/mozilla/geckodriver/releases "Ir para a página de download") e especificar o caminho dele em:
```
browser = webdriver.Firefox(executable_path="/PATH_TO_GECKO_DRIVER/")
```
Você também irá precisar especificar o caminho de onde você quer salvar o csv com o Hot 100 do dia especificado em:
```
path_to_save = '/.../BILLBOARD_HOT_100/billboard_hot_100_week_{day}-{month}-{year}.csv'.format(day=birthday_day, month=birthday_month, year=birthday_year)
```
## Futuramente...
1. Planejo integrar este script com a [API do Spotify](https://developer.spotify.com/documentation/web-api/ "Ir para a página desta API") para salvar uma playlist personalizada com as músicas que estavam no Hot 100 do dia especificado.<br/>
2. Ficarei feliz se algum web dev quiser me ajudar a transformar isto em um site.

## Melhorias
Não sei mexer com Docker (ainda). Se você souber e conseguir diminuir as install dependencies deste projeto esta será uma ajuda muito bem vinda! Me chame no [LinkedIn](https://www.linkedin.com/in/eric-velasco-de-paula-mendes/ "Meu perfil no LinkedIn") para organizarmos isto.
