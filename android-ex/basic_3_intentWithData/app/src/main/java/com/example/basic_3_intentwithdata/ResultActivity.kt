package com.example.basic_3_intentwithdata

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import kotlinx.android.synthetic.main.activity_main.*

class ResultActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_result)
    }

    override fun onStart() {
        super.onStart()

        val i = intent?: return // null이면 리턴
        // 인텐트가 있으면 i에 ..
         val sID = i.getStringExtra(MainActivity.ID) // mainactivity에 지정된 id와 password
        val sPasswd = i.getStringExtra(MainActivity.PASSWD)

        txtMessage.text = "아이디 ${sID}\n 패스워드 ${sPasswd}"
        i.putExtra(MainActivity.RESULT, txtMessage.text.toString())
        setResult(MainActivity.REQUEST, i)
    }}
