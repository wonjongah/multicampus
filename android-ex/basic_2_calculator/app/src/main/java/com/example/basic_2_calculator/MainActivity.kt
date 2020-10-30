package com.example.basic_2_calculator

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import kotlinx.android.synthetic.main.activity_main.*

class MainActivity : AppCompatActivity() {

    private  fun subNumber(i: Int, i1: Int): Int {
        return i - i1;
    }

    private fun addNumber(i: Int, i1:Int) : Int{
        return i + i1;
    }

    private fun calculate(pFunc : (Int, Int)->Int, num1 : Int, num2 : Int) : Int{ // 매개변수 타입 지정
        // 첫 번째 인자로 함수 전달
        return pFunc(num1, num2)
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        btnPlus.setOnClickListener{ // + 버튼 눌렀을 때
            // 입력받은 값이 null인지 체크
            if(firstNumber.text == null || secondNumber.text == null){
                return@setOnClickListener
            }
            // 입력받은 값이 ""인지 체크
            if(firstNumber.text.length == 0 || secondNumber.text.length == 0){
                return@setOnClickListener
            }
            
            // 숫자값을 가져오기
            var first = firstNumber.text.toString()
            var second = secondNumber.text.toString()
            
            // 문자열 -> 숫자
            var result = addNumber(first.toInt(), second.toInt())
            txtResult.setText("${result}")
        }


        // - 버튼을 눌렀을 때 (함수형 프로그래밍)
        btnMinus.setOnClickListener {

            val lstCheck = listOf(firstNumber, secondNumber) // 타입 edittext

            lstCheck.map{if (it == null) return@setOnClickListener else it}
                .map { if (it.text.length < 1) return@setOnClickListener else it }
            // it 자기자신 리턴해라라

            val lstNumber = lstCheck.map{ it.text.toString().toInt()}

            lstNumber.let{
                calculate(::subNumber, it.get(0), it.get(1)).let{txtResult.text = "${it}"}
            }
            // let -> let 앞이 매개변수 it이 되는 것
            // it은 calculate의 리턴값
        }
    }
}