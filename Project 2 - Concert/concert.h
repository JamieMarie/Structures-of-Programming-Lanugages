#ifndef __H_CONCERT__
#define __H_CONCERT__
#include <string>
#include <vector>
#include <ctime>

class concert{
	private:
		std::string concertName;
		std::vector<std::string> friends;
		int desire; 
		std::tm date;

	public:
		concert();
		concert(std::string concertName, std::vector<std::string> friends, int desire, std::tm date);
		bool operator<(const concert& other) const;
		void setVenue(std::string venue){
			concertName = venue;
		}
		void addFriend(std::string newFriend){
			friends.push_back(newFriend);
		}
		void setDesire(int level){
			desire = level;
		}
		void setDate(std::tm time){
			date = time;
		}
		std::string printConcert();
};

#endif
