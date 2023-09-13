#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;




int main(void)
{

	int n;
	cin >> n;
	vector <int> arr;
	vector <int> copy;

	int tmp;
	for (int i = 0; i < n; i++) {
		cin >> tmp;
		arr.push_back(tmp);
		copy.push_back(tmp);
	}

	sort(copy.begin(), copy.end());
	copy.erase(unique(copy.begin(), copy.end()), copy.end());

	for (int i = 0; i < n; i++) {
		cout  << lower_bound(copy.begin(), copy.end(), arr[i])-copy.begin() << " ";
	}


	return 0;
}