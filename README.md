# ChatBot
This is an experimental ChatBot which uses the simple frequentist algorithm to guess whether a user has a Covid-19 or got Cold. 
The methodology used works based on the proportions. The user inserts the query and based on the words matching with beforehand configured vocabulary calculate the <br>
of match cases and divides it over the length of the words within teh message. The proportion given the ratio is being compared with the other vocabulary of (Covid Symptoms) <br>
Whichever has the highest score will be returned to the user <br>
## Potential imrpovements
Each case can be described in a different way. <br>
-Among which some cases are described with reverse meaning "non". Ex: Non ho la febbre, non sento il gusto. (I don't have a fever, I don't feel the taste), Some penality can be thought for it <br>
-Some words with the same root can be used in different ways. "Non smetto di starnutire", "Starnutisco" , "Starnuto" Instead of specifying each word, the regex can be written. On sql it could be done with <b>like %starnut%<b/>
