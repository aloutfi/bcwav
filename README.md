bcwav: a simple python script to set tags for wav tracks downloaded from [bandcamp](https://bandcamp.com) that makes extensive use of the [music-tag library](https://pypi.org/project/music-tag/)

## Installation

To use `bcwav`, you'll need Python 3 installed on your system. You can check if Python is installed by running `python3 --version` in your terminal. If you don't have Python 3, you can download it from the [official Python website](https://www.python.org/downloads/).

Next, follow these steps to set up `bcwav`:

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/aloutfi/bcwav.git
   ```

   Replace `your-username` with your GitHub username or use the repository URL provided in the README if it's already configured on GitHub.

2. Navigate to the `bcwav` directory:

   ```bash
   cd bcwav
   ```

3. Install the required Python packages using `pip`:

   ```bash
   pip install -r requirements.txt
   ```

   This will install the necessary packages, including `music-tag`.

4.  You can create an alias for `bcwav` in a single Bash command using the `alias` command. Here's the one-liner to create the alias:

   ```bash
   echo "alias bcwav='python3 /path/to/bcwav.py'" >> ~/.bashrc && source ~/.bashrc
   ```

   Replace `/path/to/bcwav.py` with the actual path to your `bcwav.py` script.

## Usage

Once you've installed `bcwav`, you can use it to organize and tag your Bandcamp WAV files as described in the README.

Here's how to use `bcwav`:

1. Open your terminal.

2. Navigate to the directory where your Bandcamp WAV files are located. For example:

   ```bash
   cd /path/to/your/wav/files/
   ```

3.  You can create an alias for `bcwav` in a single Bash command using the `alias` command. Here's the one-liner to create the alias:

   Replace `/path/to/bcwav.py` with the actual path to your `bcwav.py` script.

4. `bcwav` will process the files in the specified directory, set tags, and rename the files according to the track titles. You should see terminal output indicating the progress.

5. After the script has finished, your WAV files will be correctly tagged and renamed in the same directory.

Works for wav files downloaded from Bandcamp that follow the nomenclature:

`<ARTIST> - <ALBUM> - <TRACK NUMBER> <TITLE>.wav` 

Given a directory, this script will:

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

➜ bcwav /Full/filepath/to/album/

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

