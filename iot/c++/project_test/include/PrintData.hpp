#pragma once
#include <string>
using namespace std;

class PrintData{
  public:
  void print(int i);
  void print(double f);
  void print(string s = "No Data!");  // 초기값 배정 (헤더파일에서만 해주면 된다)
};