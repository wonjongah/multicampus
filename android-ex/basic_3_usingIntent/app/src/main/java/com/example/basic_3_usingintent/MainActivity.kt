package com.example.basic_3_usingintent

import android.content.Intent
import android.net.Uri
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import kotlinx.android.synthetic.main.activity_main.*

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        setUpUI()
    }

    private fun setUpUI(){
        btnSMS.setOnClickListener {
            val uri = Uri.parse("smsto:" + "01026586710") // 프로토콜 지정
            val intent = Intent(Intent.ACTION_SENDTO, uri)

            intent.putExtra("sms_body", "종아 화이팅!!! 얍!!!!!!!!")
            startActivity(intent) // 암묵적, 암시적 호출, 안드로이드가 알아서
        }

        btnInternet.setOnClickListener {
            val uri = Uri.parse("http://vintageappmaker.tumblr.com/")
            val intent = Intent(Intent.ACTION_VIEW, uri)
            startActivity(intent)
        }

        btnMap.setOnClickListener {
            val uri = Uri.parse("geo: 37.5310091,127.0261659")
            val intent = Intent(Intent.ACTION_VIEW, uri)
            startActivity(intent)
        }

        btnMarket.setOnClickListener {
            val uri = Uri.parse("market://details?id=com.psw.moringcall")
            val intent = Intent(Intent.ACTION_VIEW, uri)
            startActivity(intent)
        }
    }

    // 이 일을 한 수 있는 액티비티를 찾아서 실행해달라고 안드로이드에게 부탁
}