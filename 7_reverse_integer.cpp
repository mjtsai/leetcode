class Solution {
public:
    int reverse(int x) {
        int sign=0;
        vector<int> rev;
        int x_old;
        
        
        if(x<0){
            sign = 1;
            x = -x;
        }
        
        while(x/10 != 0){
            rev.push_back(x%10);
            x = x/10;
        }
        rev.push_back(x%10);
        
        x = 0;
        x_old = 0;
        while(!rev.empty()){
            x_old = x;
            x = x*10 + rev.front();
            rev.erase(rev.begin());
            
            if(x/10 != x_old){
                x = 0;
                break;
            }
        }
        
        x = x * ((sign)?-1:1);
        
        return x;
    }
};
