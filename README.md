![Main image](https://github.com/Jak0ub/Jak0ub/blob/main/translator.png)
`Compatible with Unix and Windows based systems`
## SHA-256
```SHA-256
9BB343B4834FF66A83553193E5DCD01CA2F62E53CAFB95935F8F4DB3DE55BAF2
```
> ⚠️ **Recomendation:**
> Change your admin password to avoid possible session hijacking

---

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

---

## Download
Simply click on the project `main.py` and download the so-called "raw file". The program itself will then explain what and how to do.

> ℹ️ **Information:**
> It should be obvious that you will need `Python` to run it.

---

## Changelog

`!` `You are now able to write whole sentences with commas.`

`!` `You are now able to set [Lang from] and [Lang to] OR you can select both, so you have randomized word from randomized language`

`!` `You can now double-encrypt your credentials file and secure your program, allowing it to be unlocked only with a password you set up.`

`!` `You will now be cooldowned for false login attempts.`

`!` `You are now able to save persistent cookie(active for 30min!). This means that after terminating the program and launching it again, you will still be logged in!`

`!` `You are now able to get 1/2 points for one wrong letter(typo).`


---

## Python to Executable

```
pip install pyinstaller
```
`Instalation of pyinstaller`
```
pyinstaller --onefile soubor.py
```
`.Exe file is now located in \dist\file.exe`

