## SHA-256
```SHA-256
E16B8D1E58F419F821EDE2BA8508BD0AEDAC6E85D947557AF61DE11BB8918803
```


## Introduction
`1.`
For user results, you will need the `Results.txt` file. The file is hashed! However, the data is readable in the program itself.

`2.`
For all usernames and passwords, you will need the `credentials.txt` file, which is also hashed!

`3.`
For all vocabulary words and their translations, you will need the `words_configFile.txt` file, which is not hashed!
> ❕ **Important:**
> If you want to prevent modification by other users (if you plan to distribute the file, for example, on a school network), set the file permissions to Read-only for end users. However, NEVER set the `Results.txt` file as Read-only, otherwise, users' results will not be saved. Set the remaining two files to Read-only only after configuration. If you do this before configuration, you will need to run the program as an admin.

### ⚠️ All of these files are automatically created if missing, so if you care about the contents of any file, you will need to share the file between devices where you want this content to be present ⚠️

## About the project

A project aimed at those who want to practice a foreign language. The file is available on all OS. I hope it helps you with your learning. It is a CLI!
> ⚠️ **Note:**
> The file may have bugs, if you find any, please contact me.

## Description

It would be good to know some basics, for example, the default user is `admin` and the password is `Password`. This model is more complex, so I recommend testing it first before using it in practice.

## Download
Simply click on the project `main.py` and download the so-called "raw file". The program itself will then explain what and how to do.

> ℹ️ **Information:**
> It should be obvious that you will need `Python` to run it.

## Python to Executable

```
pip install pyinstaller
```
`Instalation of pyinstaller`
```
pyinstaller --onefile soubor.py
```
`.Exe file is now located in \dist\file.exe`

