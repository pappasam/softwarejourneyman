# Keyboard Blog - Flask Application

## Introduction

This package contains code for my first Flask application. The application will implement a blog about mechanical keyboards. Flask provides me the opportunity to learn Web Development at a relatively granular level, and a Keyboard blog empowers me to discuss keyboards (which few other people want to discuss with me). The application will be developed at a slow, steady pace. Since the project is still in its infancy, I'll be developing mostly on master. When it matures, so will be version control practices.

## Directory Structure

A great resource I'm using to learn flask is called [Explore Flask][explore_flask_main]. Although there are many resources about Flask (including its source code), few give a clear organizational overview for large projects.

The first good practice is [overall directory structure][expore_flask_organization]. I've organized my directory in a similar manner to what is proposed in the preceding link.

Another good section: [Blueprints][explore_flask_blueprints]. Taking cue from that link's terminology, my keyboard blog is organized according to function. Templates, static files, and views are separated in different folder hierarchies, with the main application at the top.

[explore_flask_main]: https://www.exploreflask.com/
[explore_flask_blueprints]: https://www.exploreflask.com/blueprints.html
[explore_flask_organization]: https://www.exploreflask.com/organizing.html
