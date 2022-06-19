#include <iostream> 
#include <cmath>
#include <list>
#include <algorithm>


int interval(int list[], int a, int b) {
    for (int i = a; i < b; i++)
    {
        std::cout << list[i]  <<" ";
    }
    return 0;
}
     
int okret(int list[]) {
    for (int i = 10; i > -1; i--)
    {
        std::cout << list[i]  <<" ";
    }
    return 0;
}


int zamjena(int list[], int a, int b){
    for (int i = 0; i < 11; i++)
    {
        int c = list[a];
        list[a] = list[b];
        list[b] = c;
        std::cout << list[i]  <<" ";
    }
    return 0;
}

int sort_min_max(int lista[], int k)
{
    for(int i = 0; i < k; i++) 
    {
        std::cout << lista[i] << " ";
    }
    std::cout << std::endl;
    return 0;
}
int sort_max_min(int lista[], int k)
{
    for(int i = 0; i < k; i++) 
    {
        std::cout << lista[i] << " ";
    }
    std::cout << std::endl;
    return 0;
}




int main() {
    int polje[] = {3, 0, 2, 1, 4, 7, 6, 8, 9, 10, 5};
    //interval(polje, 3, 8);
    //okret(polje);
    //zamjena(polje, 10, 9);
    std::sort(std::begin(polje), std::end(polje));
    //sort_min_max(polje, 11);
    std::reverse(std::begin(polje), std::end(polje));
    //sort_max_min(polje, 11);
    
}
