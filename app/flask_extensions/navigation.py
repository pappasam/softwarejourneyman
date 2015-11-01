from flask_nav import Nav
from flask_nav.elements import Navbar, View

topbar = Navbar('',
        View('Home', 'index.main_index'),
        View('Present', 'present.posts'),
        View('One tool', 'tools.posts'),
        View('Avoidable bugs', 'bugs.posts'),
        View('Human error', 'error.posts'),
        )

nav = Nav()
nav.register_element('top', topbar)
