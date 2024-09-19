## SHA-256
```SHA-256
02499DBF14A32329C30636F1A2BE2C865D7BD921BF3AF32CEE3C21754F2C3AB5
```


## Introduction
`1.`
For user results, you will need the `Results.txt` file. The file is hashed! However, the data is readable in the program itself.

`2.`
For all usernames and passwords, you will need the `credentials.txt` file, which is also hashed!

`3.`
For all vocabulary words and their translations, you will need the `words_configFile.txt` file. It is not hashed!
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

