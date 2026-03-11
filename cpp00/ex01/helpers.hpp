#ifndef HELPERS_HPP
#define HELPERS_HPP

#include "Contact.hpp"

// helpers
bool get_line(std::string *str);
int stoi(std::string str);
void d_field(std::string str);
void d_contact(Contact contact, int i);
int is_str_empty(std::string str);
std::string get_non_empty_input(std::string prompt, int f);

#endif