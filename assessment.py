# PART ONE

# 1. We have some code which is meant to calculate an item cost
#    by adding tax. Tax is normally 5% but it's higher in
#    California (7%).

#    Turn this into a function. Your function will pass in
#    the default tax amount (5%), a state abbreviation, and the
#    cost amount as parameters.

#    If the state is California, apply a 7% tax within the function.
#    Your function should return the total cost of the item,
#    including tax.

#    If the user does not provide a tax rate it should default to 5%


def total_item_cost(state, item_cost, tax=0.05):
    """
    Returns the total cost of an item including sales tax. Takes three arguments:
    a float as the tax amount, a string as the state abbreviation,
    and a float as the cost of the item. If no tax amount provided, the default is 5%.

    For example::

        >>> total_item_cost('OR', 49.79, 0.00)
        49.79

        >>> total_item_cost('CA', 99.99)
        106.99

        >>> total_item_cost('MA', 39.99)
        41.99
    """
    floated_item_cost = float(item_cost)

    if state == "CA":
        CA_tax = 0.07
        total_cost = floated_item_cost * (1 + CA_tax)
    else:
        total_cost = floated_item_cost * (1 + tax)

    rounded_total_cost = round(total_cost, 2)

    return rounded_total_cost


#####################################################################
# PART TWO

# 1. (a) Write a function, `is_berry()`, which takes a fruit name as a string
#        and returns a boolean if the fruit is a "strawberry", "cherry", or 
#        "blackberry".


def is_berry(fruit):
    """Takes a string that is the fruit name and returns a Boolean.
    Function returns True if the fruit is 'strawberry', 'cherry', or 'blackberry'.

    For example::

        >>> is_berry('watermelon')
        False

        >>> is_berry('strawberry')
        True

        >>> is_berry('cherry')
        True

        >>> is_berry('blackberry')
        True
    """
    if fruit == 'strawberry' or fruit == 'cherry' or fruit == 'blackberry':
        return True
    else:
        return False

#    (b) Write another function, shipping_cost(), which calculates shipping cost
#        by taking a fruit name as a string, calling the `is_berry()` function 
#        within the `shipping_cost()` function and returns `0` if ``is_berry()
#        == True``, and `5` if ``is_berry() == False``.


def shipping_cost(fruit):
    """Calculates the cost shipping a fruit. Function takes one argument -- 
    the fruit name which is a string.

    For example::

        >>> shipping_cost('strawberry')
        0

        >>> shipping_cost('blackberry')
        0

        >>> shipping_cost('cherry')
        0

        >>> shipping_cost('mango')
        5

        >>> shipping_cost('watermelon')
        5
    """
    if is_berry(fruit) is True:
        total_shipping_cost = 0
    else:
        total_shipping_cost = 5
    return total_shipping_cost

# 2. (a) Write a function, `is_hometown()`, which takes a town name as a string
#        and evaluates to `True` if it is your hometown, and `False` otherwise.


def is_hometown(town):
    """Function takes one string argument as the town to evaluate whether it is
    my hometown or not. My hometown is 'San Jose'. Returns a Boolean.

    For example::

        >>> is_hometown('San Jose')
        True

        >>> is_hometown('San Francisco')
        False

        >>> is_hometown('Boston')
        False

        >>> is_hometown('London')
        False
    """
    lowercase_town = town.lower()

    if lowercase_town == "san jose":
        return True
    else:
        return False

#    (b) Write a function, `full_name()`, which takes a first and last name as
#        arguments as strings and returns the concatenation of the two names in
#        one string.


def full_name(first_name, last_name):
    """Takes two arguments, first name and last name, as strings, and returns the
    conatenation of the two names in one string.

    For example::

        >>> full_name('Catherine', 'Liaw')
        'Catherine Liaw'

        >>> full_name('Benedict', 'Cumberbatch')
        'Benedict Cumberbatch'

        >>> full_name('Olivia', 'Pope')
        'Olivia Pope'
    """
    full_name_result = first_name + " " + last_name
    return full_name_result


#    (c) Write a function, `hometown_greeting()`, which takes a home town, a
#        first name, and a last name as strings as arguments, calls both
#        `is_hometown()` and `full_name()` and prints "Hi, 'full name here',
#        we're from the same place!", or "Hi 'full name here', where are you 
#        from?" depending on what `is_hometown()` evaluates to.


def hometown_greeting(town, first_name, last_name):
    """Takes three string arguments: town, first name, and last name.
    Prints a greeting depending on whether the person is from San Jose or not.

    Examples::

        >>> hometown_greeting('San Jose', 'Charlie', 'Brown')
        Hi, Charlie Brown, we're from the same place!

        >>> hometown_greeting('Chicago', 'Barack', 'Obama')
        Hi, Barack Obama, where are you from?

        >>> hometown_greeting('Washington D.C.', 'Olivia', 'Pope')
        Hi, Olivia Pope, where are you from?
    """
    hometown_result = is_hometown(town)
    full_name_result = full_name(first_name, last_name)

    if hometown_result is True:
        print "Hi, {}, we're from the same place!".format(full_name_result)
    else:
        print "Hi, {}, where are you from?".format(full_name_result)

#####################################################################

# PART THREE

# 1. Write a function ``increment()`` with a nested inner function, ``add()``
#    inside of it. The outer function should take ``x``, an integer which
#    defaults to 1. The inner function should take ``y`` and add ``x`` and ``y`` together.


def increment(x=1):
    """Function takes one integer arguments. If no argument is given,
    the default value is 1.
    """
    def add(y):
        """Nested function that adds the two integer arguments x and y together."""
        return x + y

    #   This problem is worded very confusingly to me. I'm not sure how to create a doctest
    #   for this function because when I test it, it returns None.
    #   I am confused because the outside function increment() only takes one argument x,
    #   but then where does the argument y for add() come from? The add() function is supposed
    #   to add x + y, but there is no value for y coming from the increment() function.


# 2. Call the function ``increment()`` with x = 5. Assign what is returned to a
#    variable name, addfive. Call addfive with y = 5. Call again with y = 20.


    addfive = increment(5)

    #   Again, I do not understand the instructions. When I call increment(5) as written
    #   to how I understand the instructions from #1, the function returns None.
    #   Instructions in #2 then says to call a variable addfive with y = 5. Addfive is not
    #   a function, so it seems odd to "call" a variable.


# 3. Make a function that takes in a number and a list of numbers. It should append
#    the number to the list of numbers and return the list.


def append_to_list(number, list_to_append_to):
    """Appends a number to the end of a list.
    Takes two arguments: a number and a list of numbers. 

    For example::

        >>> append_to_list(3, [1, 2, 3, 4, 5])
        [1, 2, 3, 4, 5, 3]

        >>> append_to_list(99, [342, 234, 753, 3490])
        [342, 234, 753, 3490, 99]
    """
    list_to_append_to.append(number)
    return list_to_append_to
#####################################################################
# END OF PRACTICE: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print