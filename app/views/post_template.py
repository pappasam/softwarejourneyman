import os
from flask import render_template
from ..flask_extensions import pages

def posts_post_init(blueprint, blueprint_name):
    '''Factory function that initializes standard blog templates'''

    @blueprint.route('/posts/')
    def posts():
        posts = [p for p in pages if p.path.startswith(blueprint_name)]
        posts.sort(key=lambda item:item['date'], reverse=True)
        template = os.path.join(blueprint_name, 'posts.html')
        return render_template(template, posts=posts)

    @blueprint.route('/posts/<name>/')
    def post(name):
        post_path = os.path.join(blueprint_name, name)
        post = pages.get_or_404(post_path)
        template = os.path.join(blueprint_name, 'post.html')
        return render_template(template, post=post)

    return posts, post
