package com.example.bmicalc

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import kotlinx.android.synthetic.main.activity_result.*
import org.jetbrains.anko.longToast

class ResultActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_result)

        val height = intent.getIntExtra("height", 0)
        val weight = intent.getIntExtra("weight", 0)

        val bmi = weight / Math.pow(height / 100.0, 2.0)

        when {
            bmi >= 35 -> resultTextView.text = "고도 비만"
            bmi >= 30 -> resultTextView.text = "2단계 비만"
            bmi >= 25 -> resultTextView.text = "1단계 비만"
            bmi >= 23 -> resultTextView.text = "과체중"
            bmi >= 18.5 -> resultTextView.text = "정상"
            else -> resultTextView.text = "저체중"
        }

        when {
            bmi >= 23 -> imageView.setImageResource(
                R.drawable.ic_bad_24)
            bmi >= 18.5 -> imageView.setImageResource(
                R.drawable.ic_normal_24)
            else -> imageView.setImageResource(
                R.drawable.ic_satisfied_24)
        }
        longToast("키 : $height, 체중: $weight, bmi: $bmi")


    }
}