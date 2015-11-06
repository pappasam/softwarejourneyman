# Software Journeyman

This package contains code for [softwarejourneyman.com](software_journeyman). It is implemeneted in Flask and deployed using Amazon Elastic Beanstalk.

The application uses the underlying filesystem as a database through the extension Flask-Flatpages. For this reason, it does not use a database to serve dynamic content and can be viewed as a "static" blog, updated at its author's leisure. The entire website is available in open source format in hopes that its structure can be helpful for others beginning their exploration of web development in Flask.

[software_journeyman]: http://www.softwarejourneyman.com/
