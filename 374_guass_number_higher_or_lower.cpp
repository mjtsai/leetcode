// Forward declaration of guess API.
// @param num, your guess
// @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
int guess(int num);

class Solution {
public:
    int guessNumber(int n) {
        long min_pivot = 1;
        long max_pivot = n;
        int result;
        
        while(1){
            result = guess((min_pivot+max_pivot)/2);
            if(result==0) break;
            
            
            if(max_pivot-min_pivot == 1){
                if(guess(min_pivot)==0){
                    max_pivot = min_pivot;
                    break;
                }
                if(guess(max_pivot)==0){
                    min_pivot = max_pivot;
                    break;
                }
            }else{
                if(result == -1){
                    max_pivot = (min_pivot+max_pivot)/2;
                }else if(result == 1){
                    min_pivot = (min_pivot+max_pivot)/2;
                }
            }
        }
        
    
        return (min_pivot+max_pivot)/2;
    }
};
