# Project Name

[![MIT Licensed](https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square)](./LICENSE)
[![Powered by Modus_Create](https://img.shields.io/badge/powered_by-Modus_Create-blue.svg?longCache=true&style=flat&logo=data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMzIwIDMwMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8cGF0aCBkPSJNOTguODI0IDE0OS40OThjMCAxMi41Ny0yLjM1NiAyNC41ODItNi42MzcgMzUuNjM3LTQ5LjEtMjQuODEtODIuNzc1LTc1LjY5Mi04Mi43NzUtMTM0LjQ2IDAtMTcuNzgyIDMuMDkxLTM0LjgzOCA4Ljc0OS01MC42NzVhMTQ5LjUzNSAxNDkuNTM1IDAgMCAxIDQxLjEyNCAxMS4wNDYgMTA3Ljg3NyAxMDcuODc3IDAgMCAwLTcuNTIgMzkuNjI4YzAgMzYuODQyIDE4LjQyMyA2OS4zNiA0Ni41NDQgODguOTAzLjMyNiAzLjI2NS41MTUgNi41Ny41MTUgOS45MjF6TTY3LjgyIDE1LjAxOGM0OS4xIDI0LjgxMSA4Mi43NjggNzUuNzExIDgyLjc2OCAxMzQuNDggMCA4My4xNjgtNjcuNDIgMTUwLjU4OC0xNTAuNTg4IDE1MC41ODh2LTQyLjM1M2M1OS43NzggMCAxMDguMjM1LTQ4LjQ1OSAxMDguMjM1LTEwOC4yMzUgMC0zNi44NS0xOC40My02OS4zOC00Ni41NjItODguOTI3YTk5Ljk0OSA5OS45NDkgMCAwIDEtLjQ5Ny05Ljg5NyA5OC41MTIgOTguNTEyIDAgMCAxIDYuNjQ0LTM1LjY1NnptMTU1LjI5MiAxODIuNzE4YzE3LjczNyAzNS41NTggNTQuNDUgNTkuOTk3IDk2Ljg4OCA1OS45OTd2NDIuMzUzYy02MS45NTUgMC0xMTUuMTYyLTM3LjQyLTEzOC4yOC05MC44ODZhMTU4LjgxMSAxNTguODExIDAgMCAwIDQxLjM5Mi0xMS40NjR6bS0xMC4yNi02My41ODlhOTguMjMyIDk4LjIzMiAwIDAgMS00My40MjggMTQuODg5QzE2OS42NTQgNzIuMjI0IDIyNy4zOSA4Ljk1IDMwMS44NDUuMDAzYzQuNzAxIDEzLjE1MiA3LjU5MyAyNy4xNiA4LjQ1IDQxLjcxNC01MC4xMzMgNC40Ni05MC40MzMgNDMuMDgtOTcuNDQzIDkyLjQzem01NC4yNzgtNjguMTA1YzEyLjc5NC04LjEyNyAyNy41NjctMTMuNDA3IDQzLjQ1Mi0xNC45MTEtLjI0NyA4Mi45NTctNjcuNTY3IDE1MC4xMzItMTUwLjU4MiAxNTAuMTMyLTIuODQ2IDAtNS42NzMtLjA4OC04LjQ4LS4yNDNhMTU5LjM3OCAxNTkuMzc4IDAgMCAwIDguMTk4LTQyLjExOGMuMDk0IDAgLjE4Ny4wMDguMjgyLjAwOCA1NC41NTcgMCA5OS42NjUtNDAuMzczIDEwNy4xMy05Mi44Njh6IiBmaWxsPSIjRkZGIiBmaWxsLXJ1bGU9ImV2ZW5vZGQiLz4KPC9zdmc+)](https://moduscreate.com)

Project description - one or two paragraphs. The enemy is dark and creates major problems. The solution is now available and the World can rejoice.

- [Getting Started](#getting-started)
- [How it Works](#how-it-works)
- [Developing](#developing)
  - [Prerequisites](#prerequisites)
  - [Testing](#testing)
  - [Contributing](#contributing)
- [Modus Create](#modus-create)
- [Licensing](#licensing)

# Getting Started

Setup a Python 3 based environment using a virtual env.
Ensure you have pip installed for Python 3.
Fork this GitHub repository.
Clone the forked repository.

Edit the .gitignore file and include the exclusions for the types of 
files, you typically find in a python project, which should not be commited
to GitHub.

Once you have completed these steps, you will be ready to start the project. 

# Background

We want to build a proof of concept project that consists of a command line tool
for generating some of the files needed by the project and the project itself,
a Django website.

The command line tools will take care of important tasks such as:

1. Checking if the project name is a palindrome
2. Providing help to the user
3. Converting YAML into JSON, just incase our engineers prefer to use JSON cloud formation templates.
4. Building out all the basic skeleton files of a Django site 

We're going to start with Part 1 of the project, which is the command line tools. 


# Part 1

In this task we will using the part1 directory as a project to experiment with the 
commandline and file manipulation, in order to show a PoC for generating Django projects.

Your first task will be to figure out how to install the part1 directory via 
pip into your local virtual environment. 

Once this is done, you can move onto these requirements, provided by the Project Manager.

## Requirement 1

Go ahead and run the installed code.

Once the project is started, it should print out the message:

```
This is our Django project generator tool set.
```

The project manager noticed something isn't right, buyt the junior engineer isn't sure why it isn't working.

Your first task is to fix this. The message is there, but something isn't working as expected!


## Requirement 2

We now need to add some flags to our project to handle user input from the commandline.

First we want to add a help flag. When the user parses in the help flag it should print the following message

```
Thank you for asking for help. These tools are used to generate a Django project and convert ClloudFormation code from YAML to JSON.
```

This should help users of the tool know what it is for. The PM doesn't mind how you handle the flag, jsut use the best tools available in Python for the job. 


## Requirement 3

The PM has been told by management, that all rpojects going forwward should have names that are palindromes. He thought it might be helpful, to allow engineers to check if the project name is a palindrome before creating it.

He's decided to call this project tacocat.

Add in a new flag that handles this requirement.

## Requirement 4

The DevOps team spoke to the PM and mentioned that in the future, they would like to host this project on AWS. It's not a huge concern right now, but some DevOps engineers have complained that they prefer to use JSON rather than YAML, and would like projects to have the ability to convert YAMl files to JSON if requested. 

There is a YAML file in this repository containing a snippet of Cloud Formation code. We now want to add a flag that takes this YAML file as input.
Once the file is input it should convert the contents into a JSON object and output it to a new file 
called tacocat_cf.json

You can use the following document as a guide to what the output might look like in JSON format:

https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/quickref-ec2.html

## Requirement 5

We can now check if our project is palindrome. We've also got the basics for converting YAML to JSON (just incase we want to maintain our CF templates as JSOn rather than YAML).

We now need to add a command line task, to create a new Django project skeleton called tacocat in the part2 folder.

So go ahead and add this, and make sure it generates a new project called tacocat! You might want to pass in the project name from the commandline, and maybe even re-use your palindrome function, to see if it is a valid name!

Once done, all the basic files needed to start a Django project should be present in the part2/tacocat folder (where tacocat is the project name)

This is deliverbale 1. The PM is exc ited you have made so much progress. It's now time to build out a basic site.


Part 2.

Setting up Django.



  




# Modus Create

{replace PROJECT_NAME in links below with the name of this project}

[Modus Create](https://moduscreate.com) is a digital product consultancy. We use a distributed team of the best talent in the world to offer a full suite of digital product design-build services; ranging from consumer facing apps, to digital migration, to agile development training, and business transformation.

<a href="https://moduscreate.com/?utm_source=labs&utm_medium=github&utm_campaign=PROJECT_NAME"><img src="https://res.cloudinary.com/modus-labs/image/upload/h_80/v1533109874/modus/logo-long-black.svg" height="80" alt="Modus Create"/></a>
<br />

This project is part of [Modus Labs](https://labs.moduscreate.com/?utm_source=labs&utm_medium=github&utm_campaign=PROJECT_NAME).

<a href="https://labs.moduscreate.com/?utm_source=labs&utm_medium=github&utm_campaign=PROJECT_NAME"><img src="https://res.cloudinary.com/modus-labs/image/upload/h_80/v1531492623/labs/logo-black.svg" height="80" alt="Modus Labs"/></a>

# Licensing

This project is [MIT licensed](./LICENSE).
