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
π remove app.run()
π pip install unicorn or add gunicorn==20.1.0 to requirements.txt 
π pip freeze > requirements.txt

# On Render site 
π choose Region Frankfurt (EU Central)
πgunicorn < Python Name >:app


