from pyscript import document


def candidate_checker(e):
   club_members = ["czarina lodronio" , "bjorn atendido" , "ezra lazo" , "ruzia cruz" , "eyana mendoza"]


   f_name = document.getElementById('first_name').value
   l_name = document.getElementById('last_name').value
   candidate = f_name + ' ' + l_name
   member_checker = candidate.lower() in club_members


   messages = (f'Sorry {candidate}, your name is not on the list.',
               f'Congratulations {candidate}, you are part of the Volleyball Varsity!')
  
   document.getElementById('result').innerHTML = messages[member_checker]