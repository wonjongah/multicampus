package com.example.edittext

import android.graphics.Color
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.text.Editable
import android.text.TextWatcher
import android.widget.EditText
import androidx.constraintlayout.widget.ConstraintLayout
import androidx.core.widget.addTextChangedListener
import kotlinx.android.synthetic.main.activity_main.*

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)


        edtName.setOnFocusChangeListener { v, hasFocus ->
            val edt = v as EditText
            val color = if(hasFocus){
                Color.TRANSPARENT // 투명
            } else{
                Color.LTGRAY
            }
            edt.setBackgroundColor(color)
        }
        // MainActivity의 멤버변수인 edtName
        // 타입은 EditText
        editTextTextPassword2.addTextChangedListener(object: TextWatcher{ // 추상메서드, 인터페이스만 있다, 오버라이드해줘야 함
            // 익명 구현 객체
            override fun afterTextChanged(s: Editable?) {
            }

            override fun beforeTextChanged(s: CharSequence?, start: Int, count: Int, after: Int) {
            }

            override fun onTextChanged(s: CharSequence?, start: Int, before: Int, count: Int) {
                txtViewPassWd.text = s
            }
        })

    }
}


