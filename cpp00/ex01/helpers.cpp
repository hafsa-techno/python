#include "PhoneBook.hpp"

//function tha converts from string to integer
int stoi(std::string str)
{
    int i = 0;
    int res = 0;
    int len = 0;

    if (str[i] == '+')
    {
        i++;
        len++;
    }
    while (str[i] >= '0' && str[i] <= '9' && str[i])
    {
        res = res * 10 + (str[i] - '0');
        i++;
        len++;
    }
    if (str[i] || len > 14)
        return (-1);
    return (res);
}

//get_line with handling cltr+D
bool get_line(std::string *str)
{
	if (!getline(std::cin, *str))
			return true;
	return (false);
}

// display a field of a contact in the PhoneBook
void d_field(std::string str)
{
    int i = 0;
    int len = 10 - (int)str.length();
    if (len < 0)
    {
        std::cout << str.substr(0, 9) << ".";
    }
    else
    {
        while (i++ < len)
            std::cout << " ";
        std::cout << str;
    }
}

// display a single contact
void d_contact(Contact contact, int i)
{
    std::cout << "\t";
    std::cout << "          " << i << "|";
    d_field(contact.get_first_name());
    std::cout << "|";
    d_field(contact.get_last_name());
    std::cout << "|";
    d_field(contact.get_nick_name());
    std::cout << std::endl << "\t--------------------------------------------" << std::endl;
}

//check if the field is empty
int is_str_empty(std::string str)
{
    int i = 0;
    if (str.empty())
        return (1);
    while (isspace(str[i]) && str[i])
        i++;
    if (!str[i])
        return (1);
    else
        return (0);
}

// get non empty field
std::string get_non_empty_input(std::string prompt, int f)
{
	std::string str;
	bool is_exit;

    do
    {
        std::cout << CYAN << "\t" << prompt << RESET << std::endl;
        std::cout << CYAN << "\t > " << RESET;
        is_exit = get_line(&str);
		if (is_exit == true)
			return ("");
        if (f && stoi(str) == -1)
        {
            std::cout << LIGHT_RED << "\tInvalid number" << RESET << std::endl;
            f = 1;
        }
        else
			f = 0;
		if (is_str_empty(str))
            std::cout << LIGHT_RED << "\tEmpty Field" << RESET << std::endl;
    } while (is_str_empty(str) || f);
    return (str);
}
