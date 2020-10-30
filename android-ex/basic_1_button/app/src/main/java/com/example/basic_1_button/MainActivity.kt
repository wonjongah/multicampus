package com.example.basic_1_button

import android.graphics.Color
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.Button
import android.widget.TextView
import org.w3c.dom.Text

class MainActivity : AppCompatActivity() {

    var nCount : Int = 0

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)


        var btn2 = findViewById<Button>(R.id.btn2)
        btn2.setOnClickListener { // 버튼을 클릭했을 때 호출할 함수 등록, 람다함수

            // btn2.text = ".."
            // btn2.setTextColor()
            // btn2.setBackgroundColor()

            btn2.apply {// apply -> this를 호출한 인스턴스로 바꿔주는 메서드, this는 btn2이 되었다
                text = "Cilck" // this.text한 것이랑 같다
                setTextColor(Color.parseColor("#333333"))
                setBackgroundColor(Color.parseColor("#FFFF33"))
                // btn2의 작업
            }
        }

        var txtNormal = findViewById<TextView>(R.id.txtNormal)
        var txtHtml = findViewById<TextView>(R.id.txtHtml)
        txtNormal.setOnClickListener {
            txtNormal.apply{
                setBackgroundColor(Color.RED)
                text = "Clicked!! ${nCount++}"
                setTextColor(Color.WHITE)
                setTextSize(28.0f)
            }
        }

        txtHtml.setOnClickListener {
            
        }



    }
}