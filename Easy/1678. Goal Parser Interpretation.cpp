#include <iostream>
#include <string>

class Solution {
public:
    string interpret(string command) {
        string interpreted = "";
        for (int i = 0; i < command.length(); ++i) {
            if (command[i] == 'G') {
                interpreted += 'G';
            } else if (command[i] == '(' && command[i + 1] == ')') {
                interpreted += 'o';
                ++i;
            } else if (command[i] == '(' && command[i + 1] == 'a' && command[i + 2] == 'l' && command[i + 3] == ')') {
                interpreted += "al";
                i += 3;
            }
        }
        return interpreted;
    }
};