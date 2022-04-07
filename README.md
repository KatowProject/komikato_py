# Komikato
Animanga, read and watch


# Installation
1. Install Python
2. run **pip install requirements.txt** in terminal
3. to running this repo, type **py manage.py runserver** in terminal
4. enjoy.


# RESTful API

List Scraping komikato
## Komikindo
### Status
```
api/komikindo/
```
### Home
```
api/komikindo/home
```
Ex: https://komi.kato-rest.us/api/komikindo/home
### Daftar Komik
```
api/komikindo/daftar-komik/page/<pagination:number>
```
Ex: https://komi.kato-rest.us/api/komikindo/daftar-komik/page/1
### Komik Terbaru
```
api/komikindo/komik-terbaru/page/<pagination:number>
```
Ex: https://komi.kato-rest.us/api/komikindo/komik-terbaru/page/1
### Komik Type (Manga, Manhwa, Manhua)
```
type = [manga, manhwa, manhua]
api/komikindo/komikk/<type:string>/page/<pagination:number>
```
Ex: https://komi.kato-rest.us/api/komikindo/komikk/manga/page/1
### Komik Detail
```
api/komikindo/komik/<endpoint:string>/
```
Ex: https://komi.kato-rest.us/api/komikindo/komik/mamori-mama-wa-o-yobi-janai-no〜-isekai-musuko-hankoki-〜/
### Komik Chapter
```
api/komikindo/chapter/<endpoint:string>/
```
Ex: https://komi.kato-rest.us/api/komikindo/chapter/mamori-mama-wa-o-yobi-janai-no〜-isekai-musuko-hankoki-〜-chapter-8/
### Search Komik
```
api/komikindo/search/<query:string>/?page=<pagination:number>
```
Ex: https://komi.kato-rest.us/api/komikindo/search/kanojo/?page=2

## Otakudesu
### Status
```
/api/otakudesu/
```

### Home
```
api/otakudesu/home
```
Ex: https://komi.kato-rest.us/api/otakudesu/home

### Search Anime
```
api/otakudesu/search/<query:string>
```
Ex: https://komi.kato-rest.us/api/otakudesu/search/kanojo

### Anime Detail
```
api/otakudesu/anime/<endpoint:string>
```
Ex: https://komi.kato-rest.us/api/otakudesu/anime/deaimon-sub-indo/

### Anime Episode
```
api/otakudesu/eps/<endpoint:string>
```
Ex: https://komi.kato-rest.us/api/otakudesu/eps/deimon-episode-1-sub-indo/
### Jadwal Rilis
```
api/otakudesu/jadwal-rilis
```
Ex: https://komi.kato-rest.us/api/otakudesu/jadwal-rilis
### Daftar Anime
```
api/otakudesu/daftar-anime
```
Ex: https://komi.kato-rest.us/api/otakudesu/daftar-anime