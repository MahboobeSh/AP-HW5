#include <iostream>
#include <vector>
#include <algorithm>
#include <functional>
#include <set>


template< typename T>
void print(const T& v);


int main()
{
    std::vector<int> vec1(100);
    std::vector<int> vec2(10);

    int num{1};
    std::for_each(vec1.begin(),vec1.end() ,[&num](int &i){i = num;  num++;});
    num =1;
    std::for_each(vec2.begin(),vec2.end() ,[&num](int &i){i = num;  num++;});

   // print(vec1);
   // print(vec2);
    vec1.resize(110);
    std::copy(vec2.begin(),vec2.end(),vec1.end()-10);
   // print(vec1);

    std::vector<int> odd_vec(55);
    std::copy_if(vec1.begin(),vec1.end(),odd_vec.begin(),[](int i){return i%2!=0;});
    print(odd_vec);

    std::vector<int> reverse_vec(110);
    std::copy(vec1.rbegin(),vec1.rend(),reverse_vec.begin());
    print(reverse_vec);



    return 0;
}

template< typename T>
void print(const T& v)
{
	for (auto x : v)
		std::cout << x << ", ";
	
	std::cout << "\n";
}