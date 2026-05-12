struct car {
    int speed;
    int position;
};

class Solution {
public:
    int carFleet(int target, vector<int>& position, vector<int>& speed) {
        // We want a struct for cars 
        // We want a vector to stor these cars according to their distance
        // We get a stack and loop backwards on the stored cars 
        // we check the last car on the stack and if the arrival time of that car is less than ours we add ourselves to stack. 
        // We return the number of cars in stack. 
        std::vector<car> sortedCars;
        int n = position.size();
        for (int i = 0; i< n; i++) {
            car newCar{speed[i], position[i]};
            sortedCars.push_back(newCar);
        }
        std::sort(sortedCars.begin(), sortedCars.end(), [](car a, car b){
            return a.position < b.position;
        });

        std::stack<car> fleet; 
        for (int i=n-1; i>=0; i--) {
            car currCar = sortedCars[i];
            if (!fleet.empty()) {
                car lastCar = fleet.top();
                float arrivalTimeLastCar = (target - lastCar.position) / (lastCar.speed * 1.0);
                float arrivalTimeCurrCar = (target - currCar.position) / (currCar.speed * 1.0);
                if (arrivalTimeCurrCar > arrivalTimeLastCar) fleet.push(currCar);
            } else {
                fleet.push(currCar);
            }
        }

        return fleet.size();

    }
};
