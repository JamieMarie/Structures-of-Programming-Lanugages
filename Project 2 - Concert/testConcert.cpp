#include "concert.h"
#include<vector>
#include<string>
#include<iostream>

int main(){

	//Main concert we will use
	concert a;

	//Vector of concerts 
	std::vector<concert> v(10);

	//Making options for concert names
	std::string vampireWeekend = "Vampire Weekend";
	std::string fun = "Fun";
	std::string passionPit = "Passion Pit";
	std::string lumineers = "The Lumineers";

	//Making options for friends (if I had any)
	std::string ashley = "Ashley Cefali";
	std::string rachael = "Rachael Stites";
	std::string gaelen = "Gaelen McIntee";
	std::string natalie = "Natalie Rodriguez";

	//Making options for dates
	std::tm date;
	date.tm_year = 117;
	date.tm_mon = 1;
	date.tm_mday = 3;

	//Desire should be hard coded?
	
	a.setVenue(vampireWeekend);
	a.addFriend(ashley);
	a.addFriend(rachael);
	a.setDate(date);
	a.setDesire(10);

	std::cout << "help" << std::endl;

	std::cout << a.printConcert() << std::endl;
	
	return 0;

}
