# Site Title
## Table of contents

<!--table start-->

- [UX](#UX)
    - [User Stories](#User-Stories)
    - [Strategy Plane](#Strategy-plane)
    - [Scope Plane](#Scope-Plane)
    - [Structure Plane](#Structure-Plane)
    - [Skeleton Plane](#Skeleton-Plane)
    - [Surface Plane](#Surface-Plane)
- [Features](#Features)
    - [Existing Features](#Existing-Features)
    - [Features Left to Implement](#Features-Left-to-Implement) 
- [Technologies Used](#Technologies-Used)
    - [Languages](#Languages)
    - [Tools](#Tools)
    - [Frameworks](#Frameworks)
    - [Libraries](#Libraries)
- [Testing](#Testing)
- [Deployment](#Deployment)
    - [Online Deployment](#Online-deployment)
    - [Offline Deployment](#Offline/Local-Deployment)
- [Credits](#Credits)
    -[Content](#Content)
    -[Media](#Media)
    -[Acknowledgements](#Acknowledgements)
<!--table end-->

![Mock-up](Readme_sourceFiles/mockup.png)
---
 
# UX
## User Stories

## Strategy Plane
### High level considerations

### Business goals 

### Trade Off 

![The Features diagram](Readme_sourceFiles/tradeOff.png)


### The trade off

## Scope Plane

### Trade off

#### Comments

#### Promotion of products

### Requirements

### Requirement types

## Structure Plane
### Concerns

![Structure plane](Readme_sourceFiles/Structure_plane.png)

### Interaction design 

### Information Architecture

### Principals of organisation

## Skeleton Plane

- [Desktop view](Readme_sourceFiles/DesktopWireframe.pdf)

- [Mobile & Tablet view](Readme_sourceFiles/MobileAndTabletView.pdf)

## Surface Plane

![Colour pallet for the site](Readme_sourceFiles/pallet.png)

# Features
 
## Existing Features

## Features Left to Implement

- I would like to make the mobile nav a bit more user friendly for mobile users but due to the number of icons and bootstrap, this will take a lot of time.
- Due to the low traffic and high number of products at the current stage, having 2 users order the last product at the exact same time, is unlikely but I would like to add some defensive programming for that in the future
    - By law the first person who buys the item, gets it. Thus only once a transaction is completed will the stock of the items be ckecked and be reduced by the quantity of that item.
    - Due to time constraints this will have to be implemented once traffic increases.
- Better resolution Photographs

# Technologies Used

## Languages

- [HTML5](https://en.wikipedia.org/wiki/HTML5)
- [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets#CSS_3)
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
- [Pyhton3](https://www.python.org/downloads/release/python-380/)

### Tools

- [Autoprefixer](https://autoprefixer.github.io/)
- [Markup Validation service](https://validator.w3.org/)
- [Pep8 online check](http://pep8online.com/)
- [GitHub](https://github.com/)
- [Git](https://git-scm.com/)
- [Gitpod](https://chrome.google.com/webstore/detail/gitpod-online-ide/dodmmooeoklaejobgleioelladacbeki?hl=en)
- [VSC](https://code.visualstudio.com/download)
- [Microsoft Office](https://www.office.com/)
- [favicon](https://www.favicon.cc/)
- [JSHint](https://jshint.com/)
- [AWS](https://aws.amazon.com/) - specifically S3
- [Stripe](https://stripe.com/)


### Frameworks

- [Bootstrap](https://getbootstrap.com/)
- [Font Awesome icons](https://fontawesome.com/icons?d=gallery)
- [Django](https://www.djangoproject.com/)

The following are frameworks imported from the cheese shop (They can be found in requirements.txt). 
- [Click](https://pypi.org/project/click/)
- [DNSPython](https://pypi.org/project/dnspython/)
- [itsdangerous](https://pypi.org/project/itsdangerous/)
- [Werkzeug](https://pypi.org/project/Werkzeug/)

### Libraries

- [JQuery](https://jquery.com)

# Testing

Due to this section being too long, I have written [a test file](testing.md).

# Deployment

Link to the live page: 
## Online deployment

- First create a [heroku](https://dashboard.heroku.com/apps) account and create a app - The name is up to you: mine was operation-gym. Select a region closest to you - mine was europe
- This assumes you already have a Stripe account. if not create one [here](https://stripe.com/)
- In heroku, under *resources tab* > *Add-ons*, search for postgress and add it. Select Hobby-Dev as your plan - should be free
- Head back to Gitpod and in the terminal run the following lines:
    - remember to install the already listed requirements before freezing or else they will be lost 
    - `pip3 install dj_database_url`
    - `pip3 install psycopg2-binary`
    - `pip3 install gunicorn`
    - freeze the requirements
        - `pip3 freeze --local > requirements.txt`

- In Gitpod go to *Gymshop* > *settings.py* > under the imports add `import dj_database_url`
- Still in *settings.py* > *DATABASES* > add the following code:
```
if "DATABASE_URL" in os.environ:
    DATABASES = {
    'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
}
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
```
- Migrations need to be run again
    - In the terminal type `python3 manage.py makemigrations --dry-run` to test if the migrations are made successfully
    - Then `python3 manage.py makemigrations`
    - Then `python3 manage.py migrate --plan` To see if they are executed properly
    - Then `python3 manage.py migrate` - all should have a *OK* appended to them

- Product data needs to be imported
    - In the terminal type `python3 manage.py loaddata categories.json` followed by `python3 manage.py loaddata products.json`
    - Products depend on categories so order is important

- create a super user
    - In the terminal type `python3 manage.py createsuperuser`
    - follow the prompt in the terminal to create the superuser
        - The login details for this user has been provided in the submission

- Create a Procfile for heroku
    - the context of the file should be `web: gunicorn [Main app].wsgi:application` - my main app is Gymshop

- In the terminal run `heroku login -i` and login to your heroku account through the terminal

- In the terminal run `heroku config:set DISABLE_COLLECTSTATIC=1`
    - this is to prevent heroku from collecting static files

- In Heroku under the setting tab > Config vars > show config vars,  add your variables:
    - DATABASE_URL - Should already by provided by Postgress
    - DEVELOPMENT - Boolean
    - SECRET_KEY - Provided by Django
    - STRIPE_PUBLIC_KEY - Provided by Stripe - "Publishable key" on Stripe dashboard
    - STRIPE_SECRET_KEY - Provided by Stripe - "Secret key" on Stripe dashboard 
    - STRIPE_WH_SECRET - Provided by Stripe - *Developers* > *Webhooks* > add an end point (this will be covered soon) > *Signing secret*
- 

## Offline/Local Deployment

# Credits

## Content
- [Gym Equipment JSON content](https://www.fitandme.com/guide-gym-equipment-names-how-to-use/#tab-con-18)
- [simplifaster](https://simplifaster.com/articles/curved-treadmills-pros-cons/)
- [Flat treadmill](https://www.amazon.com/TOE-Treadmill-Installation-Absorption-Apartment/dp/B08LQPPL5X/ref=sr_1_3?dchild=1&keywords=Small+Treadmill+for+Apartment&qid=1611918688&sr=8-3)

## Media

- [Unsplash](https://unsplash.com/)
- [kaggle](https://www.kaggle.com/dutt2302/gym-equipment?select=gym_data)
- [Json Media](https://www.fitandme.com/guide-gym-equipment-names-how-to-use/#tab-con-18)

## Acknowledgements
- I got the inspiration to make this project as I used some of the styling and functionality applied on it from code institute "Project - [Boutique Ado](https://github.com/KeisGSmit/OnlineShop)"
- The business Logic was inspired by [Gymshark](https://eu.gymshark.com/)
