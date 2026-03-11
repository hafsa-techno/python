#include "PhoneBook.hpp"
int	main(void)
{
	PhoneBook	P;
	std::string operation;
	bool is_exit;

	while (true)
	{
		std::cout << BOLD_YELLOW << "Choose an operation" << RESET << std::endl;
		std::cout << BOLD_GREEN << "\tADD" << RESET << " " << BOLD_BLUE << "SEARCH" << RESET << " " << BOLD_RED << "EXIT" << RESET << std::endl;
		std::cout <<" > ";
		is_exit = get_line(&operation);
		if (is_exit || operation == "" || operation == "EXIT")
			return (0);
		if (operation == "ADD")
		{
			if (P.add_contact())
				break ;
		}
		else if (operation == "SEARCH")
		{
			if (P.display_contacts())
				break ;
		}
	}
	return (0);
}
