# Upcoming Events

Find the upcoming events in your area.

![LCO Mascot](https://i.ibb.co/7CB20mV/Evenbrite-functions.png "LCO")

Liked Events Page

![LCO Mascot](https://i.ibb.co/YfSt9t2/Liked-Events.png"LCO")

Add Events

![LCO Mascot](https://i.ibb.co/9GNHDXj/add-event.png"LCO")


### Features

* User can post events

* User can like the events and see them in the liked page.

* Separated requirements files


# Getting Started

First clone the repository from Github and switch to the new directory:

    $ git clone git@github.com/Yogeshshirsath01/UpcomingEvents
    $ cd {{ Upcoming Events }}
    
Activate the virtualenv for your project.
    
Install project dependencies:

    $ pip install -r requirements.txt
    
    
Then simply apply the migrations:

    $ python manage.py migrate
    

You can now run the development server:

    $ python manage.py runserver
