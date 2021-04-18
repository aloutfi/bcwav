bcwav: a simple python script to set tags for wav tracks downloaded from [bandcamp](bandcamp.com) that makes extensive use of the [music-tag library](https://pypi.org/project/music-tag/)

Works for wav files downloaded from bandcamp that follow the nomenclature:

`<ARTIST> - <ALBUM> - <TRACK NUMBER> <TITLE>.wav` 

Given a directory this script will:

1. Map the aforementioned fields from the title to the track tags
2. Rename the file with the track title

Example:

```bash
➜ tree .
├── Tipper\ -\ Jettison\ Mind\ Hatch\ -\ 01\ Sayonara.wav
├── Tipper\ -\ Jettison\ Mind\ Hatch\ -\ 02\ Vection.wav
├── Tipper\ -\ Jettison\ Mind\ Hatch\ -\ 03\ Baleen.wav
├── Tipper\ -\ Jettison\ Mind\ Hatch\ -\ 04\ Exit\ Chapel\ Perilous.wav
├── Tipper\ -\ Jettison\ Mind\ Hatch\ -\ 05\ Viscous.wav
├── Tipper\ -\ Jettison\ Mind\ Hatch\ -\ 06\ Sahra.wav
├── Tipper\ -\ Jettison\ Mind\ Hatch\ -\ 07\ C'est\ La\ Vie.wav
├── Tipper\ -\ Jettison\ Mind\ Hatch\ -\ 08\ Tethers.wav
├── Tipper\ -\ Jettison\ Mind\ Hatch\ -\ 09\ Permatemp.wav
├── Tipper\ -\ Jettison\ Mind\ Hatch\ -\ 10\ Fallow.wav
├── Tipper\ -\ Jettison\ Mind\ Hatch\ -\ 11\ Shelled.wav
└── Tipper\ -\ Jettison\ Mind\ Hatch\ -\ 12\ Oi\ Oi\ Spit.wav

➜ python3 ../bcwav/bcwav.py /Full/filepath/to/album/

➜  tree .
├── Baleen.wav
├── C'est\ La\ Vie.wav
├── Exit\ Chapel\ Perilous.wav
├── Fallow.wav
├── Oi\ Oi\ Spit.wav
├── Permatemp.wav
├── Sahra.wav
├── Sayonara.wav
├── Shelled.wav
├── Tethers.wav
├── Vection.wav
└── Viscous.wav
```

The album is now correctly tagged and named, ameliorating track order headaches.

![JMH in VLC](https://i.imgur.com/BCn5F9O.png)

## TODO:

- Bash-ization of execution
- album artwork