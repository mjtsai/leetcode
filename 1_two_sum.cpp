class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int i, j;
        int tmp;
        vector<int> answer;
        

        //
        for(i=0; i<nums.size(); i++){
            for(j=i+1; j<nums.size(); j++){
                if((nums[i]+nums[j]) == target){
                    answer.push_back(i);
                    answer.push_back(j);
                    return answer;
                }
            }
        }
        return answer;
    }
};
