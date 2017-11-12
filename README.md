# recruitr

## Goal
The goal of this app is to help the recruitment process for a company and to manage applicants.

## Requirements

HR representatives should be able to:
- Create some positions to be filled
- Assign skills to positions (marketing, javascript, ruby…)
- Upon receiving a candidate, the recruiter is going to create a candidate profile and match her/him with a the position she/he is applying for
- When the candidate is matched to a position, the recruiters matching the skills are suggested
- The recruiter can then select a datetime, which will create an event through the google calendar API and invite the suggested employee and the applicant

- The recruiter can select an available time slot for a given employee
- The list of potential matching recruiters could be smart, with a score based on:
  - Random, so that everybody participates
  - her/his skills (perfect match, better match, partial match)
  - her/his seniority (number of previously matched applicants)
- Notification system: send a mail to both recruiter and applicant, AngelList-style
- Applicant scorecard, to be filled by company members (HR rep filling the application and recruiters) with specific traits such as experience, dynamism, interest in the company. We could have some sort of radar-graph, with an average from every members

## Expectations

- Release

  - Public Github repo (if you prefer a private one, invite us (`StanBoyet`, `larsbs`) on it beforehand)

- Code

  - Structure

    - The project includes the descibed features but must be open to extension quickly (think about how to abstract common aspects [API calls, Logs, authenticated views, etc.])

  - Documentation

    - Althought code should be self explanatory, a good documentation explaining the most important aspect of the project is required.

    - The documentation includes a point about how to run the project.

    - Especially interesting:

      - Where do you think we could put more effort reviewing the code

      - Which parts are you especially proud about

- Tools

  - Whatever you need, as long as you can explain the added value in your debrief session

  - Use what you're the most efficient with. You'll have plenty of occasion to experiment with other technologies here, as we're always eager to learn

- Bonus

  - Hosted project
    - Heroku or else (if you need a paid tier, ask us to create one for you and to invite you in)
  - Smart decisions, don't reinvent the wheel

## Instructions

You need to install django to run this server so install it with pip :

sudo apt-get install python-pip python-dev build-essential  or sudo brew install python

sudo pip install django

copy your Goolge calendar API key file in JSON format in the root's project then set up the environement variables for email and calendar features :

export SERVICE_ACCOUNT_EMAIL="your_email@gmail.com"

export CLIENT_SECRET_FILE="your_google_API_key.json"

export HOST="smtp.gmail.com"

export PASSWORD="your password"


Enaable your gmail account to be use by a less secure app, sorry ... :
https://myaccount.google.com/lesssecureapps?pli=1

before to run the server for your fisrt time you should feed the database so load data from a json fil suck as

python manage.py makemigrations

python manage.py migrate

python manage.py loaddata file.json


Finally you can run your server:

python manage.py runserver
