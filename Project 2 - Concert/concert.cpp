#include "concert.h"
#include <vector>
#include <string>
#include <ctime>
#include <iostream>

concert::concert() : concertName(), friends(), desire(), date() {}

concert::concert(std::string name, std::vector<std::string> bringing, int need, std::tm when) : concertName(name), friends(bringing), desire(need), date(when) {}

bool concert::operator<(const concert::concert& other) const {
	printf("Yo.");
	return true;
}


std::string concert::printConcert(){
	std::string result = "";

	result += "The concert is for: ";
	result += concertName;

	result += "\nThe friends you have coming are: "; 
	int counter = 0;
	std::vector<std::string>::iterator it; 
	for(it = friends.begin(); it != friends.end(); it++,counter++){
		result += friends[counter];
		result += ", ";
	}
	
	result += "\nYour desire to go is: ";
	result += std::to_string(desire);
	result += "/10";

	result += "\nThis concert happens on: ";
	if((std::to_string(date.tm_mon)).length() <= 1) result += "0";
	result += std::to_string(date.tm_mon);
	result += "/";
	if((std::to_string(date.tm_mday)).length() <=1) result += "0";
	result += std::to_string(date.tm_mday);
	result += "/";
	result += std::to_string(date.tm_year);
	result += "\n";
			
	return result;
}


int main(){

	//Main concert we will use
	concert::concert a;

	//Vector of concerts 
	std::vector<concert> v;

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
	date.tm_year = 2017;
	date.tm_mon = 1;
	date.tm_mday = 3;

	//Desire should be hard coded?
	
	a.setVenue(vampireWeekend);
	a.addFriend(ashley);
	a.addFriend(rachael);
	a.setDate(date);
	a.setDesire(10);

	v.push_back(a);

	int counter = 0;
	std::vector<concert::concert>::iterator it; 
	for(it = v.begin(); it != v.end(); it++,counter++){
		std::cout << v[counter].printConcert() <<std::endl;
	}
	
	return 0;

}
