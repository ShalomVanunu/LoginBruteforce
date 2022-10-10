# LoginBruteforce
Http Login Bruteforce
on site :
https://loginbruteforce.onrender.com/

# Setup

this site loaded on https://render.com/ 

the site coded in Flask environment
and deploy as describe :
https://render.com/docs/deploy-flask

# Upload code on Github steps:
📌 remove app.run()
📌 pip install unicorn or add gunicorn==20.1.0 to requirements.txt 
📌 pip freeze > requirements.txt

# On Render site 
📌 choose Region Frankfurt (EU Central)
📌gunicorn < Python Name >:app


