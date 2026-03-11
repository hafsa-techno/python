#include "PhoneBook.hpp"

int PhoneBook::st_index = 0;

PhoneBook::PhoneBook()
{
	index = 0;
}

int PhoneBook::add_contact()
{
    std::string first_name, last_name, nick_name, phone_number, darkest_secret;
	Contact C;
	
	first_name = get_non_empty_input("first name: ", 0);
	if (first_name.empty())
		return (true);
	last_name = get_non_empty_input("last name: ", 0);
	if (last_name.empty())
		return (true);
	nick_name = get_non_empty_input("nick name: ", 0);
	if (nick_name.empty())
		return (true);
	phone_number = get_non_empty_input("phone number: ", 1);
	if (phone_number.empty())
		return (true);
	darkest_secret = get_non_empty_input("dark secret: ", 0);
	if (darkest_secret.empty())
		return (true);
	C.set_first_name(first_name);
	C.set_last_name(last_name);
	C.set_nick_name(nick_name);
	C.set_phone_number(phone_number);
	C.set_darkest_secret(darkest_secret);
	if (st_index == 4)
		st_index = 0;
    if (this->index == 4)
    {
        contacts[st_index] = C;
		st_index++;
        return (false);
    }
    contacts[this->index] = C;
    (this->index)++;
	return (false);
}

Contact PhoneBook::get_contact(int index)
{
	return (contacts[index]);
}

int PhoneBook::search_contact()
{
	int i;
    std::string index;
	int is_exit;

	i = 0;
	do
    {
        std::cout << CYAN << "\tR/Enter index of contact" << std::endl;
        std::cout << "\t > " << RESET;
        is_exit = get_line(&index);
		if (is_exit == true)
			return (true);
        i = stoi(index);
        if (i < 0 || i >= this->index)
            std::cout << LIGHT_RED << "\tInvalid index, try again." << RESET << std::endl;
    } while (i < 0 || i >= this->index);
    std::cout << BOLD_GREEN << "\tFirst Name: " << RESET << contacts[i].get_first_name() << std::endl;
    std::cout << BOLD_GREEN << "\tLast Name: " << RESET << contacts[i].get_last_name() << std::endl;
    std::cout << BOLD_GREEN << "\tNick Name: " << RESET << contacts[i].get_nick_name() << std::endl;
    std::cout << BOLD_GREEN << "\tPhone Number: " << RESET << contacts[i].get_phone_number() << std::endl;
    std::cout << BOLD_GREEN << "\tDarkest Secret: " << RESET << contacts[i].get_darkest_secret() << std::endl;
	return (false);
}

int PhoneBook::display_contacts()
{
    int i = 0;
    std::string index;

	if (!this->index)
	{
		std::cout << "Empty phone book" << std::endl;
		return (false);
	}
    std::cout << BOLD_YELLOW << "\t--------------------------------------------" << std::endl;
    std::cout << "\t      Index|First Name| Last Name| Nick Name" << std::endl;
    std::cout << "\t--------------------------------------------" << RESET << std::endl;
    while (i < this->index)
    {
        d_contact(contacts[i], i);
        i++;
    }
	if (search_contact())
		return (true);
	return (false);
}
