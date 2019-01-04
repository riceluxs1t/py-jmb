#include <iostream>

#include <algorithm>

#include <string>

#include <cstring>

using namespace std;



const int INF = 987654321;

int cache[10000];

string num;



//num[a..b] 구간의 난이도 반환

int getRank(int start, int end)

{

        //숫자 조각 가져옴

        string part = num.substr(start, end - start + 1);

        //첫 글자만으로 이루어진 문자열과 같으면 난이도 1

        if (part == string(part.size(), part[0]))

               return 1;

        //등차수열 여부

        bool progressive = true;

        for (int i = 0; i < part.size() - 1; i++)

               if (part[i + 1] - part[i] != part[1] - part[0])

                       progressive = false;

        //등차수열이고 공차가 1 혹은 -1이면 난이도 2

        if (progressive && abs(part[1] - part[0]) == 1)

               return 2;

        //두 수가 번갈아 등장하는지 확인

        bool alternate = true;

        for (int i = 0; i < part.size(); i++)

               if (part[i] != part[i % 2])

                       alternate = false;

        if (alternate)

               return 4; //번갈아가며 등장하는 숫자

        if (progressive)

               return 5; //등차 수열을 이루고 공차가 1 아님

        return 10; //그 외 숫자

}



//수열 num[idx..]을 외우는 방법 중 난이도의 최소 합 출력

int memorize(int idx)

{

        //기저 사례:수열의 끝에 도달할 경우

        if (idx == num.size())

               return 0;

        //동적계획법

        int &result = cache[idx];

        if (result != -1)

               return result;

        result = INF;

        for (int i = 3; i <= 5; i++) //길이는 3부터 5 사이

               if (idx + i <= num.size())

                       result = min(result, memorize(idx + i) + getRank(idx, idx + i - 1)); //해당 구간 난이도+memorize(idx+i)와 result 중 작은 쪽

        return result;

}



int main(void)

{

        int test_case;

        cin >> test_case;

        if (test_case < 1 || test_case>50)

               exit(-1);



        for (int i = 0; i < test_case; i++)

        {

               memset(cache, -1, sizeof(cache));

               cin >> num;

               cout << memorize(0) << endl << endl;

        }

        return 0;

}
