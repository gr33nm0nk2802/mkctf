# mkctf

## Why ?

This tool might help your team to create challenges following a predefined format.

##  Origins

This project was, initially, created for managing file for INS'hAck 2017 event.
You can find challenges and writeups of the past editions of INS'hAck [here](https://github.com/InsecurityAsso).

This project was updated for INS'hAck 2018 event.

Version [1](https://github.com/koromodako/mkctf/releases/tag/1.0.0) was used until INS'hAck 2019.

INS'hAck 2019 will be using version [5.x.x](https://github.com/koromodako/mkctf/releases/tag/5.2.1) or above.

## Minimal requirements

 + `Python 3.7.x`

## Getting started

```
bash -c "$(curl -fsSL https://raw.githubusercontent.com/koromodako/mkctf/master/scripts/install.sh)"
```

You might need to add `~/bin` to your `$PATH` (most of the time you just reload `.profile`)

Then lets say you want to create a CTF for INS'hAck 2019:

```
mkdir inshack-2019
cd inshack-2019
mkctf-cli init
```

Follow the instructions.

You need help: `mkctf-cli -h`

## What you need to understand

`mkctf-cli` helps you manipulate two CTF concepts described bellow. These objects
rely on YAML configuration files.

`mkctf-serve` starts a web server exposing an API which _will be documented here soon_.

### Repository

Represents a collection of categories which contain instances of `Challenge`.

**How is it configured?**

```
tags: [bugbounty, crypto, for, misc, prog, pwn, re, web, quest]
difficulties: [trivial, easy, medium, hard, extreme]
directories:
  public: [public-files]
  private: [server-files, exploit, src]
files:
  build: build
  deploy: deploy
  status: exploit/exploit
  chall_conf: .mkctf.yml
  description: public-files/description.md
  txt: [writeup.md, Dockerfile]
flag:
  prefix: 'INSA{'
  suffix: '}'
name: INS'hAck 2019
```

+ `tags`: tags used to classify CTF challenges
+ `difficulties`: difficulties used to classify CTF challenges
+ `directories`: folders to be created for each challenge
    + `public`: exportable folders
    + `private`: non-exportable folders
+ `files`: files to be created for each challenge
    + `build`: a _script_ building the challenge from sources (cf. Scripts)
    + `deploy`: a _script_ deploying the challenge (cf. Scripts)
    + `status`: a _script_ testing the _exploitability_ of the challenge. It's usually an exploit (cf. Scripts)
    + `description`: a _text file_ describing the challenge
    + `chall_conf`: challenge configuration file name usually `.mkctf.yml`
    + `txt`: list of non-executable mandatory files
+ `flag`: flag properties
    + `prefix`: flag's prefix, usually ends with `{`
    + `suffix`: flag's suffix, usually a single `}`
+ `name`: CTF's name

### Challenge

Represents a CTF challenge.

**How is it configured?**

```
tags: [for, crypto]
enabled: false
flag: INSA{[redacted]}
name: Virtual Printer
parameters: {}
points: 100
slug: virtual-printer
difficulty: trivial
standalone: false
static_url: https://ctf.insecurity-insa.fr/virtual-printer.zip
company_logo_url: https://insecurity-insa.fr/favicon.ico
```

+ `tags`: challenge tags
+ `enabled`: is the challenge enabled?
+ `flag`: challenge flag
+ `name`: challenge name
+ `parameters`: _dict_ of challenge-specific parameters
+ `points`: challenge value
+ `slug`: challenge slug (should match challenge folder name)
+ `difficulty`: challenge difficulty
+ `standalone`: is the challenge standalone? (meaning it does not rely on a server)
+ `static_url`: URL of the archive containing challenge data
+ `company_logo_url`: URL of a logo for a sponsor challenge   

### Scripts

Scripts like `build`, `deploy` and `status` are expected to behave according to the following rules:

1. a _script_ **shall not take mandatory arguments**
2. a _script_ **shall execute before a timeout is triggered** which defaults to 60 seconds. `--timeout` option enable you to override this value
3. a _script_ **shall return a code** which will be interpreted according to the following table:

| **exit code** | **status** | **description** |
|:-------------:|:----------:|:----------------|
| `0` | `SUCCESS` | Script succeeded. |
| `2` | `N/A` | Script does not apply/have a meaning to this challenge. |
| `3` | `MANUAL` | Script cannot perform this task entirely, you will have to get your hands dirty. |
| `4` | `NOT IMPLEMENTED` | Script is not implemented. |
| _other values_ | `FAILURE` | Script failed. |

The special status `TIMED-OUT` may occur if your script took too long to execute as explained in `2.`

If the **exit code differs from 0** both _stdout_ and _stderr_ will be printed out.

You can use this behavior to print meaningful instructions/exceptions within these _scripts_ (particularly interesting if your script returns a code `3 (MANUAL)`)
