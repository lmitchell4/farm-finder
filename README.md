

![Site Logo](https://github.com/lmitchell4/farm-finder/blob/master/catalog/static/images/logo.png) 
# Farm Finder Catalog Site


Farm Finder is a template for a website that connects people who grow 
their own food with people who are looking for home-grown food items. 
Users can create catalogs with descriptions and images of the items they 
grow and indicate whether each item has a fixed price or whether they are 
open to bartering for items grown by their fellow farmers.



## Overview

The site was built with [Python 2.7.6](https://www.python.org/downloads/) and 
the [Flask](http://flask.pocoo.org/) web development framework. 

The repo includes a Vagrant Virtual Machine (VM) that can be used to run the 
website locally while it is in development. The VM used here is 
based on the Vagrant VM provided in the 
[udacity/fullstack-nanodegree-vm](https://github.com/udacity/fullstack-nanodegree-vm) 
repo. Below are instructions for installing the VM and running the site locally.


### Installation

1. Download and install [Git](https://git-scm.com/downloads)

2. Install [Vagrant]( https://www.vagrantup.com/downloads.html)

3. Install [VirtualBox](https://www.virtualbox.org/wiki/Downloads)

4. Fork and clone this repo


## Running the Site Locally

1. Open a shell and navigate to the newly created catalog directory (the first one containing the file `pg_config.sh`). 
Note that on Linux or Mac you can use a regular terminal instead, but on 
Windows you will need to use the Git Bash shell.

    ```
    $ cd my_path/.../catalog
    ```

2. Launch and log in to the VM by typing:

    ```
    $ vagrant up
    $ vagrant ssh
    ```
    
3. Navigate to the /vagrant directory and run the `runserver.py` script:

    ```
    $ cd /vagrant
    $ python runserver.py
    ```
   
4. Open a web browser and navigate to [http://localhost:5000/](http://localhost:5000/)

5. (Optional) The default installation includes a database called `farmfinder.db` in the 
`/database` directory. If you ever want to regenerate the database, navigate 
to the `/database` directory, delete the old one, and run the script 
`dbsetdup.py` to create an empty database:

    ```
    $ cd .../database
    $ rm farmfinder.db
    $ python dbsetup.py
    ```

    To repopulate the database with the default dummy data, run the `lots_of_farms.py` 
    script:

    ```
    $ python lots_of_farms.py
    ```

6. When you're done using the site code, you can log out of the VM and shut 
it down by typing:

    ```
    $ exit
    $ vagrant halt
    ```
    

### Features

* Users are able to create accounts for multiple farms. Each farm has 
a catalog of the items they grow (with an option to include a photo of 
the item), a farm profile, and an events page 
where they can post information about events they will be attending such 
as farmers' markets.

* Users are able to add, edit, and delete catalog items, profiles, and events 
from farm accounts that they create. They're also able to add and delete 
entire farm accounts.

* Users log in to the site using their Google account.


### To do

* The site is still in development and there are features that don't work 
yet. For example, there is not yet a Discussions page, and the Buy/Barter 
links in the catalogs don't currently do anything.


### License

This project is released under [the MIT License](https://github.com/lmitchell4/alpha-blog/blob/master/LICENSE).

