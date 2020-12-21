# Refresh

Spaced repetition practice for remembering more of what you read.

### How it works

Refresh uses a form of [spaced repetition](https://en.wikipedia.org/wiki/Spaced_repetition) to help you remember all the most important quotes, notes, and big ideas from what you read. In particular, it uses what a variation of the Leitner system in which each flash card progresses through 5 levels of increasingly long spaces between repetition. Failing to remember a card correctly reverts its level back to the beginning. This is depicted graphically here:

![](./public/leitner.png)

Similar to the Anki flashcards system, Refresh determines whether or not a card was answered correctly based on users discretion. The application also allows users to input new cards directly via the GUI. Unlike Anki, however, Refresh is the capability to create new flashcards based on quotes, by auto generating holes in the quote. All aspects of the application were programmed in Python.

### Running Refresh

`python refresh.py`

or

`chmod +x refresh.py`

`./refresh.py`

### Screenshots

#### Home screen

![](./public/home.png)

#### Practice flow

![](./public/front.png)
![](./public/back.png)

#### Adding new cards

![](./public/quick_add.png)
