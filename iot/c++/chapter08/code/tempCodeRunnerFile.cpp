#include <iostream>
#include <string>
using namespace std;

// void print(string t){
//     cout << t << endl;
// }
// const char *t -> 읽기만 하겠다
void print(const char * t){ // char * t -> *t = 'A'; 가능하다는 소리 
    //(char t[])
    cout << t << endl;
} // test, pstr은 되지만 str은 안 된다 string 쓰고 싶은데 char 쓰고 있음
int main(int argc, char const *argv[]) {
    char test[] = "Hello"; // 문자열 배열
    // 정적할당 -> 스택, test는 첫 엘리먼트를 가리키는 포인터(배열명은 상수)
    // test = 200; -> 에러
    // test[20] = '!'; -> 에러 hello\0으로 6바이트까지 가능
    char *pstr = "C++"; // 문자열 포인터
    // 지역변수 -> 스택에 8바이트
    // C++은 상수 (전역에 있다)
    // *pstr = 'p'; -> c를 p로 바꾸겠다 ->실제로 데이터가 전역변수에 있고 상수 파트에 있기 때문에 이 작업은 오류
    // 읽기는 가능, 쓰기는 오류 -> 컴파일러가 수정 못하게 해주면 좋겠다 -> const
    string str = "World"; //string 객체
    // string(32)바이트 -> 실제 데이터는 힙에 있다
    // cout << test << endl;
    // cout << pstr << endl;
    // cout << str << endl;

    print(test);
    // 문자열 계열이 스트링으로 넘어갈 때 -> string t = test; (복사됨)
    print(pstr);
    // string t = pstr;
    print(str.c_str());
    // string t = str;
    // 지역변수 t는 함수 끝나면 사라진다 ~string()에 의해서 
    // c_str() -> c포인터로 리턴해달라(실제 스트링 객체가 가지는 주소를 리턴)
    // c_str()의 리턴타입은 const char * -> 주소는 알려주지만 주소로 쓰기는 불가능
    return 0;
}