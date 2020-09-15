class Solution {
public:
    int myAtoi(string str) {
        // match [+-]?\d+
        // state0 -> state0 if char!=+ or - or \d
        // state0 -> state1 if char==+ or -
        // state0 -> state2 if char==\d
        // state1 -> state3 if char!=\d
        // state1 -> state2 if char==\d
        // state2 -> state2 if char==\d
        // state2 -> state3 if char!=\d
        
        // wierd test case : +-2 -> I design to parse -2 , but exp is 0(wrong format)
        
        
        int     state=0;
        int     i;
        int     answer=0, answer_old=0;
        char    sign='+';
        
        
        for(i=0; i<str.size(); i++){
            if(state==3) break;
            
            switch(state){
                case 0:
                    if(str[i]>='0' && str[i]<='9'){
                        answer = str[i]-'0';
                        state=2;
                    }else if(str[i]=='+' || str[i]=='-'){
                        sign = str[i];
                        state=1;
                    }else if(str[i]!='+' && str[i]!='-' && !(str[i]>='0' && str[i]<='9') && str[i]!=' '){
                        state = 3;
                    }
                    else{
                        answer = 0;
                        sign = '+';
                        state=0;
                    }
                    break;
                case 1:
                    if(str[i]>='0' && str[i]<='9'){
                        if(sign=='+' && answer<0) answer = -answer;
                        else if (sign=='-' && answer>0) answer = -answer;
                        
                        answer_old = answer;
                        
                        answer = answer*10;
						if(answer/10 != answer_old){
                       		if(answer_old>0) 		return INT_MAX;
                        	else if(answer_old<0) 	return INT_MIN;  

						}
                        
                        
                        if(answer_old>=0)   answer += str[i]-'0';
                        else            answer -= str[i]-'0';
                        
                        if(answer_old>0 && answer<0) return INT_MAX;
                        else if(answer_old<0 && answer>0) return INT_MIN;
                        
                        state=2;
                    }else{
                        state=3;
                    }
                    break;
                case 2:
                    if(str[i]>='0' && str[i]<='9'){
                        if(sign=='+' && answer<0) answer = -answer;
                        else if (sign=='-' && answer>0) answer = -answer;  
                        
                        answer_old = answer;
                        
                        answer = answer*10;
						if(answer/10 != answer_old){
                       		if(answer_old>0) 		return INT_MAX;
                        	else if(answer_old<0) 	return INT_MIN;  

						}
                        
                        if(answer_old>=0)   answer += str[i]-'0';
                        else            answer -= str[i]-'0';
                        
                        if(answer_old>0 && answer<0) return INT_MAX;
                        else if(answer_old<0 && answer>0) return INT_MIN;  
                        
                        state=2;
                    }else{
                        state=3;
                    }
                    break;
                default:
                    break;
            }
        }
        //
        if(sign=='+' && answer<0) answer = -answer;
        else if (sign=='-' && answer>0) answer = -answer;  
        
        return answer;
    }
};
