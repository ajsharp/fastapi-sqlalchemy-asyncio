# What?

A POC to test sqlalchemy asyncio stuff with fastapi. 

# How to use this

You need to be running a postgres database server on localhost:5432, and it needs a database called `fastapitest`.

You can create on by running `createdb fastapitest`

## 1. Install deps

`make install`

## 2. Run the server

`make run`

## 3. Throw a bunch of traffic at it

`make load`