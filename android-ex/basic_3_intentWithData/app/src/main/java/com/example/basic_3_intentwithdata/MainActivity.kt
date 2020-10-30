package com.example.basic_3_intentwithdata

import android.content.Intent
import android.graphics.Color
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.EditText
import kotlinx.android.synthetic.main.activity_main.*

class MainActivity : AppCompatActivity() {

    companion object{ // 내부객체, 파이썬의 static, 접근할 때 MainActivity.ID 이런식으로 접근
        val REQUEST = 0
        val ID = "ID"
        val PASSWD = "PASSWD"
        val RESULT = "RESULT"
    }
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        edtId.setOnFocusChangeListener(){v, hasFocus ->
            val edt = v as EditText
            val color = if(hasFocus){
                Color.TRANSPARENT
            }else{
                Color.LTGRAY
            }
            edt.setBackgroundColor(color)
        }

        btnLogin.setOnClickListener {
            val i = Intent(this, ResultActivity::class.java)
            i.putExtra(ID, edtId.text.toString())
            startActivityForResult(i, REQUEST)
        }
    }

    override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent?) {
        // startActivity의 RESULT에 사용했던 게 requestCode로 넘어감
        // 두 번째의 resultCode는 종료코드, 어떻게 종료했는지.. 정상종료 메모리 부족해서 종료 등
        // data 실질적 데이터 들어있음

        if(requestCode != REQUEST) return // 액티비티 구분하는 코드, 여러개의 액티비티 있으면 swicth or 다중if

        // if(data != null)
        data?.getStringExtra(RESULT).let {
            txtMessage.text = it
        }

        super.onActivityResult(requestCode, resultCode, data)
    }
}