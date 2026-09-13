from bs4 import BeautifulSoup

with open("dm.html", "r") as fd:
    soup = BeautifulSoup(fd, 'html.parser')
    root = soup.html

    # Find list with Mythical

    # Step 1: Go to the body element

    # Could do either of these lines/methods to get the body element
    # e_body = root.body
    e_body = root.find('body')

    # Step 2: Get the unordered lists from the body element
    
    l_e_ul = e_body.find_all('ul')

    # Step 3: Find the ul element that's Mythical!

    e_target_ul = None

    for ul_element in l_e_ul:
        #print(ul_element.getText())
        s_text = ul_element.getText()
        # Use find(), not index().  index() throws an exception if the item
        # isn't found, but find doesn't throw the exception.
        if s_text.find("Mythical") > 0:
            #print("FOUND IT")
            e_target_ul = ul_element
        else:
            #print("nope")
            pass
        #print("------------------------------------")
        
    #print("=====================")
    #print(e_target_ul.getText())

    # Step 4: We have the Mythical <li>, but we need the <ul> contained in
    # it, so grab the <ul> element from the Mythical <li>
    e_mythical_ul = e_target_ul.find('ul')

    ### NOTE #############################################################
    # At this point, you need to start using some more advanced pieces of
    # BeautifulSoup and the internals of how the document is represented.
    # To do that, you need to start reading the documentation  *gasp*   ;)
    #
    # .contents and .children are important:
    # https://www.crummy.com/software/BeautifulSoup/bs4/doc/#contents-and-children
    #
    # Being able to navigate sideways with next_sibling is also important:
    # https://www.crummy.com/software/BeautifulSoup/bs4/doc/#going-sideways
    ######################################################################

    # Step 5: We just want the first child of the li tag containing dragon.
    # The first child is the text itself.  Subsequent items are the remainder of
    # the tag's contents.
    l_mythical_ul_li = e_mythical_ul.find('li')
    iter_guts = l_mythical_ul_li.children
    # Unfortunately, .children gives you back an iterator, rather than a list, so
    # to access the first item (which is what we want), we need to call next on
    # the iterator.
    print((next(iter_guts)).getText().strip())

    # Step 6: Print out the siblings
    while l_mythical_ul_li.next_sibling != None:
        next_sib = l_mythical_ul_li.next_sibling

        # Ignore siblings that are just an empty item
        if next_sib.getText().strip() != "":
            print(next_sib.getText().strip())
        l_mythical_ul_li = next_sib
    
    
