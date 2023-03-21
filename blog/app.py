blogs = dict() # blog_name: Blog object

def menu():
    # Show the user available blogs
    # Let the user make a choice
    # Do sum' with that choice
    # Exit

    print_blogs()

def print_blogs():
    # Print the available blogs
    for key, blog in blog.items():
        print('- {}'.format(blog))