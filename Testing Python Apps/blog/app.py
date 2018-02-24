from blog import Blog

MENU_PROMPT = 'Enter "c" to create a blog, "l" to list blogs, "r" to read one, "p" to create a post, or "q" to quit: '

blogs = dict() #blog_name : Blog object

def menu():
    #Show the user available blogs
    #Let the user make a choice
    #Do something with that choice
    #Eventually exit

    print_blogs()
    selection = input(MENU_PROMPT)
    while selection != 'q':
        if selection == 'c':
            ask_create_blog()
        elif selection == 'l':
            print_blogs()
        elif selection == 'r':
            ask_read_blog()
        elif selection == 'p':
            ask_create_post()
        selection = input(MENU_PROMPT)

#note: A method is a function inside a Class
#This is a function
def print_blogs():
    for key, blog in blogs.items(): #[(blog_name, Blog), (blog_name, Blog)]
        print('- {}'.format(blog))

def ask_create_blog():
    blog_title = input('Enter the blog title: ')
    blog_name = input('Enter the name: ')
    blogs.append(Blog(blog_title, blog_name))

def ask_read_blog():
    blog_title = input('Enter the blog title: ')

def ask_create_post():
    pass
