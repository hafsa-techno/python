#ifndef PHONEBOOK_H
# define PHONEBOOK_H

# include "Colors.hpp"
# include "helpers.hpp"
# include <iostream>
# include <stdlib.h>

// Phone Book class
class PhoneBook
{
private:
	int index;
	static int st_index;
	Contact contacts[4];

public:
	PhoneBook();
	int add_contact();
	int display_contacts();
	int search_contact();
	Contact get_contact(int index);
};

#endif
