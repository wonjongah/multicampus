package com.example.basic_2_logcat

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.util.Log
import kotlinx.android.synthetic.main.activity_main.*
import java.lang.Exception

class MainActivity : AppCompatActivity() {

    val TAG = "MainActivity"
    var nCount : Int = 0
    var nMaxCount : Int = 10
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        btnLogcatTest.setOnClickListener {
            Log.d(TAG, "${nCount++} clicked")
            try{
                val nResult = nMaxCount / (nMaxCount - nCount)
                Log.d(TAG, "nMaxCount / (nMaxCount - nCount) is ${nResult}")
            } catch(e:Exception){
                Log.e(TAG, "${nCount} : ${e.toString()}")
            }
        }
    }
}