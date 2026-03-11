#include <iostream>

void str_upper(char *str)
{
	int i;

	i = 0;
	while (str[i])
	{
		std::cout << (char)toupper(str[i]);
		i++;
	}
}

int main(int ac, char *arv[])
{
	int i;

	i = 1;
	if (ac < 2)
	{
		std::cout << "* LOUD AND UNBEARABLE FEEDBACK NOISE *" << std::endl;
		return (1);
	}
	while (i < ac)
	{
		str_upper(arv[i]);
		i++;
	}
	std::cout << std::endl;
	return (0);
}
