package com.example.basic_2_activitylife

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.util.Log

class MainActivity : AppCompatActivity() {
    var nLineNumber = 0
    val TAG = "ALLTEST"
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        Log.d(TAG, String.format("\n%d: onCreate", nLineNumber++))
        // log.d(TAG, ${nLineNumber++} onCreate")
    }

    override fun onStart() {
        super.onStart()
        Log.d(TAG, String.format("%d: onStart", nLineNumber++))
    }

    override fun onResume() {
        super.onResume()
        Log.d(TAG, String.format("%d: onResume", nLineNumber++))

    }

    override fun onStop() {
        super.onStop()
        Log.d(TAG, String.format("%d: onStop", nLineNumber++))

    }

    override fun onDestroy() {
        super.onDestroy()
        Log.d(TAG, String.format("%d: onDestroy", nLineNumber++))

    }
}