# lab-3-vcs-and-models

## Steps to get this django app running on your own server

1) Open a terminal and navigate to the folder you want to create your project in (e.g. `cd ~Documents/Code`)
2) Clone this repository with `git clone https://github.com/Carleton-BIT/lab-3-vcs-and-models.git`
3) On the command line, install dependencies (`pip install django python-decouple`)
4) In your project folder (lab-3-vcs-and-models/studentdemo) create a file called `.env`
5) Generate a secret key by running `python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'`
6) Edit `.env` with your text file, and add a line that says `SECRET_KEY="your-secret-key-here"`
