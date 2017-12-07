# QwilrTask
Task given by Qwilr

before you run, check that you have installed pip and flask
you can do this by running "pip install pip" and "pip install flask"
you can also run the following commands "sudo apt-get update" and "sudo apt-get upgrade" to make sure you are up to date.

To run the program type "python app.py"
if that does not work, then try "chmod 755 app.py" and then "python app.py"

Q&A
Overall process you went through, any key decisions made.

before coding i used a pen and paper to draw out what i wanted. This included what the webpage would look like and information flow.
After that i Explored the API and once i was done with that, i got to coding.
At first i was stuffing everything into main.html, but then i thought that it would be worth it to spend some time organsing it so that it is more readable. I made it so, that other webpages can extend main and input their own unique information.


Shortcuts, simplifying assumptions, known bugs, etc.

in templates there is an includes folder. this contains common web components and i can use over again in different pages.
one assumption is that the button "buy" and "sell" work. Right now they are just dummy buttons and i thought it would be more important to get the API working in time.
It does not make sense to get the buttons working first, because we need to know what is the value of the stock.
Another shortcut was to use only one stock, in this case bitcoin. it would take a lot of time to implement a system where a user can take which stocks s/he wants to buy. 


What slowed you down, what was unexpected

API, reading through the documentation took way longer than expected. i soon realised that i didn't have to read through the whole thing, but just get what i wanted and use it. 


Any problems you ran into, and how you solved them

API, the first problem was converting the JSON into a dictionary. This took some time.
Then what happened is that the information was no longer orangised. This was because dictionaries do not have order.
accessing and exploring the API was tough to begin with, but i felt more comfort at the end.
