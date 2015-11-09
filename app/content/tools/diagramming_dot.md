title: Charting the course with Dot and Graphviz
date: 2015-11-08
task: Diagramming
tool: Dot language / Graphviz

How do you explain a system to other developers before any code has been written? If code is being written, how to you ensure each developer remembers the big picture, and can revise it when necessary? After a system has been built, how do you introduce a non-technical person to your system's raison d'être?

One solution I've often witnessed is dry prose. A developer might create a long, dry text file and forward it as an attachment with no email header. During an on-boarding meeting, he might point out that he sent an email and that he's ready for questions. The non-technical person then might ask, "Can you explain what you mean here in the second line by 'class inheritance'?" It becomes clear this is the meeting from hell. No resolutions are drawn, everyone's time was wasted, and the non-technical participant concludes he hates working with engineers. After three more prose-filled meetings, the project begins, crashes, and burns three weeks later.

The correct solution would have been to draw a picture. If the developer had walked the team through a diagram, the non-technical member might have seen the box reading "Data expected from **Company A**". This same non-technical person might have pointed out that Company A is suing Company C, which will probably mean we'll never get said data. Non-technical participants are often the only people in the room aware of political blockers. By making technical content accessible through a diagram, it becomes much easier to obtain necessary input.

Of course, non-technical participants aren't the only people who benefit from diagrams. I'm fairly certain all developers appreciate the simplicity of a nicely drawn diagram. In a perfect world, every project would be associated with an up-to-date diagram for everyone's reference.

## So then, why you no draw picture?

If people appreciate diagrams so much, why do developers so often neglect them? My guess: developers dislike diagramming because diagrams are not generated with a text editor. After meditating on the subject for a while, I realized that the role of a separate application in diagram generation was literally poison for my creation of diagrams.

* Most people associate diagrams with presentation software
* Presentation software is most-often used and appreciated by non-developers, who enjoy dragging their mouses around the mouse pad
* When I'm forced to leave my text editor and enter with GUI world of non-developers, my soul starts dying
* Therefore, If I had to leave the terminal to generate a diagram, I'd probably just resign myself to cryptic text files and whiteboarding.

## Solution: diagram through code!

Luckily, several months ago, I had a discussion with a budding young project manager. He mentioned that a developer he'd worked with made awesome diagrams, and that he did this through source code. The source files ended in *.dot*, and this guy swore by them for conveying the meaning of his code. This discussion sparked a weekend of searching and experimenting, and I discovered the DOT language.

## DOT language

### Introduction

The [DOT language](https://en.wikipedia.org/wiki/DOT_(graph_description_language)) is programming language, written in a C-like syntax, that compiles to a diagram. It is not particularly hard to use, but finding it was quite the challenge. I've provided two very useful links for you to read more about the language and get started with it. The language documentation is thorough, and pretty much all you're going to get on the subject. DOT language is very well-documented, but your only documentation is in the PDF below.

[Language documentation pdf](http://graphviz.org/pdf/dotguide.pdf)  
[Graphviz - DOT compiler](http://graphviz.org/)

Before providing an example, let me provide a laundry list of reasons why you'll want to make the DOT language, along with Graphviz, your team's only diagramming tool.

1. Free software - keeps the lawyers off like Teflon
* Business friendly - licensed under Eclipse Public License, so keep your GPL fears at bay
* Version controlled like any other software (eg, with git)
* Customizable - expressive language with well-documented features
* Easy to learn - C-like syntax that developers should be comfortable playing with
* Uncorruptible - raw text format will always be recoverable

Based on my research, DOT is the **only** software on the market that satisfies all of my ideal requirements. For diagrams whose main purpose is to get everybody on the same page without hemorrhaging money, DOT is literally the perfect tool.

### Example

My prose about the DOT language is probably fascinating, but I figure an example will help send home the possibilities of this language as a diagramming tool. See below for an example of the DOT language. See below for the rendered image, which shows three groups: Outsiders, the Software Kingdom, and the Land of users. There is no logic to the image itself, but it looks fairly logical. I could probably explain why both Patent Trolls and Breakthroughs are attracted to noobs, but in all honestly, I created this diagram with little thought beyond trying to show the number of shapes and colors one can quickly put together.

![]({{ url_for('static', filename='img/diagramming_dot.png') }})

The image is certainly colorful. With a little imagination, I'm sure you can see yourself putting the content of your software projects in this kind of form. I'm sure it will be much more logical than what I put together.

Although the above image is cool, what is cooler (to me) is that everything was generated through code. Please see the following snippet that can be used to generate the above image:

    :::dot
    digraph kingdom_danger {
        rankdir=LR; /* Diagram goes from left to right */
        node [shape=hexagon style=filled fillcolor=cornsilk color=black];

        /* These are my outsiders */
        OUT1 [label="Outsider 1"];
        OUT2 [label="Outsider 2"];

        /* This is a cluster representing the perils and joy of software */
        subgraph cluster_software_kingdom {
            label = "Software Kingdom" style=filled;
            fillcolor=peachpuff color=black;
            node [shape=trapezium];
            SGF [label="Segfault" fillcolor=lightgray];
            BTR [label="Breakthrough" fillcolor=orangered];
            PTN [label="Patent Troll" fillcolor=plum];
        }

        /* All users gather here, and bask in your freedom */
        subgraph cluster_users {
            label = "Land of users" style=filled;
            fillcolor=gainsboro color=black;
            node [shape=doublecircle];
            HKR [label="Hacker" fillcolor=seagreen];
            NOB [label="Noob" fillcolor=royalblue];
            GMR [label="Gamer" fillcolor=purple];
        }

        /* Relationships between outsiders and the kingdom */
        OUT1 -> BTR;
        OUT1 -> PTN;
        OUT2 -> SGF;

        /* Kingdom and its relationship with users */
        SGF -> HKR;
        SGF -> GMR;
        PTN -> NOB;
        BTR -> NOB;

        /* My fun title */
        labelloc=t;
        label=<<B>Kingdom Danger:</B> Fun times!>;
    }

#### Steps to compile into a viewable image

Pretty nifty, right? If you want to execute this code on your own machine, go to Graphviz's website and follow the instructions on getting a copy for your operating system. If you are using either Linux Mint or Ubuntu, you can probably install the necessary dependencies like this:

    :::bash
    sudo apt-get install graphviz

That's not too had, right? Once you have the necessary dependencies installed, place the DOT language script in a file on your local computer, naming the file *software_kingdom.dot*. Open a terminal and navigate to the same directory as your ".dot" file. Enter the following commands:

    :::bash
    mkdir img
    dot -Tpng software_kingdom.dot -o img/software_kingdom.png

This command will create a .png file in a newly created directory img/. Feel free to get creative and make your own charts; it's quite fun.

## Summary / Conclusion

The DOT language is the perfect tool for creating diagrams. It is:

* Free
* Business-friendly
* Version-controllable
* Customizable
* Easy to learn
* Uncorruptible

So what are you waiting for. Get out there, make some sweet diagrams, and keep your team on the same page.
